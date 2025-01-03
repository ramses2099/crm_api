# Generated by Django 5.1.4 on 2025-01-02 12:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomerType",
            fields=[
                (
                    "customertype_id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="customertype_id",
                    ),
                ),
                ("description", models.CharField(max_length=250)),
                ("updated", models.DateTimeField(blank=True, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "customer_id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="customer_id",
                    ),
                ),
                ("firstname", models.CharField(max_length=600)),
                ("lastname", models.CharField(max_length=600)),
                ("updated", models.DateTimeField(blank=True, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="users",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "customertype",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="api.customertype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Status",
            fields=[
                (
                    "status_id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="status_id",
                    ),
                ),
                ("description", models.CharField(max_length=250)),
                ("updated", models.DateTimeField(blank=True, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="status",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="customertype",
            name="status",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="status",
                to="api.status",
            ),
        ),
        migrations.CreateModel(
            name="CustomerPhone",
            fields=[
                (
                    "customerphone_id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="customerphone_id",
                    ),
                ),
                ("phone", models.CharField(max_length=20)),
                ("updated", models.DateTimeField(blank=True, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="api.customer"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "customertype",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="api.customertype",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="api.status"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CustomerEmail",
            fields=[
                (
                    "customeremail_id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="customeremail_id",
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("updated", models.DateTimeField(blank=True, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="api.customer"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "customertype",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="api.customertype",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="api.status"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CustomerAddress",
            fields=[
                (
                    "customeraddress_id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="customeraddress_id",
                    ),
                ),
                ("address", models.CharField(max_length=850)),
                ("city", models.CharField(max_length=500)),
                ("province", models.CharField(max_length=500)),
                ("postalcode", models.CharField(max_length=15)),
                ("updated", models.DateTimeField(blank=True, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="api.customer"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "customertype",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="api.customertype",
                    ),
                ),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="api.status"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="customer",
            name="status",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="api.status"
            ),
        ),
    ]
