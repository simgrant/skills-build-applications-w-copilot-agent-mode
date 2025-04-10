# Use the codespace Django REST API endpoint suffix
from django.conf import settings

# Example usage in a view
class ExampleView(APIView):
    def get(self, request):
        api_suffix = settings.CODESPACE_API_SUFFIX
        return Response({"message": f"API endpoint suffix is {api_suffix}"})