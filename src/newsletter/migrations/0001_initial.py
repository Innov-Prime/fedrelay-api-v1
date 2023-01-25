# Generated by Django 4.1.4 on 2023-01-25 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=300, unique=True)),
                ('created_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
