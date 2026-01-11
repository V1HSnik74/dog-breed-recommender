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


