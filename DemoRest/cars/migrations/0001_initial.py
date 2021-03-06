# Generated by Django 2.2.8 on 2019-12-30 08:15

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
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vin', models.CharField(db_index=True, max_length=64, verbose_name='Vin')),
                ('color', models.CharField(max_length=34, verbose_name='Color')),
                ('brand', models.CharField(max_length=44, verbose_name='Brand')),
                ('car_type', models.IntegerField(choices=[(1, 'Седан'), (2, 'Хэчбэк'), (3, 'Универсал'), (4, 'Купе')], verbose_name='Car_Type')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
