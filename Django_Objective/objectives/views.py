from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Objective

# Create your views here.
def index(request):
    objective_list = Objective.objects.all()
    context = {
            'objective_list': objective_list,
 }
    return render(request, "objectives/index.html", context)

def objective_details(request, objective_id):
    try:
       objective = Objective.objects.get(pk=objective_id)
    except Objective.DoesNotExist:
       raise Http404("Question does not exist")
    return render(request, 'objective/detail.html', {'objective': objective})