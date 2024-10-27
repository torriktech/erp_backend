# Generated by Django 5.0.4 on 2024-09-28 14:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cashbook",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(default=django.utils.timezone.now)),
                ("description", models.CharField(max_length=255)),
                ("voucher_number", models.CharField(max_length=50, unique=True)),
                (
                    "transaction_type",
                    models.CharField(
                        choices=[("Income", "Income"), ("Expense", "Expense")],
                        max_length=7,
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "balance",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
            ],
        ),
    ]