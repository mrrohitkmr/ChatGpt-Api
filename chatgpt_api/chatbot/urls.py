from django.urls import path
from .views import chatbot_response

urlpatterns = [
    path('chatbot/', chatbot_response.as_view()),
]
