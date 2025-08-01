# Generated by Django 5.2.4 on 2025-07-18 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sowaf', '0014_alter_newclient_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newclient',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='newclient',
            name='company_email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='newclient',
            name='contact',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='newclient',
            name='contact_email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='newclient',
            name='contact_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='newclient',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='newclient',
            name='credit_limit',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='newclient',
            name='currency',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='newclient',
            name='industry',
            field=models.CharField(blank=True, choices=[('Consumer products', 'Consumer products'), ('Energy and natural resources', 'Energy and natural resources'), ('Financial services', 'Financial services'), ('Healthcare', 'Healthcare'), ('Industrial products', 'Industrial products'), ('Not for profit', 'Not for profit'), ('Individual private clients', 'Individual private clients'), ('Public sector', 'Public sector'), ('Real estate and construction', 'Real estate and construction'), ('Services', 'Services'), ('Technology, media and telecommunications', 'Technology, media and telecommunications'), ('Travel, tourism and leisure', 'Travel, tourism and leisure'), ('Others', 'Others')], default='', null=True),
        ),
        migrations.AlterField(
            model_name='newclient',
            name='notes',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='newclient',
            name='payment_terms',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='newclient',
            name='phone',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='newclient',
            name='position',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='newclient',
            name='reg_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='newclient',
            name='status',
            field=models.CharField(blank=True, choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='newclient',
            name='tin',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
