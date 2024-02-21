from datetime import datetime

import requests
from pydantic import BaseModel

from devops.settings import settings
from devops.utils import check_valid_server_response


class ReleaseDefinition(BaseModel):
    id: int
    name: str


class Release(BaseModel):
    id: int
    name: str
    createdOn: datetime
    releaseDefinition: ReleaseDefinition

    def get_deployed_environments(self, project_id: str):
        response = requests.request(
            method="GET",
            url=f'{settings.VSRM_BASE_URL}/{settings.ORGANIZATION}/{project_id}/_apis/release/releases/{self.id}?api-version=7.2-preview.8',
            auth=settings.get_authentication_headers(),
        )

        check_valid_server_response(response, f"get logs for the release {self.name}")
        environments = response.json()['environments']

        return {env['name'] for env in environments if env['name'] if env['status'] != 'notStarted'}
