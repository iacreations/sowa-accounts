# Generated by Django 5.2.4 on 2025-07-20 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sowaf', '0022_rename_residual_price_newasset_accumulated_depreciation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newasset',
            name='capitalization_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
