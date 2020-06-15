# Generated by Django 2.2.5 on 2020-06-15 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fruitboxes', '0001_initial'),
        ('salads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('merchant_uid', models.CharField(blank=True, max_length=30, verbose_name='mid')),
                ('saladAmount', models.IntegerField(blank=True, null=True, verbose_name='샐러드수량')),
                ('fruitAmount', models.IntegerField(blank=True, null=True, verbose_name='과일박스수량')),
                ('orderType', models.CharField(blank=True, max_length=30, verbose_name='오더타입')),
                ('deliveryDate', models.DateField(blank=True, null=True, verbose_name='배송일')),
                ('user', models.CharField(blank=True, max_length=30, verbose_name='주문자')),
                ('address', models.CharField(blank=True, max_length=30, verbose_name='주소')),
                ('address1', models.CharField(blank=True, max_length=30, verbose_name='주소1')),
                ('etc', models.CharField(blank=True, max_length=30, verbose_name='현관')),
                ('tel', models.CharField(blank=True, max_length=30, verbose_name='전화번호')),
                ('number', models.CharField(blank=True, max_length=30, verbose_name='오더횟수')),
                ('fruit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fruitboxes.Fruitbox', verbose_name='과일박스')),
                ('salad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='salads.Salad', verbose_name='샐러드')),
            ],
            options={
                'verbose_name': '주문',
                'verbose_name_plural': '주문',
                'ordering': ['-created'],
            },
        ),
    ]
