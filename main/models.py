from django.db import models


class DogBreed(models.Model):
    name = models.CharField(max_length=50)
    min_weight = models.IntegerField()
    max_weight = models.IntegerField()
    shedding = models.IntegerField(choices=[
        (1, 'Не линяет'),
        (2, 'Слабо линяет'),
        (3, 'Умеренно линяет'),
        (4, 'Сильно линяет'),
        (5, 'Очень сильно линяет')
    ])
    grooming = models.IntegerField(choices=[
        (1, 'Не требует ухода'),
        (2, 'Требует небольшого ухода'),
        (3, 'Требует умеренного ухода'),
        (4, 'Требует тщательного ухода'),
        (5, 'Требует очень тщательного ухода')
    ])
    coat_length = models.IntegerField(choices=[
        (1, 'Нет шерсти'),
        (2, 'Короткошерстный'),
        (3, 'Шерсть средней длины'),
        (4, 'Длинношерстный'),
        (5, 'Очень длинношерстный')
    ])
    energy = models.IntegerField(choices=[
        (1, 'Не энергичная'),
        (2, 'Немного энергичная'),
        (3, 'Умеренно энергичная'),
        (4, 'Сильно энергичная'),
        (5, 'Очень сильно энергичная')
    ])
    trainability = models.IntegerField(choices=[
        (1, 'Очень плохо поддается дрессировке'),
        (2, 'Плохо поддается дрессировке'),
        (3, 'Средне поддается дрессировке'),
        (4, 'Хорошо поддается дрессировке'),
        (5, 'Очень хорошо поддается дрессировке')
    ])
    good_with_children = models.IntegerField(choices=[
        (1, 'Очень плохо ладит с детьми'),
        (2, 'Плохо ладит с детьми'),
        (3, 'Нормально ладит с детьми'),
        (4, 'Хорошо ладит с детьми'),
        (5, 'Очень хорошо ладит с детьми')
    ])
    good_with_other_dogs = models.IntegerField(choices=[
        (1, 'Очень плохо ладит с другими собаками'),
        (2, 'Плохо ладит с другими собаками'),
        (3, 'Нормально ладит с другими собаками'),
        (4, 'Хорошо ладит с другими собаками'),
        (5, 'Очень хорошо ладит с другими собаками')
    ])

    def __str__(self):
        return self.name

    @property
    def avg_weight(self):
        return (self.max_weight + self.min_weight) // 2


class Survey(models.Model):
    HOME = [('apartment', 'квартира'), ('house', 'дом')]
    has_children = models.BooleanField(verbose_name='Есть дети')
    home_type = models.CharField(verbose_name='Тип жилья', max_length=9, choices=HOME)
    activity_level = models.IntegerField(choices=[
        (1, 'Очень низкая'),
        (2, 'Низкая'),
        (3, 'Средняя'),
        (4, 'Высокая'),
        (5, 'Очень высокая'),
    ],
    default=3)
    preferred_weight = models.IntegerField(choices=[
        (1, 'Очень маленькая (до 5 кг)'),
        (2, 'Маленькая (5-10 кг)'),
        (3, 'Средняя (10-20 кг)'),
        (4, 'Крупная (20-45 кг)'),
        (5, 'Очень крупная (45-120 кг)')
    ],
    default=3)
    has_allergy = models.BooleanField(verbose_name='Наличие аллергии на собак')
    has_other_dogs = models.BooleanField(verbose_name='Наличие других собак')
    has_time_for_grooming = models.BooleanField(verbose_name='Есть время на грумминг')

    def __str__(self):
        return f'Анкета №{self.id}'