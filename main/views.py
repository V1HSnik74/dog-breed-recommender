from django.shortcuts import render
from .models import DogBreed, Recommendation
from .forms import SurveyForm


WEIGHT_RANGES = {1: (0, 5), 2: (5, 10), 3: (10, 20), 4: (20, 45), 5: (45, 120)}
WEIGHT_SCORES = {0: 18, 1: 14, 2: 10, 3: 6, 4: 2, 5: 0}
KIDS_DOGS_SCORES = {5: 20, 4: 15, 3: 10}
ACTIVITY_SCORES =  {0: 10, 1: 8, 2: 6, 3: 4, 4: 2, 5: 0}
ALLERGY_SCORES = {1: 20, 2: 15, 0: 0}
GROOMING_TRAINABILITY_SCORES =  {1: 5, 2: 4, 3: 3, 4: 2, 5: 1, 0: 0}


def index(request):
    form = SurveyForm()
    return render(request, 'main/surveyform.html', {'form': form})


def get_survey_result(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            survey = form.save()
            recommendations_for_survey = get_recommendations(survey)
            recommendations = Recommendation.objects.create(
                survey=survey,
                breeds_json=recommendations_for_survey
            )
            return render(request, 'main/recommendations.html', {'rec': recommendations})
    form = SurveyForm()
    return render(request, 'main/surveyform.html', {'form': form})


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
    activity_suitability = ACTIVITY_SCORES[abs(dog.energy - survey.activity_level)]
    grooming_suitability = check_dog_grooming_suitability(dog, survey)
    dog_trainability = GROOMING_TRAINABILITY_SCORES[dog.trainability]
    total_score = weight_score + kids_score + dogs_suitability + activity_suitability + grooming_suitability + dog_trainability + allergy_suitability
    return total_score


def check_dog_weight_suitability(dog, survey):
    dog_w_min, dog_w_max = WEIGHT_RANGES[survey.preferred_weight]
    if dog_w_min <= dog.avg_weight <= dog_w_max:
        return 20
    if dog.avg_weight <  dog_w_min:
        dist = dog_w_min - dog.avg_weight
    else:
        dist = dog.avg_weight - dog_w_max
    return WEIGHT_SCORES[min(dist//5, 5)]


def check_dog_with_kids_suitability(dog, survey):
    if not survey.has_children:
        return 20
    if dog.good_with_children < 3:
        return 0
    return KIDS_DOGS_SCORES[dog.good_with_children]


def check_dog_with_dogs_suitability(dog, survey):
    if not survey.has_other_dogs:
        return 20
    if dog.good_with_other_dogs < 3:
        return 0
    return KIDS_DOGS_SCORES[dog.good_with_other_dogs]


def check_dog_allergy_suitability(dog, survey):
    if not survey.has_allergy:
        return 20
    if dog.shedding > 2:
        return 0
    return ALLERGY_SCORES[dog.shedding]


def check_dog_grooming_suitability(dog, survey):
    if dog.grooming >= 4 and not survey.has_time_for_grooming:
        return 0
    return GROOMING_TRAINABILITY_SCORES[dog.grooming]
