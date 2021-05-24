from .views import QuestionView
from django.urls import path
urlpatterns = [
                path('questions', QuestionView.as_view()),
                ]