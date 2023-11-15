# Generated by Django 4.2.2 on 2023-08-05 09:35

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='예약 일시')),
                ('book_number', models.UUIDField(default=uuid.uuid4, verbose_name='예약 번호')),
                ('people_num', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(8), django.core.validators.MaxValueValidator(200)], verbose_name='예약 인원')),
                ('meeting_name', models.CharField(max_length=15, verbose_name='모임명')),
                ('description', models.TextField(blank=True, max_length=100, verbose_name='요청 사항')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant', verbose_name='식당 이름')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='예약자 이름')),
            ],
        ),
    ]
