from django import forms
from .models import Survey


WEIGHT_CHOICES = [
    (1, 'Очень маленькая (до 5 кг)'), (2, 'Маленькая (5-10 кг)'),
    (3, 'Средняя (10-20 кг)'), (4, 'Крупная (20-45 кг)'),
    (5, 'Очень крупная (45-120 кг)')
]
ACTIVITY_CHOICES = [
    (1, 'Очень низкая'), (2, 'Низкая'), (3, 'Средняя'), (4, 'Высокая'), (5, 'Очень высокая')
]
HOME_CHOICES = [('house', 'Дом'), ('apartment', 'Квартира')]


class SurveyForm(forms.ModelForm):
    preferred_weight = forms.ChoiceField(choices=WEIGHT_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}))
    activity_level = forms.ChoiceField(choices=ACTIVITY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}))
    home_type = forms.ChoiceField(choices=HOME_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select form-select-home'}))

    class Meta:
        model = Survey
        fields = ['preferred_weight','activity_level', 'has_children', 'has_allergy', 'has_other_dogs',
                  'has_time_for_grooming', 'home_type']
        widgets = {
            'has_children': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_allergy': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_other_dogs': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_time_for_grooming': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def clean(self):
        return super().clean()