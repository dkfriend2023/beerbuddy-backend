# Generated by Django 4.2.2 on 2023-09-24 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authentication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=30, verbose_name='휴대폰 번호')),
                ('auth_number', models.CharField(max_length=30, verbose_name='인증번호')),
            ],
            options={
                'verbose_name_plural': '휴대폰인증 관리 페이지',
                'db_table': 'authentications',
            },
        ),
    ]