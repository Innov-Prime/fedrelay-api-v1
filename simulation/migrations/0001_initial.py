# Generated by Django 4.1.7 on 2023-03-03 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Simulator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localisation', models.CharField(max_length=200)),
                ('product_type', models.CharField(max_length=200)),
                ('delivery_point', models.CharField(max_length=200)),
                ('delivery_delay', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=100)),
                ('created_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
