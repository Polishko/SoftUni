# Generated by Django 4.2.4 on 2023-10-20 06:16

from django.db import migrations


def create_unique_brands(apps, schema_editor):
    shoe = apps.get_model("main_app", "Shoe")
    unique_brands = apps.get_model("main_app", "UniqueBrands")

    db_alias = schema_editor.connection.alias

    unique_brand_names = shoe.objects.values_list("brand", flat=True).distinct()

    for brand_name in unique_brand_names:
        unique_brands.objects.using(db_alias).create(brand_name=brand_name)

    # this is not very good because you create and add each value set, its better first to create all values (instances) and then populate the db using class_name.objects.bulk_create(list_of_objects)


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_uniquebrands'),
    ]

    operations = [
        migrations.RunPython(create_unique_brands)
    ]
