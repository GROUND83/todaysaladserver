# Generated by Django 2.2.5 on 2020-06-15 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=140, null=True, unique=True, verbose_name='이벤트제목')),
                ('description', models.TextField(null=True, verbose_name='이벤트설명')),
                ('photo', models.ImageField(blank=True, help_text='700px300px', upload_to='events_photos')),
                ('detailphoto', models.ImageField(blank=True, help_text='700px1200px', upload_to='events_photos')),
                ('isActive', models.BooleanField(default=False, verbose_name='이벤트진행중')),
            ],
            options={
                'verbose_name': '이벤트',
                'verbose_name_plural': '이벤트',
            },
        ),
    ]
