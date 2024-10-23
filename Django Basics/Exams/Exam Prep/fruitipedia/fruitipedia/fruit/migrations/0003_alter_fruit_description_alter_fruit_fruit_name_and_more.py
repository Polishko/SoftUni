# Generated by Django 5.1.2 on 2024-10-23 12:16

import django.core.validators
import django.db.models.deletion
import fruitipedia.userprofile.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruit', '0002_alter_fruit_fruit_name'),
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruit',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='fruit',
            name='fruit_name',
            field=models.CharField(error_messages={'unique': 'This fruit name is already in use! Try a new one.'}, max_length=30, unique=True, validators=[django.core.validators.MinLengthValidator(2), fruitipedia.userprofile.validators.FruitNameValidator()], verbose_name='Fruit Name'),
        ),
        migrations.AlterField(
            model_name='fruit',
            name='image_url',
            field=models.URLField(verbose_name='Image URL'),
        ),
        migrations.AlterField(
            model_name='fruit',
            name='nutrition',
            field=models.TextField(blank=True, null=True, verbose_name='Nutrition'),
        ),
        migrations.AlterField(
            model_name='fruit',
            name='owner',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='fruits', to='userprofile.profile'),
        ),
    ]
