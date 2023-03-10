# Generated by Django 4.1.7 on 2023-03-03 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomEmetteur', models.CharField(max_length=100)),
                ('prenomEmetteur', models.CharField(max_length=100)),
                ('telephoneEmetteur', models.CharField(max_length=100)),
                ('lieuColis', models.CharField(max_length=200)),
                ('detailLocalisation', models.TextField(max_length=500)),
                ('villeReception', models.CharField(max_length=200)),
                ('pointRelais', models.CharField(max_length=200)),
                ('notification', models.TextField(max_length=500)),
                ('nomDestinataire', models.CharField(max_length=200)),
                ('prenomDestinataire', models.CharField(max_length=200)),
                ('telephoneDestinataire', models.CharField(max_length=200)),
                ('emailDestinataire', models.EmailField(max_length=254)),
                ('typeColis', models.CharField(max_length=200)),
                ('poids', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=500)),
                ('follow_code', models.CharField(max_length=200, null=True)),
                ('is_validated', models.BooleanField(default=False)),
                ('transactionId', models.CharField(max_length=300, null=True, unique=True)),
                ('is_lancement', models.BooleanField(default=True)),
                ('is_enlevement', models.BooleanField(default=False)),
                ('is_acheminement', models.BooleanField(default=False)),
                ('is_reception', models.BooleanField(default=False)),
                ('is_termine', models.BooleanField(default=False)),
                ('client_id', models.IntegerField()),
                ('created_date', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
