# Generated by Django 4.2.2 on 2023-08-05 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_about_hero_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('body', models.TextField()),
                ('img', models.ImageField(upload_to='blog')),
            ],
        ),
    ]
