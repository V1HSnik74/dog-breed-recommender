from django.contrib import admin

# Register your models here.
from .models import DogBreed, Survey
admin.site.register(DogBreed)
admin.site.register(Survey)