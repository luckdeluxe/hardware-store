# Generated by Django 3.2.5 on 2021-08-06 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billing_profiles', '0001_initial'),
        ('orders', '0003_order_shipping_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='billing_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billing_profiles.billingprofile'),
        ),
    ]