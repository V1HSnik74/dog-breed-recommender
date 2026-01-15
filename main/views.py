from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import Survey, DogBreed, Recommendation

def index(request):
    return render(request, 'main/surveyform.html')

@csrf_protect
def get_survey_result(request):
    if request.method != 'POST':
        return render(request, 'main/surveyform.html')

    preferred_weight = int(request.POST.get('preferred_weight'))
    activity_level = int(request.POST.get('activity_level'))
    has_children = request.POST.get('has_children') == 'on'
    has_allergy = request.POST.get('has_allergy') == 'on'
    has_other_dogs = request.POST.get('has_other_dogs') == 'on'
    has_time_for_grooming = request.POST.get('has_time_for_grooming') == 'on'
    home_type = request.POST.get('home_type')

    survey = Survey.objects.create(
            has_children=has_children,
            home_type=home_type,
            activity_level=activity_level,
            preferred_weight=preferred_weight,
            has_allergy=has_allergy,
            has_other_dogs=has_other_dogs,
            has_time_for_grooming=has_time_for_grooming
        )
    recommendations_for_survey = get_recommendations(survey)
    recommendations = Recommendation.objects.create(
        survey=survey,
        breeds_json=recommendations_for_survey
    )
    return render(request, 'main/recommendations.html', {'rec': recommendations})


def get_recommendations(survey):
    recommendations = []
    dogs = DogBreed.objects.all()
    for dog in dogs:
        score = calculate_dog_suitability(dog, survey)
        recommendations.append({'id': dog.id,
                                'score': score,
                                'name_rus': dog.name_rus,
                                'name': dog.name,
                                'avg_weight': dog.avg_weight,
                                'trainability': dog.trainability,
                                'energy': dog.energy,
                                'good_with_children': dog.good_with_children,
                                'good_with_other_dogs': dog.good_with_other_dogs,
                                'grooming': dog.grooming,
                                'photo': dog.dog_photo
                                })
    return sorted(recommendations, key=lambda x: x['score'], reverse=True)[:20]


def calculate_dog_suitability(dog, survey):
    if survey.home_type == 'apartment' and dog.avg_weight >= 40:
        return 0
    weight_score = check_dog_weight_suitability(dog, survey)
    kids_score = check_dog_with_kids_suitability(dog, survey)
    dogs_suitability = check_dog_with_dogs_suitability(dog, survey)
    allergy_suitability = check_dog_allergy_suitability(dog, survey)
    activity_suitability = check_dog_activity_level(dog, survey)
    grooming_suitability = check_dog_grooming_suitability(dog, survey)
    dog_trainability = check_dog_trainability(dog)
    total_score = weight_score + kids_score + dogs_suitability + activity_suitability + grooming_suitability + dog_trainability + allergy_suitability
    return total_score

def check_dog_weight_suitability(dog, survey):
    weight_ranges ={
        1: (0, 5),
        2: (5, 10),
        3: (10, 20),
        4: (20, 45),
        5: (45, 120)
    }
    dog_w_min, dog_w_max = weight_ranges[survey.preferred_weight]
    if dog_w_min > dog.avg_weight or dog_w_max < dog.avg_weight:
        return 0
    return 20


def check_dog_with_kids_suitability(dog, survey):
    values = {
        5: 20,
        4: 15,
        3: 10
    }
    if not survey.has_children:
        return 20
    if dog.good_with_children < 3:
        return 0
    return values[dog.good_with_children]


def check_dog_with_dogs_suitability(dog, survey):
    values = {
        5: 20,
        4: 15,
        3: 10
    }
    if not survey.has_other_dogs:
        return 20
    if dog.good_with_other_dogs < 3:
        return 0
    return values[dog.good_with_other_dogs]


def check_dog_activity_level(dog, survey):
    difference = {
        0: 10,
        1: 8,
        2: 6,
        3: 4,
        4: 2,
        5: 0
    }
    return difference[abs(dog.energy - survey.activity_level)]


def check_dog_allergy_suitability(dog, survey):
    values = {
        1: 20,
        2: 15,
        0: 0
    }
    if not survey.has_allergy:
        return 20
    if dog.shedding > 2:
        return 0
    return values[dog.shedding]


def check_dog_grooming_suitability(dog, survey):
    values = {
        1: 5,
        2: 4,
        3: 3,
        4: 2,
        5: 1,
        0: 0
    }
    if dog.grooming >= 4 and not survey.has_time_for_grooming:
        return 0
    return values[dog.grooming]


def check_dog_trainability(dog):
    values = {
        1: 5,
        2: 4,
        3: 3,
        4: 2,
        5: 1,
        0: 0
    }
    return values[dog.trainability]