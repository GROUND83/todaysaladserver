from django.db import models
from cores import models as core_models
from ingredients import models as ingredeint_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class SaladType(AbstractItem):
    class Meta:
        verbose_name = "샐러드 타입"
        verbose_name_plural = "샐러드 타입 모음"

    def __str__(self):

        return self.name


class Salad(core_models.TimeStampedModel):
    class Meta:
        verbose_name = "샐러드"
        verbose_name_plural = "샐러드 모음"

    name = models.CharField(max_length=140, null=True, verbose_name="샐러드명", unique=True)
    description = models.TextField(null=True, verbose_name="샐러드설명", blank=True)
    salad_type = models.ManyToManyField(SaladType, blank=True, verbose_name="샐러드타입")
    ingredients = models.ManyToManyField(
        "ingredients.Ingredient", related_name="salads", blank=True, verbose_name="재료",
    )
    # 칼로기 계산할것
    calory = models.DecimalField(
        decimal_places=2, max_digits=10, default=0, verbose_name="전체칼로리"
    )
    totalsugars = models.DecimalField(
        decimal_places=2, max_digits=10, default=0, verbose_name="총당류"
    )
    totalfat = models.DecimalField(
        decimal_places=2, max_digits=10, default=0, verbose_name="총지방"
    )
    totalcarbohydrate = models.DecimalField(
        decimal_places=2, max_digits=10, default=0, verbose_name="총탄수화물"
    )
    totalprotein = models.DecimalField(
        decimal_places=2, max_digits=10, default=0, verbose_name="총단백질"
    )
    totalcholesterol = models.DecimalField(
        decimal_places=2, max_digits=10, default=0, verbose_name="총콜레스테롤"
    )
    totalsalt = models.DecimalField(
        decimal_places=2, max_digits=10, default=0, verbose_name="총나트륨"
    )
    totalpotassium = models.DecimalField(
        decimal_places=2, max_digits=10, default=0, verbose_name="총칼륨"
    )
    totaldietaryfiber = models.DecimalField(
        decimal_places=2, max_digits=10, default=0, verbose_name="총식이섬유"
    )
    price = models.IntegerField(default=8000, verbose_name="가격")
    unit = models.DecimalField(
        decimal_places=2, max_digits=10, default=1, verbose_name="총중량"
    )
    amount = models.IntegerField(default=1, verbose_name="주문수량")
    instant_order = models.BooleanField(default=True, verbose_name="주문가능")
    photo = models.ImageField(blank=True, upload_to="salads_photos")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            super().save(*args, **kwargs)
        all_calories = 0
        all_units = 0
        all_sugars = 0
        all_fat = 0
        all_carbohydrate = 0
        all_protein = 0
        all_cholesterol = 0
        all_salt = 0
        all_potassium = 0
        all_dietaryfiber = 0
        for ingredient in self.ingredients.all():
            all_calories += ingredient.weightForCalory
            all_units += ingredient.baseunit
            all_sugars += ingredient.weightForSugars
            all_fat += ingredient.weightForFat
            all_carbohydrate += ingredient.weightForCarbohydrate
            all_protein += ingredient.weightForProtein
            all_cholesterol += ingredient.weightForCholesterol
            all_salt += ingredient.weightForSalt
            all_potassium += ingredient.weightForPotassium
            all_dietaryfiber += ingredient.weightForDietaryfiber
        self.calory = all_calories
        self.unit = all_units
        self.totalsugars = all_sugars
        self.totalfat = all_fat
        self.totalcarbohydrate = all_carbohydrate
        self.totalprotein = all_protein
        self.totalcholesterol = all_cholesterol
        self.totalsalt = all_salt
        self.totalpotassium = all_potassium
        self.totaldietaryfiber = all_dietaryfiber
        print(self.calory)
        super(Salad, self).save(*args, **kwargs)  # Call the "real" save() method.

    # def first_photo(self):
    #     try:
    #         photo = self.photos.all()[:1]
    #         return photo.file.url
    #     except ValueError:
    #         return None


# class Photo(core_models.TimeStampedModel):

#     """ Photo Model Definition """

#     class Meta:
#         verbose_name = "샐러드사진"
#         verbose_name_plural = "샐러드사진모음"

#     caption = models.CharField(max_length=80, verbose_name="사진이름")
#     file = models.ImageField(upload_to="salads_photos")
#     salad = models.ForeignKey(
#         Salad, related_name="photos", on_delete=models.CASCADE, null=True
#     )

#     def __str__(self):
#         return self.caption
