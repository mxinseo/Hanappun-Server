from django.db import models
from users.models import User
from clinic.models import Clinic

# Create your models here.

# minseo : 리뷰 모델
class Review(models.Model):
    reviewer = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='작성자')
    content = models.TextField(verbose_name='리뷰 내용')
    clinic = models.ForeignKey(to=Clinic, on_delete=models.CASCADE, verbose_name='한의원')
    rate = models.IntegerField(verbose_name='별점')

    CATEGORY_CHOICES = [
        ('Facility', '시설이 쾌적해요'),
        ('Prescription', '약 처방이 잘 맞아요'),
        ('Health', '건강 관리에 철저해요'),
        ('Kindness', '의료진, 직원이 친절해요'),
    ]

    review_cate = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=True)
