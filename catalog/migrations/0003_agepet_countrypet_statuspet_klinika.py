# Generated by Django 4.2.5 on 2023-09-26 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_actor_born_alter_actor_country_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgePet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=20, verbose_name='Возраст')),
            ],
        ),
        migrations.CreateModel(
            name='Countrypet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя')),
            ],
        ),
        migrations.CreateModel(
            name='Statuspet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('молодой', 'молодой'), ('юный', 'юный'), ('пожилой', 'пожилой')], max_length=20, verbose_name='Статус')),
            ],
        ),
        migrations.CreateModel(
            name='Klinika',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Название')),
                ('problemsummary', models.TextField(max_length=500, verbose_name='Проблема')),
                ('agepet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.agepet', verbose_name='Возраст')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.countrypet', verbose_name='Страна')),
                ('status', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='catalog.statuspet', verbose_name='Статус')),
            ],
        ),
    ]