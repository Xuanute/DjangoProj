from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice


# Create your views here.

def index(request):
    name = "Xuan"
    return render(request, "polls/index.html", {"name": name})


def product_detail(request):
    return HttpResponse("<h1>Product detail page</h1>")


def get_question_list(request):
    list_question = Question.objects.all()
    context = {
        'questions': list_question
    }
    return render(request, "polls/question_list.html", context)
