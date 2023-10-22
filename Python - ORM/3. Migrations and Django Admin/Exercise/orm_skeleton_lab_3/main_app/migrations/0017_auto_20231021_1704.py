# Generated by Django 4.2.4 on 2023-10-21 14:04

from django.db import migrations


def add_price(apps, schema_editor):
    Item = apps.get_model("main_app", "Item")

    all_items = Item.objects.all()

    for item in all_items:
        if item.price <= 10:
            item.rarity = "Rare"
        elif 11 <= item.price <= 20:
            item.rarity = "Very Rare"
        elif 21 <= item.price <= 30:
            item.rarity = "Extremely Rare"
        else:
            item.rarity = "Mega Rare"

        item.save()


def reverse_add_price(apps, schema_editor):
    Item = apps.get_model("main_app", "Item")

    all_items = Item.objects.all()

    for item in all_items:
        item.rarity = "empty"
        item.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_item'),
    ]

    operations = [migrations.RunPython(
        add_price, reverse_code=reverse_add_price
    )
    ]
