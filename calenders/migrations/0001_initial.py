# Generated by Django 2.2.5 on 2020-06-15 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fruitboxes', '0001_initial'),
        ('easyfoods', '0001_initial'),
        ('salads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('day', models.DateField(blank=True, help_text='샐러드 일자를 입력하세요.', null=True, unique=True, verbose_name='일자')),
                ('isHoliday', models.BooleanField(default=True, help_text='자동계산 입력하지 마세요.', verbose_name='공휴일여부')),
                ('holiday', models.CharField(blank=True, max_length=30, null=True, verbose_name='공휴일')),
                ('month', models.CharField(blank=True, help_text='자동계산 입력하지 마세요.', max_length=100, null=True, verbose_name='월')),
                ('year', models.CharField(blank=True, help_text='자동계산 입력하지 마세요.', max_length=100, null=True, verbose_name='년')),
                ('date', models.CharField(blank=True, help_text='자동계산 입력하지 마세요.', max_length=100, null=True, verbose_name='일')),
                ('dayofweek', models.CharField(blank=True, help_text='자동계산 입력하지 마세요.', max_length=100, null=True, verbose_name='요일')),
                ('easyfood', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='easyfoods.EasyFood', verbose_name='간편식')),
                ('fruit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fruitboxes.Fruitbox', verbose_name='과일박스')),
                ('salad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='salads.Salad', verbose_name='샐러드선택')),
            ],
            options={
                'verbose_name': '샐러드달력',
                'verbose_name_plural': '샐러드달력',
                'ordering': ['day'],
            },
        ),
    ]