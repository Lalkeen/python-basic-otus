# Generated by Django 4.2.3 on 2023-07-20 12:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("showcase_app", "0004_product_updated_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="archived",
            field=models.BooleanField(default=False),
        ),
    ]