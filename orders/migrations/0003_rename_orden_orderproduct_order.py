# Generated by Django 4.2.16 on 2025-03-06 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_rename_order_orderproduct_orden"),
    ]

    operations = [
        migrations.RenameField(
            model_name="orderproduct",
            old_name="orden",
            new_name="order",
        ),
    ]
