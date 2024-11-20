from src.services.blob_service import BlobService
from src.services.credit_card_service import CreditCardService
from src.utils.Config import Config

def main():
    # Instância dos serviços
    blob_service = BlobService(Config.AZURE_BLOB_CONNECTION_STRING, Config.AZURE_BLOB_CONTAINER_NAME)
    credit_card_service = CreditCardService(Config.AZURE_FORMRECOGNIZER_ENDPOINT, Config.AZURE_FORMRECOGNIZER_KEY)
    
    # Exemplo de upload e análise
    file_path = "document.pdf"
    blob_name = "uploaded_document.pdf"
    
    blob_service.upload_document(file_path, blob_name)
    document_url = f"https://{Config.AZURE_BLOB_CONTAINER_NAME}.blob.core.windows.net/{blob_name}"
    result = credit_card_service.analyze_credit_card(document_url)
    
    print("Análise concluída:", result)

if __name__ == "__main__":
    main()
