from typing import Dict, Tuple

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ORGANIZATION: str
    BASE_URL: str = "https://dev.azure.com"
    VSRM_BASE_URL: str = "https://vsrm.dev.azure.com"
    PAT: str

    def get_authentication_headers(self) -> Tuple[str, str]:
        return 'something', self.PAT


settings = Settings()
