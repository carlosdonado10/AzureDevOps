from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from typing import List
from collections import Counter

import pandas as pd
import requests
from pydantic import BaseModel
from tqdm import tqdm

from devops.components.release import Release, ReleaseDefinition
from devops.settings import settings
from devops.utils import check_valid_server_response


class Project(BaseModel):
    id: str
    name: str

    @classmethod
    def get_list_of_projects(cls) -> List["Project"]:
        response = requests.request(
            method="GET",
            url=f"{settings.BASE_URL}/{settings.ORGANIZATION}/_apis/projects?api-version=7.2-preview.4",
            auth=settings.get_authentication_headers()
        )

        check_valid_server_response(response, f"get projects for organization {settings.ORGANIZATION}")

        return [cls(**project_data) for project_data in response.json()['value']]

    def get_list_of_pipelines(self):
        response = requests.request(
            method="GET",
            url=f'{settings.BASE_URL}/{settings.ORGANIZATION}/{self.id}/_apis/pipelines?api-version=7.2-preview.1',
            auth=settings.get_authentication_headers()
        )

        check_valid_server_response(response, f"get pipelines for project {self.name}")

        return response.json()['value']

    def get_list_of_releases_by_dates(self, start_date: datetime, end_date: datetime):
        date_params = {
            "minCreatedTime": start_date,
            "maxCreatedTime": end_date,
        }

        response = requests.request(
            method="GET",
            url=f'{settings.VSRM_BASE_URL}/{settings.ORGANIZATION}/{self.id}/_apis/release/releases?api-version=7.2-preview.8',
            auth=settings.get_authentication_headers(),
            params=date_params
        )

        check_valid_server_response(response, f"get pipelines for project {self.name}")

        return [Release(**release_data, release_definition=ReleaseDefinition(**release_data["releaseDefinition"])) for
                release_data in response.json()['value']]