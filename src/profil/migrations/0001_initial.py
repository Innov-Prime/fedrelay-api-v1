# Generated by Django 4.1.4 on 2023-01-31 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0003_alter_user_email_alter_user_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfilModel',
            fields=[
                ('nom', models.CharField(max_length=200)),
                ('prenom', models.CharField(max_length=200)),
                ('telephone', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('profession', models.CharField(max_length=200)),
                ('pays', models.CharField(max_length=100)),
                ('ville', models.CharField(max_length=200)),
                ('quartier', models.CharField(max_length=200)),
                ('created_date', models.DateField(auto_now=True)),
                ('avatar', models.CharField(max_length=10000, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
