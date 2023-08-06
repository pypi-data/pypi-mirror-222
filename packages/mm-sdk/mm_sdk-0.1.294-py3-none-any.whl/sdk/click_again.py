from pydantic import BaseModel

from .client import HttpUrl, SDKClient, SDKResponse


class DeleteOrgResponse(BaseModel):
    status: str


class ClickAgainService:
    def __init__(self, client: SDKClient, url: HttpUrl):
        self._client = client
        self._url = url
        self.delete_url = self._url + "/api/delete_org_from_amocrm/?org_amo_id="

    def delete_amocrm_org(self, org_amo_id: int) -> SDKResponse[DeleteOrgResponse]:
        return self._client.get(
            self.delete_url + f"{org_amo_id}",
            DeleteOrgResponse,
            timeout=60,
        )
