from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

class CreditCardService:
    def __init__(self, endpoint, key):
        self.client = DocumentAnalysisClient(endpoint, AzureKeyCredential(key))

    def analyze_credit_card(self, document_url):
        poller = self.client.begin_analyze_document("prebuilt-document", document_url)
        result = poller.result()
        for field in result.fields:
            print(f"{field}: {result.fields[field].value}")
        return result
