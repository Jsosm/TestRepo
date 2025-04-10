from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")
    output = "<table>"
    output += "<tr><th>Question</th></tr>"

    for q in latest_question_list:
        output += "<tr>"
        output += "<td>"
        output += q.question_text
        output += "</td>"

        output += "<td>"
        output += str(q.pub_date)
        output += "</td>"


        output += "<td>"
        output += str(q.num)
        output += "</td>"

        output += "</tr>"

   # ", ".join([q.question_text for q in latest_question_list]) 
    output += "</tr></table>"
    

    return HttpResponse(output)