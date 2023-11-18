from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import os
import json

api_key = os.environ.get('API_KEY')

class SearchAPIView(APIView):
    def get(self, request):
        # Get the search query from the user
        query = request.GET.get('q', '')

        # Define the API parameters
        api_url = "https://www.searchapi.io/api/v1/search"
        params = {
            "engine": "google_shopping",
            "q": query,
            "location": "Tamil Nadu,India",
            "location_used": "Tamil Nadu,India",
            "google_domain": "google.co.in",
            "hl": "en",
            "gl": "in",
            "num": "60",
            "api_key": api_key
    
        }

        # Make the API request
        response = requests.get(api_url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            return Response(data)
        else:
            return Response({"error": f"Error: {response.status_code}, {response.text}"})
