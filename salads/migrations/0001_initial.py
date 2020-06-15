# Generated by Django 2.2.5 on 2020-06-15 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaladType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'verbose_name': '샐러드 타입',
                'verbose_name_plural': '샐러드 타입 모음',
            },
        ),
        migrations.CreateModel(
            name='Salad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=140, null=True, unique=True, verbose_name='샐러드명')),
                ('description', models.TextField(blank=True, null=True, verbose_name='샐러드설명')),
                ('calory', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='전체칼로리')),
                ('totalsugars', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='총당류')),
                ('totalfat', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='총지방')),
                ('totalcarbohydrate', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='총탄수화물')),
                ('totalprotein', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='총단백질')),
                ('totalcholesterol', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='총콜레스테롤')),
                ('totalsalt', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='총나트륨')),
                ('totalpotassium', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='총칼륨')),
                ('totaldietaryfiber', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='총식이섬유')),
                ('price', models.IntegerField(default=8000, verbose_name='가격')),
                ('unit', models.DecimalField(decimal_places=2, default=1, max_digits=10, verbose_name='총중량')),
                ('amount', models.IntegerField(default=1, verbose_name='주문수량')),
                ('instant_order', models.BooleanField(default=True, verbose_name='주문가능')),
                ('photo', models.ImageField(blank=True, upload_to='salads_photos')),
                ('ingredients', models.ManyToManyField(blank=True, related_name='salads', to='ingredients.Ingredient', verbose_name='재료')),
                ('salad_type', models.ManyToManyField(blank=True, to='salads.SaladType', verbose_name='샐러드타입')),
            ],
            options={
                'verbose_name': '샐러드',
                'verbose_name_plural': '샐러드 모음',
            },
        ),
    ]
