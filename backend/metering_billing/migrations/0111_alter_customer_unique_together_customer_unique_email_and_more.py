# Generated by Django 4.0.5 on 2022-12-11 22:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("metering_billing", "0110_alter_metric_unique_together_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="customer",
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name="customer",
            constraint=models.UniqueConstraint(
                fields=("organization", "email"), name="unique_email"
            ),
        ),
        migrations.AddConstraint(
            model_name="customer",
            constraint=models.UniqueConstraint(
                fields=("organization", "customer_id"), name="unique_customer_id"
            ),
        ),
    ]
