# Generated by Django 5.0.7 on 2024-08-05 20:37

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
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='리뷰 내용')),
                ('rate', models.IntegerField(verbose_name='별점')),
                ('is_selected_Facility', models.BooleanField(verbose_name='시설이 쾌적해요')),
                ('is_selected_Prescription', models.BooleanField(verbose_name='약 처방이 잘 맞아요')),
                ('is_selected_Health', models.BooleanField(verbose_name='건강 관리에 철저해요')),
                ('is_selected_Kindness', models.BooleanField(verbose_name='의료진, 직원이 친절해요')),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.clinic', verbose_name='한의원')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
        ),
    ]
