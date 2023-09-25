from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=20, verbose_name='Жанр')

    def __str__(self):
        return self.name

class Director(models.Model):
    fname = models.CharField(max_length=20, verbose_name='Имя')
    lname = models.CharField(max_length=20, verbose_name='Фамилия')

    def __str__(self):
        return f'{self.fname}, {self.lname}'

class Actor(models.Model):
    fname = models.CharField(max_length=20, verbose_name='Имя')
    lname = models.CharField(max_length=20, verbose_name='Фамилия')
    born = models.DateField(verbose_name='Дата Рождения', blank=True, null=True)
    country = models.CharField(max_length=20, verbose_name='Страна рождения', blank=True, null=True)

    def __str__(self):
        return self.lname

class Status(models.Model):
    VIBOR = (('бесплатно','бесплатно'),('базовая','базовая'),('супер','супер'))
    name = models.CharField(max_length=20, choices=VIBOR, verbose_name='Подписка')

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=20, verbose_name='Страна')

    def __str__(self):
        return self.name


class AgeRate(models.Model):
    choise = (('G', 'G'), ('PG', 'PG'), ('PG-13', 'PG-13'), ('R', 'R'), ('NC-17', 'NC-17'))
    rate = models.CharField(max_length=20, choices=choise, verbose_name='Возраст')

    def __str__(self):
        return self.rate

class Kino(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')
    genre = models.ForeignKey(Genre, on_delete=models.SET_DEFAULT, default=1, verbose_name='Жанр')
    rating = models.FloatField(verbose_name='Реётинг')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, verbose_name='Страна')
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, null=True, verbose_name='Директор')
    summary = models.TextField(max_length=500, verbose_name='Описание')
    year = models.IntegerField(verbose_name='Год')
    ager = models.ForeignKey(AgeRate, on_delete=models.SET_NULL, null=True, verbose_name='Возраст')
    actor = models.ManyToManyField(Actor, verbose_name='Актёр')
    status = models.ForeignKey(Status, on_delete=models.SET_DEFAULT, default=1, verbose_name='Подписка')

    def __str__(self):
        return self.title

    def display_actors(self):
        res = ''
        for a in self.actor.all():
            res += a.lname+' '
        return res
    display_actors.short_description = 'Актёры'