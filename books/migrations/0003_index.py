# Generated by Django 4.2.2 on 2023-07-21 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_main'),
    ]

    operations = [
        migrations.CreateModel(
            name='index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstP', models.TextField()),
                ('secondP', models.TextField()),
                ('thirdP', models.TextField()),
                ('forthP', models.TextField()),
                ('fifthP', models.TextField()),
            ],
        ),
    ]