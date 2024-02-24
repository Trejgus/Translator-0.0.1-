from rest_framework.views import APIView
from django.http import JsonResponse, HttpRequest
from .translator import translate

class APITranslate(APIView):
    
    def get(self, request: HttpRequest, text, to_lang, translator='google'):
        result = translate(text, to_lang, translator)
        return JsonResponse({"result": result}, status = 200)