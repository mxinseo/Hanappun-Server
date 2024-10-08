
# 체질별 맞는 요소와 맞지 않는 요소 정의
# body_type_preferences = {
#     '목양': {
#         'likes': ['민물생선', '오리고기', '닭고기', '토마토', '우유', '소고기', '밀가루', '고구마', '감자', '마늘'],
#         'dislikes': ['바다생선', '조개류', '갑각류', '청포도', '팥', '복분자', '보리', '메밀', '오이', '모과', '돼지고기', '시금치', '고추', '딸기', '미역']
#     },
#     '목음': {
#         'likes': ['치즈', '콩', '백미', '가지', '옥수수', '쇠고기', '돼지고기', '밀가루', '감자', '마늘'],
#         'dislikes': ['바다생선', '조개류', '청포도', '와인', '찹쌀', '생강', '오이', '복분자', '꿀', '닭고기', '현미', '보리', '고구마', '토마토']
#     },
#     '토양': {
#         'likes': ['아보카도', '갑각류', '우유', '백미', '콩', '돼지고기', '소고기', '복어'],
#         'dislikes': ['도라지', '현미', '미역', '망고', '고추', '참기름', '고구마', '토마토', '녹용', '밤', '옥수수', '시금치', '감자', '사과', '김']
#     },
#     '토음': {
#         'likes': ['딸기', '치즈', '조개류', '팥', '견과류', '돼지고기', '복어'],
#         'dislikes': ['닭고기', '오리고기', '밤', '현미', '도라지', '마늘', '토마토', '고구마', '도토리', '마', '콩', '쇠고기', '감자', '가지', '김']
#     },
#     '금양': {
#         'likes': ['굴', '갑각류', '두부', '오이', '애호박', '바다생선', '조개류', '백미', '배추', '상추'],
#         'dislikes': ['쇠고기', '닭고기', '유제품', '콩', '밀가루', '돼지고기', '치즈', '현미', '고구마', '호박', '미역', '토마토', '수박', '팥', '보리']
#     },
#     '금음': {
#         'likes': ['갑각류', '복어', '된장', '두부', '오이', '바다생선', '흰살생선', '백미', '배추', '상추'],
#         'dislikes': ['쇠고기', '바다생선', '백미', '배추', '조개류', '치즈', '현미', '고구마', '도라지', '호박', '굴', '팥', '보리', '옥수수', '깻잎']
#     },
#     '수양': {
#         'likes': ['흰살생선', '콩', '밤', '백미', '고구마', '감자', '닭고기', '오리고기', '사과'],
#         'dislikes': ['돼지고기', '복어', '팥', '보리', '알로에', '감', '참외', '붉은살생선', '조개류', '쇠고기', '유제품', '바다생선', '민물생선', '청국장']
#     },
#     '수음': {
#         'likes': ['민물생선', '버터', '콩', '밤', '백미', '된장', '쇠고기', '닭고기', '감자', '사과'],
#         'dislikes': ['청포도', '팥', '복어', '갑각류', '돼지고기', '바다생선', '조개류', '흰살생선', '메밀', '오이', '시금치', '두유', '배추', '상추', '김']
#     }
# }

# # 체질별 구성요소 점수 정의
# component_scores = {
#     '목양': {
#         '50': ['민물생선', '오리고기', '닭고기', '토마토', '우유'],
#         '30': ['소고기', '밀가루', '고구마', '감자', '마늘'],
#         '-10': ['돼지고기', '시금치', '고추', '딸기', '미역'],
#         '-30': ['복분자', '보리', '메밀', '오이', '모과'],
#         '-50': ['바다생선', '조개류', '갑각류', '청포도', '팥']
#     },
#     '목음': {
#         '50': ['치즈', '콩', '백미', '가지', '옥수수'],
#         '30': ['쇠고기', '돼지고기', '밀가루', '감자', '마늘'],
#         '-10': ['닭고기', '현미', '보리', '고구마', '토마토'],
#         '-30': ['찹쌀', '생강', '오이', '복분자', '꿀'],
#         '-50': ['바다생선', '조개류', '청포도', '와인']
#     },
#     '토양': {
#         '50': ['돼지고기', '소고기', '복어'],
#         '30': ['아보카도', '갑각류', '우유', '백미', '콩'],
#         '-10': ['옥수수', '시금치', '감자', '사과', '김'],
#         '-30': ['참기름', '고구마', '토마토', '녹용', '밤'],
#         '-50': ['도라지', '현미', '미역', '망고', '고추']
#     },
#     '토음': {
#         '50': ['돼지고기', '복어'],
#         '30': ['딸기', '치즈', '조개류', '팥', '견과류'],
#         '-10': ['콩', '쇠고기', '감자', '가지', '김'],
#         '-30': ['마늘', '토마토', '고구마', '도토리', '마'],
#         '-50': ['닭고기', '오리고기', '밤', '현미', '도라지']
#     },
#     '금양': {
#         '50': ['바다생선', '조개류', '백미', '배추', '상추'],
#         '30': ['굴', '갑각류', '두부', '오이', '애호박'],
#         '-10': ['미역', '토마토', '수박', '팥', '보리'],
#         '-30': ['돼지고기', '치즈', '현미', '고구마', '호박'],
#         '-50': ['쇠고기', '닭고기', '유제품', '콩', '밀가루']
#     },
#     '금음': {
#         '50': ['바다생선', '흰살생선', '백미', '배추', '상추'],
#         '30': ['갑각류', '복어', '된장', '두부', '오이'],
#         '-10': ['굴', '팥', '보리', '옥수수', '깻잎'],
#         '-30': ['치즈', '현미', '고구마', '도라지', '호박'],
#         '-50': ['쇠고기', '바다생선', '백미', '배추', '조개류']
#     },
#     '수양': {
#         '50': ['감자', '닭고기', '오리고기', '사과'],
#         '30': ['흰살생선', '콩', '밤', '백미', '고구마'],
#         '-10': ['쇠고기', '유제품', '바다생선', '민물생선', '청국장'],
#         '-30': ['감', '참외', '붉은살 생선', '조개류'],
#         '-50': ['돼지고기', '복어', '팥', '보리', '알로에']
#     },
#     '수음': {
#         '50': ['된장', '쇠고기', '닭고기', '감자', '사과'],
#         '30': ['민물생선', '버터', '콩', '밤', '백미'],
#         '-10': ['시금치', '두유', '배추', '상추', '김'],
#         '-30': ['바다생선', '조개류', '흰살생선', '메밀', '오이'],
#         '-50': ['청포도', '팥', '복어', '갑각류', '돼지고기']
#     }
# }

# from rest_framework import serializers
# from .models import Meal, Ingredient
# from users.models import User  # User 모델을 가져옵니다.

# class IngredientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ingredient
#         fields = ['id', 'name']


# class MealSerializer(serializers.ModelSerializer):
#     ingredients = IngredientSerializer(many=True)
#     user = serializers.CharField(source='user.constitution_8', read_only=True)  # constitution_8 필드를 사용

#     class Meta:
#         model = Meal
#         fields = ['id', 'name', 'date', 'timing', 'ingredients', 'user', 'total']

#     def create(self, validated_data):
#         ingredients_data = validated_data.pop('ingredients')
#         user = self.context['request'].user  # 요청한 사용자를 가져옵니다
#         meal = Meal.objects.create(user=user, **validated_data)

#         total_score = 0
#         for ingredient_data in ingredients_data:
#             ingredient, _ = Ingredient.objects.get_or_create(**ingredient_data)
#             meal.ingredients.add(ingredient)
#             total_score += self.calculate_score(user.constitution_8, ingredient.name)

#         meal.total = total_score
#         meal.save()
#         return meal

#     def update(self, instance, validated_data):
#         ingredients_data = validated_data.pop('ingredients')
#         user = self.context['request'].user  # 요청한 사용자를 가져옵니다

#         instance.name = validated_data.get('name', instance.name)
#         instance.date = validated_data.get('date', instance.date)
#         instance.timing = validated_data.get('timing', instance.timing)

#         instance.ingredients.clear()
#         total_score = 0
#         for ingredient_data in ingredients_data:
#             ingredient, _ = Ingredient.objects.get_or_create(**ingredient_data)
#             instance.ingredients.add(ingredient)
#             total_score += self.calculate_score(user.constitution_8, ingredient.name)

#         instance.total = total_score
#         instance.save()
#         return instance

    # def calculate_score(self, constitution_8, ingredient_name):
    #     component_scores = {
    #         '목양': {
    #             '50': ['민물생선', '오리고기', '닭고기', '토마토', '우유'],
    #             '30': ['소고기', '밀가루', '고구마', '감자', '마늘'],
    #             '-10': ['돼지고기', '시금치', '고추', '딸기', '미역'],
    #             '-30': ['복분자', '보리', '메밀', '오이', '모과'],
    #             '-50': ['바다생선', '조개류', '갑각류', '청포도', '팥']
    #             },
    #         '목음': {
    #             '50': ['치즈', '콩', '백미', '가지', '옥수수'],
    #             '30': ['쇠고기', '돼지고기', '밀가루', '감자', '마늘'],
    #             '-10': ['닭고기', '현미', '보리', '고구마', '토마토'],
    #             '-30': ['찹쌀', '생강', '오이', '복분자', '꿀'],
    #             '-50': ['바다생선', '조개류', '청포도', '와인']
    #             },
    #         '토양': {
    #             '50': ['돼지고기', '소고기', '복어'],
    #             '30': ['아보카도', '갑각류', '우유', '백미', '콩'],
    #             '-10': ['옥수수', '시금치', '감자', '사과', '김'],
    #             '-30': ['참기름', '고구마', '토마토', '녹용', '밤'],
    #             '-50': ['도라지', '현미', '미역', '망고', '고추'],
    #             },
    #         '토음': {
    #             '50': ['돼지고기', '복어'],
    #             '30': ['딸기', '치즈', '조개류', '팥', '견과류'],
    #             '-10': ['콩', '쇠고기', '감자', '가지', '김'],
    #             '-30': ['마늘', '토마토', '고구마', '도토리', '마'],
    #             '-50': ['닭고기', '오리고기', '밤', '현미', '도라지']
    #             },
    #         '금양': {
    #             '50': ['바다생선', '조개류', '백미', '배추', '상추'],
    #             '30': ['굴', '갑각류', '두부', '오이', '애호박'],
    #             '-10': ['미역', '토마토', '수박', '팥', '보리'],
    #             '-30': ['돼지고기', '치즈', '현미', '고구마', '호박'],
    #             '-50': ['쇠고기', '닭고기', '유제품', '콩', '밀가루']
    #             },
    #         '금음': {
    #             '50': ['바다생선', '흰살생선', '백미', '배추', '상추'],
    #             '30': ['갑각류', '복어', '된장', '두부', '오이'],
    #             '-10': ['굴', '팥', '보리', '옥수수', '깻잎'],
    #             '-30': ['치즈', '현미', '고구마', '도라지', '호박'],
    #             '-50': ['쇠고기', '바다생선', '백미', '배추', '조개류']
    #             },
    #         '수양': {
    #             '50': ['감자', '닭고기', '오리고기', '사과'],
    #             '30': ['흰살생선', '콩', '밤', '백미', '고구마'],
    #             '-10': ['쇠고기', '유제품', '바다생선', '민물생선', '청국장'],
    #             '-30': ['감', '참외', '붉은살 생선', '조개류'],
    #             '-50': ['돼지고기', '복어', '팥', '보리', '알로에']
    #             },
    #         '수음': {
    #             '50': ['된장', '쇠고기', '닭고기', '감자', '사과'],
    #             '30': ['민물생선', '버터', '콩', '밤', '백미'],
    #             '-10': ['시금치', '두유', '배추', '상추', '김'],
    #             '-30': ['바다생선', '조개류', '흰살생선', '메밀', '오이'],
    #             '-50': ['청포도', '팥', '복어', '갑각류', '돼지고기']
    #         }
    #         }
#         score_table = component_scores.get(constitution_8, {})
#         for score, ingredients in score_table.items():
#             if ingredient_name in ingredients:
#                 return int(score)
#         return 0

from rest_framework import serializers
from .models import Meal, Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']

class MealSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    user = serializers.CharField(source='user.username', read_only=True)  # user 필드를 읽기 전용으로 설정

    class Meta:
        model = Meal
        fields = ['id', 'name', 'date', 'timing', 'ingredients', 'user', 'total']

    def to_representation(self, instance):
        """음식을 체질에 따라 좋아하는 성분과 싫어하는 성분으로 나누기"""
        response = super().to_representation(instance)
        user_constitution = instance.user.constitution_8

        body_type_preferences = {
    '목양': {
        'likes': ['민물생선', '오리고기', '닭고기', '토마토', '우유', '소고기', '밀가루', '고구마', '감자', '마늘'],
        'dislikes': ['바다생선', '조개류', '갑각류', '청포도', '팥', '복분자', '보리', '메밀', '오이', '모과', '돼지고기', '시금치', '고추', '딸기', '미역']
    },
    '목음': {
        'likes': ['치즈', '콩', '백미', '가지', '옥수수', '쇠고기', '돼지고기', '밀가루', '감자', '마늘'],
        'dislikes': ['바다생선', '조개류', '청포도', '와인', '찹쌀', '생강', '오이', '복분자', '꿀', '닭고기', '현미', '보리', '고구마', '토마토']
    },
    '토양': {
        'likes': ['아보카도', '갑각류', '우유', '백미', '콩', '돼지고기', '소고기', '복어'],
        'dislikes': ['도라지', '현미', '미역', '망고', '고추', '참기름', '고구마', '토마토', '녹용', '밤', '옥수수', '시금치', '감자', '사과', '김']
    },
    '토음': {
        'likes': ['딸기', '치즈', '조개류', '팥', '견과류', '돼지고기', '복어'],
        'dislikes': ['닭고기', '오리고기', '밤', '현미', '도라지', '마늘', '토마토', '고구마', '도토리', '마', '콩', '쇠고기', '감자', '가지', '김']
    },
    '금양': {
        'likes': ['굴', '갑각류', '두부', '오이', '애호박', '바다생선', '조개류', '백미', '배추', '상추'],
        'dislikes': ['쇠고기', '닭고기', '유제품', '콩', '밀가루', '돼지고기', '치즈', '현미', '고구마', '호박', '미역', '토마토', '수박', '팥', '보리']
    },
    '금음': {
        'likes': ['갑각류', '복어', '된장', '두부', '오이', '바다생선', '흰살생선', '백미', '배추', '상추'],
        'dislikes': ['쇠고기', '바다생선', '백미', '배추', '조개류', '치즈', '현미', '고구마', '도라지', '호박', '굴', '팥', '보리', '옥수수', '깻잎']
    },
    '수양': {
        'likes': ['흰살생선', '콩', '밤', '백미', '고구마', '감자', '닭고기', '오리고기', '사과'],
        'dislikes': ['돼지고기', '복어', '팥', '보리', '알로에', '감', '참외', '붉은살생선', '조개류', '쇠고기', '유제품', '바다생선', '민물생선', '청국장']
    },
    '수음': {
        'likes': ['민물생선', '버터', '콩', '밤', '백미', '된장', '쇠고기', '닭고기', '감자', '사과'],
        'dislikes': ['청포도', '팥', '복어', '갑각류', '돼지고기', '바다생선', '조개류', '흰살생선', '메밀', '오이', '시금치', '두유', '배추', '상추', '김']
    }
}

        preferences = body_type_preferences.get(user_constitution, {'likes': [], 'dislikes': [], 'soso': []})

        ingredient_details = {"likes": [], "dislikes": [], 'soso': []}
        for ingredient in instance.ingredients.all():
            if ingredient.name in preferences['likes']:
                ingredient_details['likes'].append(ingredient.name)
            elif ingredient.name in preferences['dislikes']:
                ingredient_details['dislikes'].append(ingredient.name)
            else:
                ingredient_details['soso'].append(ingredient.name)

        response['ingredient_details'] = ingredient_details

        total_score = self.get_daily_total_score(instance.user, instance.date)
        response['total_daily_score'] = total_score

        if total_score < 0:
            response['score_evaluation'] = "bad"
        elif 0 <= total_score < 100:
            response['score_evaluation'] = "soso"
        else:
            response['score_evaluation'] = "good"

        return response

    def get_daily_total_score(self, user, date):
        meals = Meal.objects.filter(user=user, date=date)  # 해당 날짜의 모든 식사 조회

        total_score = 0
        meal_count = 0

        for meal in meals:
            meal_score = 0

        # 메뉴에 속한 성분들의 점수를 합산하여 메뉴의 총점 계산
            for ingredient in meal.ingredients.all():
                meal_score += self.calculate_score(user.constitution_8, ingredient.name)

        # 메뉴의 총 점수를 전체 총점에 합산
            total_score += meal_score
            meal_count += 1

    # 메뉴가 없는 경우 0점 반환
        if meal_count == 0:
            return 0

    # 모든 메뉴 점수의 평균 계산
        daily_average_score = total_score / meal_count

        return daily_average_score


    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        user = self.context['user']  # views.py에서 전달받은 user 사용
        meal = Meal.objects.create(user=user, **validated_data)

        total_score = 0
        for ingredient_data in ingredients_data:
            ingredient, _ = Ingredient.objects.get_or_create(**ingredient_data)
            meal.ingredients.add(ingredient)
            total_score += self.calculate_score(user.constitution_8, ingredient.name)

        meal.total = total_score
        meal.save()
        return meal

    def update(self, instance, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        user = self.context['user']  # views.py에서 전달받은 user 사용

        instance.name = validated_data.get('name', instance.name)
        instance.date = validated_data.get('date', instance.date)
        instance.timing = validated_data.get('timing', instance.timing)

        instance.ingredients.clear()
        total_score = 0
        for ingredient_data in ingredients_data:
            ingredient, _ = Ingredient.objects.get_or_create(**ingredient_data)
            instance.ingredients.add(ingredient)
            total_score += self.calculate_score(user.constitution_8, ingredient.name)

        instance.total = total_score
        instance.save()
        return instance
    
    def calculate_score(self, constitution_8, ingredient_name):
        component_scores = {
            '목양': {
                '50': ['민물생선', '오리고기', '닭고기', '토마토', '우유'],
                '30': ['소고기', '밀가루', '고구마', '감자', '마늘'],
                '-10': ['돼지고기', '시금치', '고추', '딸기', '미역'],
                '-30': ['복분자', '보리', '메밀', '오이', '모과'],
                '-50': ['바다생선', '조개류', '갑각류', '청포도', '팥']
                },
            '목음': {
                '50': ['치즈', '콩', '백미', '가지', '옥수수'],
                '30': ['쇠고기', '돼지고기', '밀가루', '감자', '마늘'],
                '-10': ['닭고기', '현미', '보리', '고구마', '토마토'],
                '-30': ['찹쌀', '생강', '오이', '복분자', '꿀'],
                '-50': ['바다생선', '조개류', '청포도', '와인']
                },
            '토양': {
                '50': ['돼지고기', '소고기', '복어'],
                '30': ['아보카도', '갑각류', '우유', '백미', '콩'],
                '-10': ['옥수수', '시금치', '감자', '사과', '김'],
                '-30': ['참기름', '고구마', '토마토', '녹용', '밤'],
                '-50': ['도라지', '현미', '미역', '망고', '고추'],
                },
            '토음': {
                '50': ['돼지고기', '복어'],
                '30': ['딸기', '치즈', '조개류', '팥', '견과류'],
                '-10': ['콩', '쇠고기', '감자', '가지', '김'],
                '-30': ['마늘', '토마토', '고구마', '도토리', '마'],
                '-50': ['닭고기', '오리고기', '밤', '현미', '도라지']
                },
            '금양': {
                '50': ['바다생선', '조개류', '백미', '배추', '상추'],
                '30': ['굴', '갑각류', '두부', '오이', '애호박'],
                '-10': ['미역', '토마토', '수박', '팥', '보리'],
                '-30': ['돼지고기', '치즈', '현미', '고구마', '호박'],
                '-50': ['쇠고기', '닭고기', '유제품', '콩', '밀가루']
                },
            '금음': {
                '50': ['바다생선', '흰살생선', '백미', '배추', '상추'],
                '30': ['갑각류', '복어', '된장', '두부', '오이'],
                '-10': ['굴', '팥', '보리', '옥수수', '깻잎'],
                '-30': ['치즈', '현미', '고구마', '도라지', '호박'],
                '-50': ['쇠고기', '바다생선', '백미', '배추', '조개류']
                },
            '수양': {
                '50': ['감자', '닭고기', '오리고기', '사과'],
                '30': ['흰살생선', '콩', '밤', '백미', '고구마'],
                '-10': ['쇠고기', '유제품', '바다생선', '민물생선', '청국장'],
                '-30': ['감', '참외', '붉은살 생선', '조개류'],
                '-50': ['돼지고기', '복어', '팥', '보리', '알로에']
                },
            '수음': {
                '50': ['된장', '쇠고기', '닭고기', '감자', '사과'],
                '30': ['민물생선', '버터', '콩', '밤', '백미'],
                '-10': ['시금치', '두유', '배추', '상추', '김'],
                '-30': ['바다생선', '조개류', '흰살생선', '메밀', '오이'],
                '-50': ['청포도', '팥', '복어', '갑각류', '돼지고기']
            }
        }

        score_table = component_scores.get(constitution_8, {})
        for score, ingredients in score_table.items():
            if ingredient_name in ingredients:
                return int(score)
        return 0




    # def calculate_score(self, constitution_8, ingredient_name):
        # component_scores = {
        #     '목양': {
        #         '50': ['민물생선', '오리고기', '닭고기', '토마토', '우유'],
        #         '30': ['소고기', '밀가루', '고구마', '감자', '마늘'],
        #         '-10': ['돼지고기', '시금치', '고추', '딸기', '미역'],
        #         '-30': ['복분자', '보리', '메밀', '오이', '모과'],
        #         '-50': ['바다생선', '조개류', '갑각류', '청포도', '팥']
        #         },
        #     '목음': {
        #         '50': ['치즈', '콩', '백미', '가지', '옥수수'],
        #         '30': ['쇠고기', '돼지고기', '밀가루', '감자', '마늘'],
        #         '-10': ['닭고기', '현미', '보리', '고구마', '토마토'],
        #         '-30': ['찹쌀', '생강', '오이', '복분자', '꿀'],
        #         '-50': ['바다생선', '조개류', '청포도', '와인']
        #         },
        #     '토양': {
        #         '50': ['돼지고기', '소고기', '복어'],
        #         '30': ['아보카도', '갑각류', '우유', '백미', '콩'],
        #         '-10': ['옥수수', '시금치', '감자', '사과', '김'],
        #         '-30': ['참기름', '고구마', '토마토', '녹용', '밤'],
        #         '-50': ['도라지', '현미', '미역', '망고', '고추'],
        #         },
        #     '토음': {
        #         '50': ['돼지고기', '복어'],
        #         '30': ['딸기', '치즈', '조개류', '팥', '견과류'],
        #         '-10': ['콩', '쇠고기', '감자', '가지', '김'],
        #         '-30': ['마늘', '토마토', '고구마', '도토리', '마'],
        #         '-50': ['닭고기', '오리고기', '밤', '현미', '도라지']
        #         },
        #     '금양': {
        #         '50': ['바다생선', '조개류', '백미', '배추', '상추'],
        #         '30': ['굴', '갑각류', '두부', '오이', '애호박'],
        #         '-10': ['미역', '토마토', '수박', '팥', '보리'],
        #         '-30': ['돼지고기', '치즈', '현미', '고구마', '호박'],
        #         '-50': ['쇠고기', '닭고기', '유제품', '콩', '밀가루']
        #         },
        #     '금음': {
        #         '50': ['바다생선', '흰살생선', '백미', '배추', '상추'],
        #         '30': ['갑각류', '복어', '된장', '두부', '오이'],
        #         '-10': ['굴', '팥', '보리', '옥수수', '깻잎'],
        #         '-30': ['치즈', '현미', '고구마', '도라지', '호박'],
        #         '-50': ['쇠고기', '바다생선', '백미', '배추', '조개류']
        #         },
        #     '수양': {
        #         '50': ['감자', '닭고기', '오리고기', '사과'],
        #         '30': ['흰살생선', '콩', '밤', '백미', '고구마'],
        #         '-10': ['쇠고기', '유제품', '바다생선', '민물생선', '청국장'],
        #         '-30': ['감', '참외', '붉은살 생선', '조개류'],
        #         '-50': ['돼지고기', '복어', '팥', '보리', '알로에']
        #         },
        #     '수음': {
        #         '50': ['된장', '쇠고기', '닭고기', '감자', '사과'],
        #         '30': ['민물생선', '버터', '콩', '밤', '백미'],
        #         '-10': ['시금치', '두유', '배추', '상추', '김'],
        #         '-30': ['바다생선', '조개류', '흰살생선', '메밀', '오이'],
        #         '-50': ['청포도', '팥', '복어', '갑각류', '돼지고기']
        #     }
        #     }

    #     score_table = component_scores.get(constitution_8, {})
    #     for score, ingredients in score_table.items():
    #         if ingredient_name in ingredients:
    #             return int(score)
    #     return 0
