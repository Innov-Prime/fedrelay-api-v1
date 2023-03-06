# Generated by Django 4.1.7 on 2023-03-03 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=200)),
                ('telephone', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=600)),
                ('object', models.CharField(max_length=600)),
                ('created_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
