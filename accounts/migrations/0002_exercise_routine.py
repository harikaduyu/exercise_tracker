# Generated by Django 3.1.4 on 2021-02-06 12:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Biceps', 'Biceps'), ('Triceps', 'Triceps'), ('Chest', 'Chest'), ('Shoulders', 'Shoulders'), ('Hips', 'Hips'), ('Legs', 'Leg'), ('Running', 'Running'), ('Walking', 'Walking')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.DurationField(default=datetime.timedelta(seconds=1500))),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.account')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.exercise')),
            ],
        ),
    ]
