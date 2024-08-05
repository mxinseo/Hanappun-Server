# Generated by Django 5.0.7 on 2024-08-06 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0003_alter_meal_overall_status_alter_meal_total_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='bad_foods',
        ),
        migrations.RemoveField(
            model_name='meal',
            name='good_foods',
        ),
        migrations.AddField(
            model_name='meal',
            name='dinner_bad_foods',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='meal',
            name='dinner_good_foods',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='meal',
            name='lunch_bad_foods',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='meal',
            name='lunch_good_foods',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='meal',
            name='morning_bad_foods',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='meal',
            name='morning_good_foods',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='meal',
            name='snack_bad_foods',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='meal',
            name='snack_good_foods',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='meal',
            name='overall_status',
            field=models.CharField(default='soso', max_length=20),
        ),
        migrations.AlterField(
            model_name='meal',
            name='total_score',
            field=models.IntegerField(default=0),
        ),
    ]
