# Generated by Django 4.0.5 on 2022-12-12 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("metering_billing", "0112_merge_20221211_2248"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalorganization",
            name="is_demo",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="organization",
            name="is_demo",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="apitoken",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="api_keys",
                to="metering_billing.organization",
            ),
        ),
        migrations.AlterField(
            model_name="backtest",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="backtests",
                to="metering_billing.organization",
            ),
        ),
        migrations.AlterField(
            model_name="customer",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="customers",
                to="metering_billing.organization",
            ),
        ),
        migrations.AlterField(
            model_name="externalplanlink",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="external_plan_links",
                to="metering_billing.organization",
            ),
        ),
        migrations.AlterField(
            model_name="feature",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="features",
                to="metering_billing.organization",
            ),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="currency",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="metering_billing.pricingunit",
            ),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="customer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="invoices",
                to="metering_billing.customer",
            ),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="organization",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="invoices",
                to="metering_billing.organization",
            ),
        ),
        migrations.AlterField(
            model_name="invoice",
            name="subscription",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="invoices",
                to="metering_billing.subscription",
            ),
        ),
        migrations.AlterField(
            model_name="metric",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="billable_metrics",
                to="metering_billing.organization",
            ),
        ),
        migrations.AlterField(
            model_name="organizationinvitetoken",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="invite_token",
                to="metering_billing.organization",
            ),
        ),
        migrations.AlterField(
            model_name="organizationsetting",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="settings",
                to="metering_billing.organization",
            ),
        ),
        migrations.AlterField(
            model_name="plan",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="plans",
                to="metering_billing.organization",
            ),
        ),
        migrations.AlterField(
            model_name="planversion",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="plan_versions",
                to="metering_billing.organization",
            ),
        ),
        migrations.AlterField(
            model_name="priceadjustment",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="price_adjustments",
                to="metering_billing.organization",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="metering_billing.organization",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="organization",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="users",
                to="metering_billing.organization",
            ),
        ),
        migrations.AlterField(
            model_name="webhookendpoint",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="webhook_endpoints",
                to="metering_billing.organization",
            ),
        ),
    ]