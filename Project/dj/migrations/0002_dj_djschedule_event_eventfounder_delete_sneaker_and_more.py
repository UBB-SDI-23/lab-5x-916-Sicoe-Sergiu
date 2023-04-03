# Generated by Django 4.1.7 on 2023-03-28 17:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dj', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(blank=True, choices=[('Priku', 'Priku'), ('Prichindel', 'Prichindel'), ('PetreInspirescu', 'Petre Inspirescu'), ('RQZ', 'RQZ'), ('Sepp', 'Sepp'), ('NuZau', 'Nu Zau'), ('Cosmjn', 'Cosmjn'), ('Lizz', 'LIZZ'), ('DanAndrei', 'DanAndrei'), ('Cap', 'Cap'), ('Sublee', 'Sublee')], max_length=50, unique=True)),
                ('full_name', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=50)),
                ('fee', models.IntegerField()),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='DjSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('hour', models.TimeField()),
                ('set_length', models.DurationField(default=datetime.timedelta)),
                ('dj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='line_up', to='dj.dj')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=150)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('capacity', models.IntegerField()),
                ('access_fee', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='EventFounder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rating', models.FloatField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Sneaker',
        ),
        migrations.AddField(
            model_name='event',
            name='founder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='dj.eventfounder'),
        ),
        migrations.AddField(
            model_name='djschedule',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_schedule', to='dj.event'),
        ),
    ]
