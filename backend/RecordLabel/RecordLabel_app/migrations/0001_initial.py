# Generated by Django 4.2 on 2023-04-27 08:17

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
            ],
        ),
        migrations.CreateModel(
            name='EventFounder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=150)),
                ('start_date', models.DateField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.date(2023, 4, 27))])),
                ('end_date', models.DateField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.date(2023, 4, 27))])),
                ('capacity', models.IntegerField()),
                ('access_fee', models.FloatField()),
                ('founder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='RecordLabel_app.eventfounder')),
            ],
        ),
        migrations.CreateModel(
            name='DjSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.date(2023, 4, 27))])),
                ('hour', models.TimeField()),
                ('set_length', models.DurationField(default=datetime.timedelta)),
                ('dj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='line_up', to='RecordLabel_app.dj')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_schedule', to='RecordLabel_app.event')),
            ],
        ),
    ]
