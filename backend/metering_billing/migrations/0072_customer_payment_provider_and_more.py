# Generated by Django 4.0.5 on 2022-11-11 06:35

from django.db import migrations, models
import metering_billing.utils.utils


class Migration(migrations.Migration):

    dependencies = [
        ("metering_billing", "0071_remove_historicalinvoice_old_customer_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="payment_provider",
            field=models.CharField(
                blank=True, choices=[("stripe", "Stripe")], max_length=40, null=True
            ),
        ),
        migrations.AddField(
            model_name="historicalcustomer",
            name="payment_provider",
            field=models.CharField(
                blank=True, choices=[("stripe", "Stripe")], max_length=40, null=True
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="customer_id",
            field=models.CharField(
                default=metering_billing.utils.utils.customer_uuid, max_length=50
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="customer_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="historicalcustomer",
            name="customer_id",
            field=models.CharField(
                default=metering_billing.utils.utils.customer_uuid, max_length=50
            ),
        ),
        migrations.AlterField(
            model_name="historicalcustomer",
            name="customer_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]