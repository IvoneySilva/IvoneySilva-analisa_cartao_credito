from azure.storage.blob import BlobServiceClient
import os

class BlobService:
    def __init__(self, connection_string, container_name):
        self.blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        self.container_name = container_name

    def upload_document(self, file_path, blob_name):
        container_client = self.blob_service_client.get_container_client(self.container_name)
        with open(file_path, "rb") as data:
            container_client.upload_blob(blob_name, data)
        print(f"File {file_path} uploaded as {blob_name}.")

    def download_document(self, blob_name, download_path):
        container_client = self.blob_service_client.get_container_client(self.container_name)
        with open(download_path, "wb") as file:
            file.write(container_client.download_blob(blob_name).readall())
        print(f"Blob {blob_name} downloaded to {download_path}.")
