# Generated by Django 4.2.2 on 2023-08-05 09:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('user_image', models.FileField(blank=True, upload_to='users', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png', 'pdf', 'svg'])], verbose_name='프로필 이미지')),
                ('user_nickname', models.CharField(max_length=10, unique=True)),
                ('uni', models.CharField(help_text='대학교 풀네임(ex, OO대학교)', max_length=20, verbose_name='소속 대학교')),
                ('phone_number', models.CharField(blank=True, max_length=13, unique=True, validators=[django.core.validators.RegexValidator('^010-?[1-9]\\d{3}-?\\d{4}$')])),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
