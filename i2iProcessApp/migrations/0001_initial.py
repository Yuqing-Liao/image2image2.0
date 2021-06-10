# Generated by Django 3.2.1 on 2021-05-29 04:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('uploader', models.CharField(max_length=32)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('address', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='name')),
                ('passward', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(6, message='not less than 6')], verbose_name='password')),
                ('registe_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='admin',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='i2iProcessApp.user')),
                ('admin_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('Authorization', models.IntegerField(verbose_name='authorization')),
            ],
            bases=('i2iProcessApp.user',),
        ),
        migrations.CreateModel(
            name='client',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='i2iProcessApp.user')),
                ('client_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('history', models.TextField()),
            ],
            bases=('i2iProcessApp.user',),
        ),
    ]
