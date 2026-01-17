from django.contrib import admin

# Register your models here.
from .models import DogBreed, Survey, Recommendation


@admin.register(DogBreed)
class DogBreedAdmin(admin.ModelAdmin):
    list_display = ['name_rus', 'name', 'avg_weight', 'energy', 'good_with_children',
                    'shedding', 'grooming']
    search_fields = ['name_rus', 'name']

@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ['id', 'activity_level', 'preferred_weight', 'has_children',
                    'home_type', 'has_allergy', 'has_other_dogs']
    search_fields = ['id']

@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_display = ['id', 'survey']
    search_fields = ['id']