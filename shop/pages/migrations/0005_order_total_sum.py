# Generated by Django 5.1.1 on 2024-10-15 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_basket_in_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_sum',
            field=models.IntegerField(default=0),
        ),
    ]
