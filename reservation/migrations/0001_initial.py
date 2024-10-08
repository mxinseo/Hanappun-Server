# Generated by Django 5.0.7 on 2024-09-22 20:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clinic', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='예약일정')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='환자 아이디')),
                ('clinic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clinic.clinic', verbose_name='한의원')),
            ],
        ),
    ]
