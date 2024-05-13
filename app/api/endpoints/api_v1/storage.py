from enum import Enum
from azure.storage.blob import BlobServiceClient
from fastapi import APIRouter, File, UploadFile, HTTPException, Response
from app.core.config import Settings


class Partner(Enum):
    PARTNER_ONE = "partner_one"
    PARTNER_TWO = "partner_two"


class CloudStorageApiRouter:
    def __init__(self):
        self.router = APIRouter(tags=["storage"])
        self.blob_service_client = BlobServiceClient.from_connection_string(Settings().AZURE_STORAGE_CONNECTION_STRING)
        self.init_routes()

    def init_routes(self):
        self.router.add_api_route("/upload-file-to-azure", self.upload_file_to_azure, methods=["POST"], status_code=201)
        self.router.add_api_route("/list-files", self.list_files, methods=["GET"])
        self.router.add_api_route("/download-file/{blob_name}", self.download_file, methods=["GET"])

    async def upload_file_to_azure(self, partner: Partner, file: UploadFile = File(...)) -> dict:
        """Upload a file to Azure Blob Storage."""
        container_path = f"{Settings().AZURE_CONTAINER_NAME}/{partner.value}"
        blob_client = self.blob_service_client.get_blob_client(container=container_path, blob=file.filename)
        try:
            file_content = await file.read()
            blob_client.upload_blob(file_content, overwrite=True)
            return {"message": f"Successfully uploaded {file.filename} to Azure Blob Storage in {partner.value}."}
        except Exception as e:
            print(f"Failed to upload {file.filename} to {partner.value}: {str(e)}")
            raise HTTPException(status_code=500, detail=str(e))

    async def list_files(self, partner: Partner) -> dict:
        """List all files in the specified partner's Azure Blob Storage container."""
        container_path = f"{Settings().AZURE_CONTAINER_NAME}/{partner.value}"
        container_client = self.blob_service_client.get_container_client(container=container_path)
        blob_list = container_client.list_blobs()
        return {"files": [blob.name for blob in blob_list]}

    async def download_file(self, partner: Partner, blob_name: str):
        """Download a specific file from the specified partner's Azure Blob Storage container."""
        container_path = f"{Settings().AZURE_CONTAINER_NAME}/{partner.value}"
        blob_client = self.blob_service_client.get_blob_client(container=container_path, blob=blob_name)
        stream = blob_client.download_blob()
        return Response(stream, media_type="application/octet-stream")







