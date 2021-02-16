from django.shortcuts import render
from .forms import createCaseForm

# Create your views here.
def Case(request):
    createcaseform = createCaseForm()
    return render(request, 'medicalCase/Case.html', {'case_form': createcaseform})

