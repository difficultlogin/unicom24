# Generated by Django 2.1.1 on 2018-09-27 08:42

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
            name='ClientProfileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True)),
                ('birthday', models.DateField()),
                ('phone', models.CharField(max_length=11)),
                ('passport_id', models.CharField(max_length=10)),
                ('scoring_score', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OfferModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('offer_type', models.SmallIntegerField(choices=[(1, 'Потребительский'), (2, 'Ипотека'), (3, 'Автокредит')])),
                ('scoring_score_min', models.IntegerField()),
                ('scoring_score_max', models.IntegerField()),
                ('rotation_start', models.DateTimeField()),
                ('rotation_end', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RequestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.SmallIntegerField(choices=[(1, 'новая'), (2, 'отправлена'), (3, 'получена'), (4, 'одобрено'), (5, 'отказано'), (6, 'выдано')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ClientProfileModel')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.OfferModel')),
            ],
        ),
    ]
