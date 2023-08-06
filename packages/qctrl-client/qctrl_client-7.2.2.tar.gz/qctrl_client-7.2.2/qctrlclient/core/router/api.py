# Copyright 2023 Q-CTRL. All rights reserved.
#
# Licensed under the Q-CTRL Terms of service (the "License"). Unauthorized
# copying or use of this file, via any medium, is strictly prohibited.
# Proprietary and confidential. You may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#    https://q-ctrl.com/terms
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS. See the
# License for the specific language.

import json
from dataclasses import dataclass
from enum import Enum
from functools import cached_property
from typing import (
    Any,
    Dict,
    List,
    Optional,
)
from warnings import warn

import gql
from qctrlcommons.serializers import (
    DataTypeDecoder,
    DataTypeEncoder,
)
from tenacity import (
    retry,
    retry_if_result,
    wait_chain,
    wait_fixed,
)

from qctrlclient import GraphQLClient
from qctrlclient.core.settings import CoreClientSettings
from qctrlclient.core.utils import (
    get_installed_version,
    show_error_message,
)
from qctrlclient.exceptions import GraphQLClientError

from .base import BaseRouter

# every 2s for the first 30s, then every 10s
_POLL_WAIT_CHAIN = wait_chain(*[wait_fixed(2) for _ in range(15)] + [wait_fixed(10)])


class ActionStatus(Enum):
    """Valid Action statuses."""

    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"
    REVOKED = "REVOKED"


@dataclass
class Organization:
    """Simple client-side representation of an Organization.

    Parameters
    ----------
    organization_id : str
        The unique organization identifier.
    slug : str
        The unique organization slug.
    name : str
        The name of the organization.
    """

    organization_id: str
    slug: str
    name: str

    def to_dict(self) -> Dict[str, str]:
        """
        The dictionary representation of the organization.
        """
        return {
            "id": self.organization_id,
            "slug": self.slug,
            "name": self.name,
        }


@dataclass
class Action:
    """Simple client-side representation of the Action
    model.

    Parameters
    ----------
    action_id : str
        The unique action identifier.
    status : str, optional
        The current status of the action.
    raw_result : Any, options
        The raw, encoded result retrieved from the
        API. Use the `result` property to get the
        decoded result.
    errors : List[Dict[str, Any]], optional
        List of any errors that occurred during
        execution.
    """

    action_id: str
    status: Optional[str] = None
    raw_result: Optional[Any] = None
    errors: Optional[List[Dict[str, Any]]] = None

    @property
    def result(self) -> Any:
        """Returns the decoded result."""
        _result = self.raw_result

        if _result is not None:
            _result = json.loads(_result, cls=DataTypeDecoder)

        return _result

    def is_finished(self) -> bool:
        """Checks if the action has finished."""
        return self.status in (
            ActionStatus.SUCCESS.value,
            ActionStatus.FAILURE.value,
            ActionStatus.REVOKED.value,
        )

    def is_failed(self) -> bool:
        """Checks if the action failed."""
        return self.status == ActionStatus.FAILURE.value

    def is_revoked(self) -> bool:
        """Checks if the action was revoked."""
        return self.status == ActionStatus.REVOKED.value


class ApiRouter(BaseRouter):
    """Remotely executes the workflow using the `startCoreWorkflow`
    GraphQL mutation.

    Parameters
    ----------
    client : GraphQLClient
        The GraphQL client used to make the request to execute
        the workflow remotely.
    registry : Registry
        The registry that the workflows being executed are
        registered in.
    """

    _TRACKED_PACKAGES = [
        "boulder-opal",
        "fire-opal",
        "qctrl-client",
        "qctrl-commons",
    ]

    def __init__(self, client: GraphQLClient, settings: CoreClientSettings):
        self._client = client
        self._settings = settings
        self._validate()

    def _validate(self):
        """Performs validation checks on the settings."""

        if not self._settings.product:
            raise GraphQLClientError("`product` must be configured in settings")

        self._check_has_organizations()
        self._check_must_set_organization()
        self._check_organization_permission()

    def _check_must_set_organization(self):
        if self._settings.organization:
            return

        if len(self._organizations) > 1:
            error_message = "You are assigned to multiple organizations. "
            error_message += "Please configure an organization:\n\n"

            for organization in self._organizations:
                error_message += f"- {organization.slug}\n"

            show_error_message(error_message)

    def _check_has_organizations(self):
        # if no organizations found
        if not self._organizations:
            show_error_message("No organizations found")

    def _check_organization_permission(self):
        """Checks that the user is assigned to the configured
        organization. Requires that the `organization` setting
        is configured.

        Parameters
        ----------
        organizations : List[Organization]
            List of organizations that the user is assigned to which provide
            access to the corresponding product.
        """

        assigned = False

        if not self._settings.organization:
            return

        for organization in self._organizations:
            if organization.slug == self._settings.organization:
                assigned = True
                break

        if not assigned:
            show_error_message(
                f"Configured organization not found: `{self._settings.organization}`"
            )

    @property
    def _organization(self) -> Organization:
        """Returns the organization that the user is assigned to
        which provides access to the configured product.
        """

        if self._settings.organization:
            for organization in self._organizations:
                if organization.slug == self._settings.organization:
                    return organization

        if len(self._organizations) == 1:
            return self._organizations[0]

        raise GraphQLClientError(
            f"Configured organization not found: `{self._settings.organization}`"
        )

    @cached_property
    def _organizations(self) -> List[Organization]:
        """Returns the list of organizations that the user is
        assigned to which provide access to the configured product.
        """

        query = gql.gql(
            """
            query {
                profile {
                    profile {
                        organizations {
                            id
                            slug
                            name
                            products {
                                name
                                active
                            }
                        }
                    }
                    errors {
                        fields
                        message
                    }
                }
            }
        """
        )

        response = self._client.execute(query)
        data = response["profile"]["profile"]["organizations"]
        organizations = []

        for organization_data in data:
            if self._has_product_access(
                organization_data, self._settings.product.value.name
            ):
                organizations.append(
                    Organization(
                        organization_id=organization_data["id"],
                        slug=organization_data["slug"],
                        name=organization_data["name"],
                    )
                )

        return organizations

    @staticmethod
    def _has_product_access(organization_data: Dict, product_name: str) -> bool:
        """Convenience function to check if the organization
        has access to the given product. The format of
        `organization_data` is based on the output of the query
        in `_get_organizations`.
        """

        for product_data in organization_data["products"]:
            if product_data["name"] == product_name:
                return product_data["active"]

        return False

    def __call__(self, workflow, data=None):

        query = gql.gql(
            """
            mutation ($input: StartCoreWorkflowInput!) {
                startCoreWorkflow(input: $input) {
                    action {
                        modelId
                        status
                        result
                        errors {
                            exception
                            traceback
                        }
                    }
                    warnings {
                        message
                    }
                    errors {
                        message
                        fields
                    }
                }
            }
        """
        )

        client_metadata = self._get_client_metadata()
        input_ = {
            "registry": self._settings.product.value.registry,
            "workflow": workflow,
            "data": json.dumps(data, cls=DataTypeEncoder),
            "clientMetadata": json.dumps(client_metadata),
        }

        response = self._client.execute(query, {"input": input_})

        # pylint:disable=unsubscriptable-object

        self._handle_warnings(response["startCoreWorkflow"]["warnings"])
        action_data = response["startCoreWorkflow"]["action"]

        action = Action(
            action_id=action_data["modelId"],
            status=action_data["status"],
            raw_result=action_data["result"],
            errors=action_data["errors"],
        )

        return self.get_result(action)

    def _get_client_metadata(self) -> Dict[str, Any]:
        """Return the client metadata to be included on the
        request to start the workflow.
        """

        package_versions = {}

        for package in self._TRACKED_PACKAGES:
            package_versions[package] = get_installed_version(package)

        return {
            "package_versions": package_versions,
            "organization_slug": self._organization.slug,
            "organization": self._organization.to_dict(),
        }

    @staticmethod
    def _handle_warnings(warnings_data: List[Dict[str, Any]]):
        """Handles warnings returned when starting a workflow."""

        for warning_data in warnings_data:
            message = warning_data["message"]
            warn(Warning(message))

    @retry(
        wait=_POLL_WAIT_CHAIN,
        retry=retry_if_result(lambda action: not action.is_finished()),
    )
    def _poll_for_completion(self, action: Action) -> Action:
        """Polls the API waiting for the action to be finished.
        When finished, an updated `Action` object is returned.
        """

        _query = gql.gql(
            """
            query($modelId: String!) {
                action(modelId: $modelId) {
                    action {
                        status
                        errors {
                            exception
                            traceback
                        }
                        result
                    }
                    errors {
                        message
                    }
                }
            }
        """
        )

        response = self._client.execute(_query, {"modelId": action.action_id})
        action.status = response["action"]["action"]["status"]
        action.raw_result = response["action"]["action"]["result"]
        action.errors = response["action"]["action"]["errors"]
        return action

    def get_result(self, action: Action) -> Any:
        """Returns the result of the action. If the action
        has not finished, the API will be polled until it has.
        If the action has failed, a `RuntimeError` will be
        raised.
        """

        if not action.is_finished():
            action = self._poll_for_completion(action)

        if action.is_failed():
            raise RuntimeError(action.errors)

        if action.is_revoked():
            raise RuntimeError("The action was cancelled")

        return action.result
