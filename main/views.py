from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import Survey

def index(request):
    return render(request, 'main/surveyform.html')

@csrf_protect
def get_survey_result(request):
    if request.method != 'POST':
        return render(request, 'main/surveyform.html')

    preferred_weight = request.POST.get('preferred_weight')
    activity_level = request.POST.get('activity_level')
    has_children = request.POST.get('has_children') == 'on'
    has_allergy = request.POST.get('has_allergy') == 'on'
    has_other_dogs = request.POST.get('has_other_dogs') == 'on'
    has_time_for_grooming = request.POST.get('has_time_for_grooming') == 'on'
    home_type = request.POST.get('home_type')

    try:
        Survey.objects.create(
            has_children=has_children,
            home_type=home_type,
            activity_level=activity_level,
            preferred_weight=preferred_weight,
            has_allergy=has_allergy,
            has_other_dogs=has_other_dogs,
            has_time_for_grooming=has_time_for_grooming
        )
    except Exception as e:
        print(f'Error: {e}')

    return redirect('index')