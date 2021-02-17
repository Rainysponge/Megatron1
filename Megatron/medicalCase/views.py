from django.shortcuts import render
from .forms import createCaseForm


# Create your views here.
def Case(request):
    context = {}
    if request.method == 'POST':
        create_case_form = createCaseForm(request.POST)
        if create_case_form.is_valid():
            patient_id = create_case_form.cleaned_data['patient_No']
            # pay_No = create_order_form.cleaned_data['']
            # shop_id = create_order_form.cleaned_data['shop_id']
            # shop_id = str(user.pk) + '_' + shop_id
            context['patient_id'] = patient_id
    else:
        create_case_form = createCaseForm()
    context['case_form'] = create_case_form

    return render(request, 'medicalCase/Case.html', context)
