from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from questions.models import Answer, Question
from quiz.models import Quiz
from results.models import Result

class QuizListView(ListView):
    model = Quiz
    template_name = "home.html"

def quiz_view(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    context = {
        "quiz": quiz
    }
    return render(request, "quiz/quiz.html", context)

def quiz_data_view(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    questions = []

    # Prepare the questions and their answers in a structured format
    for q in quiz.get_questions():
        answers = [a.text for a in q.get_answers()]  # List comprehension to get answer texts
        questions.append({str(q): answers})  # Use str(q) to get a string representation of the question
    
    return JsonResponse({
        'data': questions,
        'time': quiz.time  # Include the time for the quiz
    })

def send_quiz_view(request, pk):
    if request.is_ajax():
        data = request.POST.dict()  # Convert POST data to a dictionary
        data.pop('csrfmiddlewaretoken')  # Remove CSRF token

        quiz = get_object_or_404(Quiz, pk=pk)
        user = request.user
        score = 0
        results = []
        
        # Iterate through submitted answers
        for question_text, answer_text in data.items():
            question = get_object_or_404(Question, text=question_text)
            correct_answer = None
            
            if answer_text:
                question_answers = Answer.objects.filter(question=question)
                for answer in question_answers:
                    if answer.text == answer_text:
                        if answer.correct:
                            score += 1
                        correct_answer = answer.text
                    elif answer.correct:
                        correct_answer = answer.text
                
                results.append({
                    str(question): {  # Use str(question) for readable key
                        'correct_answer': correct_answer,
                        'answered': answer_text
                    }
                })
            else:
                results.append({
                    str(question): {'not_answered': 'No answer provided'}
                })

        # Calculate the score as a percentage
        score_percentage = (score / quiz.number_of_questions) * 100
        Result.objects.create(quiz=quiz, user=user, score=score_percentage)

        # Return JSON response with the results
        return JsonResponse({
            'passed': score_percentage >= quiz.required_score_to_pass,
            'score': score_percentage,
            'results': results
        })

