# Generated by Django 5.2.4 on 2025-07-16 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sowaf', '0006_newsupplier'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsupplier',
            options={'ordering': ['company_name']},
        ),
    ]
