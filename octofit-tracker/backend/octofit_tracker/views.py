# Update the return for the REST API URL endpoints to use the codespace URL
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView

class ExampleView(APIView):
    def get(self, request):
        api_suffix = settings.CODESPACE_API_SUFFIX
        codespace_url = "https://fantastic-zebra-x6jgv49q9pp2vj9w-8000.app.github.dev"
        return Response({"message": f"API endpoint is {codespace_url}{api_suffix}"})