from django.db import models
from cores import models as core_models


class Ingredient(core_models.TimeStampedModel):
    class Meta:
        verbose_name = "재료"
        verbose_name_plural = "재료 모음"
        ordering = ["ingredient_type"]

    TYPE_BASE = "01base"
    TYPE_SUBBASE = "02otherbase"
    TYPE_FRUIT = "03fruit"
    TYPE_TOPPING = "04topping"
    TYPE_CHEESE = "05cheese"
    TYPE_PREMIUM = "06premium"
    TYPE_DRESSING = "07dressing"
    TYPE_CHOICES = (
        (TYPE_BASE, "01base"),
        (TYPE_SUBBASE, "02otherbase"),
        (TYPE_FRUIT, "03fruit"),
        (TYPE_TOPPING, "04topping"),
        (TYPE_CHEESE, "05cheese"),
        (TYPE_PREMIUM, "06premium"),
        (TYPE_DRESSING, "07dressing"),
    )

    ingredient_type = models.CharField(
        choices=TYPE_CHOICES,
        default=TYPE_BASE,
        blank=True,
        max_length=40,
        verbose_name="재료타입",
    )
    name = models.CharField(max_length=140, null=True, verbose_name="재료이름", unique=True)
    calory = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        default=30,
        verbose_name="칼로리(cal)",
        help_text="100g당",
    )
    sugars = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        default=0,
        verbose_name="당류(g)",
        help_text="당류",
        null=True,
    )
    fat = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        default=0,
        verbose_name="지방(g)",
        help_text="지방",
        null=True,
    )
    carbohydrate = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        default=0,
        verbose_name="단수화물(g)",
        help_text="단수화물",
        blank=True,
    )
    protein = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        default=0,
        verbose_name="단백질(g)",
        help_text="단백질",
        blank=True,
    )
    cholesterol = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        default=0,
        verbose_name="콜레스테롤(mg)",
        help_text="콜레스테롤",
        null=True,
    )
    salt = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        default=0,
        verbose_name="나트륨(mg)",
        help_text="나트륨",
        null=True,
    )
    potassium = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        default=0,
        verbose_name="칼륨(mg)",
        help_text="칼륨",
        null=True,
    )
    dietaryfiber = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        default=30,
        verbose_name="식이섬유(g)",
        help_text="식이섬유",
        null=True,
    )
    weightForCalory = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        default=0,
        verbose_name="적용칼로리(cal)",
        help_text="[자동계산,입력X]",
    )
    weightForSugars = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        default=0,
        verbose_name="적용당류(g)",
        help_text="중량적용칼로리[자동계산,입력X]",
    )
    weightForFat = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        default=0,
        verbose_name="적용지방(g)",
        help_text="중량적용칼로리[자동계산,입력X]",
    )
    weightForCarbohydrate = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        default=0,
        verbose_name="적용탄수화물(g)",
        help_text="[자동계산,입력X]",
    )
    weightForProtein = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        default=0,
        verbose_name="적용단백질(g)",
        help_text="[자동계산,입력X]",
    )
    weightForCholesterol = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        default=0,
        verbose_name="적용콜레스테롤(g)",
        help_text="[자동계산,입력X]",
    )
    weightForSalt = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        default=0,
        verbose_name="적용나트륨(g)",
        help_text="[자동계산,입력X]",
    )
    weightForPotassium = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        default=0,
        verbose_name="적욜칼륨(g)",
        help_text="[자동계산,입력X]",
    )
    weightForDietaryfiber = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        default=0,
        verbose_name="적용식이섬유(g)",
        help_text="[자동계산,입력X]",
    )

    baseprice = models.IntegerField(default=1000, verbose_name="기본가격")
    description = models.TextField(
        null=True,
        default="양상추는 샐러드로 많이 이용된다. 내용물로는 수분이 전체의 94∼95%를 차지하고, 그 밖에 탄수화물·조단백질·조섬유·비타민C 등이 들어 있다.",
        verbose_name="재료설명",
    )
    baseunit = models.DecimalField(
        decimal_places=2, max_digits=10, default=30, verbose_name="기본중량(g)"
    )
    amount = models.IntegerField(default=1, verbose_name="기본수량")
    instant_order = models.BooleanField(default=True, verbose_name="주문가능")
    photo = models.ImageField(blank=True, upload_to="ingredients_photos")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id:
            super().save(*args, **kwargs)
        new_calory = 0
        new_sugars = 0.0
        new_fat = 0.0
        new_carbohydrate = 0.0
        new_protein = 0.0
        new_cholesterol = 0.0
        new_salt = 0.0
        new_potassium = 0.0
        new_dietaryfiber = 0.0

        new_calory = (self.baseunit * self.calory) / 100
        new_sugars = (self.baseunit * self.sugars) / 100
        new_fat = (self.baseunit * self.fat) / 100
        new_carbohydrate = (self.baseunit * self.carbohydrate) / 100
        new_protein = (self.baseunit * self.protein) / 100
        new_cholesterol = (self.baseunit * self.cholesterol) / 100
        new_salt = (self.baseunit * self.salt) / 100
        new_potassium = (self.baseunit * self.potassium) / 100
        new_dietaryfiber = (self.baseunit * self.dietaryfiber) / 100

        self.weightForCalory = new_calory
        self.weightForSugars = new_sugars
        self.weightForFat = new_fat
        self.weightForCarbohydrate = new_carbohydrate
        self.weightForProtein = new_protein
        self.weightForCholesterol = new_cholesterol
        self.weightForSalt = new_salt
        self.weightForPotassium = new_potassium
        self.weightForDietaryfiber = new_dietaryfiber
        print(self.weightForCalory)
        super(Ingredient, self).save(*args, **kwargs)


class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """

    class Meta:
        verbose_name = "재료 사진"
        verbose_name_plural = "재료 사진 모음"

    caption = models.CharField(max_length=80, verbose_name="사진이름")
    file = models.ImageField(upload_to="ingredient_photos")
    ingredient = models.ForeignKey(
        "Ingredient", related_name="photos", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.caption
