# Generated by Django 5.1.2 on 2024-10-23 17:13

import django.core.validators
import worldofspeed.userprofile.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(3), worldofspeed.userprofile.validators.UserNameValidator()], verbose_name='Username')),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField(help_text='Age requirement: 21 years and above.', validators=[django.core.validators.MinValueValidator(21)], verbose_name='Age')),
                ('password', models.CharField(max_length=20, verbose_name='Password')),
                ('firstname', models.CharField(blank=True, max_length=25, null=True, verbose_name='First Name')),
                ('lastname', models.CharField(blank=True, max_length=25, null=True, verbose_name='Last Name')),
                ('profile_picture', models.URLField(blank=True, null=True, verbose_name='Profile Picture')),
            ],
        ),
    ]
