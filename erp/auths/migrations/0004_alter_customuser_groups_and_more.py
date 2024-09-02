# Generated by Django 5.0.4 on 2024-09-01 10:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("auths", "0003_remove_employee_payroll_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="groups",
            field=models.ManyToManyField(
                blank=True, related_name="customuser_set", to="auth.group"
            ),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                related_name="customuser_set_permissions",
                to="auth.permission",
            ),
        ),
        migrations.AlterField(
            model_name="employee",
            name="company",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="employees",
                to="auths.companyprofile",
            ),
        ),
    ]
