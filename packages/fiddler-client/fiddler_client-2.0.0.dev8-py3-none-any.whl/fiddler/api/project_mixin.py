from http import HTTPStatus
from typing import List

from pydantic import parse_obj_as

from fiddler.libs.http_client import RequestClient
from fiddler.schema.project import Project
from fiddler.utils.compatibility_helpers import project_id_compat
from fiddler.utils.decorators import handle_api_error_response
from fiddler.utils.logger import get_logger
from fiddler.utils.response_handler import (
    APIResponseHandler,
    PaginatedResponseHandler,
)

logger = get_logger(__name__)


class ProjectMixin:
    client: RequestClient
    organization_name: str

    @handle_api_error_response
    def get_projects(self, limit: int = 300, offset: int = 0) -> List[Project]:
        """
        Get a list of all projects in the organization

        :params limit: Number of projects to fetch in a call
        :params offset: Number of rows to skip before any rows are retrived
        :returns: List of `Project` object
        """
        response = self.client.get(
            url='projects',
            params={
                'organization_name': self.organization_name,
                'limit': limit,
                'offset': offset,
            },
        )
        # @TODO:  abstracted as an iter object so user doesn't have to manage pagination manually
        items = PaginatedResponseHandler(response).get_pagination_items()
        return parse_obj_as(List[Project], items)

    # Projects
    def get_project_names(self) -> List[str]:
        """List the ids of all projects in the organization.

        :returns: List of strings containing the ids of each project.
        """
        projects = self.get_projects()
        return [p.name for p in projects]

    @handle_api_error_response
    def delete_project(self, project_id: str = None, project_name: str = None) -> None:
        """
        Delete a project

        :params project_id: Name of the project to delete
        :params project_name: Name of the project to delete
        :returns: None
        """
        project_name = project_id_compat(
            project_id=project_id, project_name=project_name
        )
        response = self.client.delete(
            url=f'projects/{self.organization_name}:{project_name}'
        )
        if response.status_code == HTTPStatus.OK:
            logger.info(f'{project_name} deleted successfully.')
        else:
            # @TODO: Handle non 200 status response
            logger.info('Delete unsuccessful')

    @handle_api_error_response
    def add_project(self, project_name: str) -> Project:
        """
        Add a new project.

        :param project_name: The unique identifier of the project on the
            Fiddler engine. Must be a short string without whitespace.

        :returns: Created `Project` object.
        """
        request_body = Project(
            name=project_name, organization_name=self.organization_name
        ).dict()
        response = self.client.post(
            url='projects',
            params={'organization_name': self.organization_name},
            data=request_body,
        )
        logger.info(f'{project_name} created successfully!')
        return Project.deserialize(APIResponseHandler(response))
