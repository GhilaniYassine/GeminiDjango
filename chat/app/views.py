from django.shortcuts import render

from django.http import HttpResponse

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services.gemini_service import GeminiService

def chat_home(request):
    """Render the chat interface"""
    return render(request, 'chat_interface.html')

class ChatAPIView(APIView):
    """API endpoint for chat interactions"""
    def post(self, request):
        message = request.data.get('message', '')
        if not message:
            return Response(
                {'error': 'No message provided'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Initialize the Gemini service
        gemini_service = GeminiService()
        
        # Get response from Gemini
        response_text = gemini_service.generate_response(message)
        
        return Response({'response': response_text}) 