# Generated by Django 5.0.3 on 2024-03-30 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_products_previous_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='products',
            name='previous_price',
            field=models.IntegerField(default=0),
        ),
    ]