from django.urls import path
from .views import QuizListView, quiz_data_view, quiz_view, send_quiz_view

app_name = "quiz"

urlpatterns = [
    path('', QuizListView.as_view(), name='main-view'),
    path('<pk>/', quiz_view, name='quiz-view'),
    path('<pk>/data/', quiz_data_view, name='quiz-data-view'),
    path('<pk>/save/', send_quiz_view, name='send-quiz-view'),
]
