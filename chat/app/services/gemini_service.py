import google.generativeai as genai
from django.conf import settings

class GeminiService:
    def __init__(self):
        self.api_key = settings.GEMINI_API_KEY
        genai.configure(api_key=self.api_key)
<<<<<<< HEAD
        self.model = genai.GenerativeModel('gemini-2.0-flash')
=======
        self.model = genai.GenerativeModel('gemini-1.0-pro')
>>>>>>> 20e128895b83184b894cd4fb3d8bf9cc08c331bc

    def generate_response(self, user_input):
        try:
            response = self.model.generate_content(user_input)
            return response.text
        except Exception as e:
            print(f"Error when calling Gemini API: {e}")
            return "Sorry, I couldn't process your request at the moment."