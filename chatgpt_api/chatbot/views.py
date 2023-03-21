from django.shortcuts import render
import openai
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.views import APIView

openai.api_key = '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'

@method_decorator(csrf_exempt,name='dispatch')
class chatbot_response(APIView):
    def post(self, request):
        question = request.data['question']
        prompt = request.POST.get('prompt', question)
        model = request.POST.get('model', 'text-davinci-002')
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        output_text = ' '.join(i['text'] for i in response['choices'])
        return Response({'question':question, "answer": output_text})
