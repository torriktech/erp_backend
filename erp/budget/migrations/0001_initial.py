# Generated by Django 5.0.4 on 2024-07-28 17:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("project", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Budget",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("budget_position", models.CharField(max_length=255)),
                ("start_date", models.DateTimeField()),
                ("end_date", models.DateTimeField()),
                ("planned_amount", models.FloatField()),
                ("practical_amount", models.FloatField()),
                ("paid_amount", models.FloatField()),
                ("paid_date", models.DateTimeField()),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                (
                    "project_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="budgets",
                        to="project.project",
                    ),
                ),
            ],
        ),
    ]
