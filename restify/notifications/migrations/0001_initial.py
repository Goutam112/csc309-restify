# Generated by Django 4.1.7 on 2023-03-12 00:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Notification",
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
                (
                    "content",
                    models.CharField(
                        choices=[
                            (
                                "HOST",
                                (
                                    ("host_new_reservation", "New reservation"),
                                    (
                                        "host_cancellation_request",
                                        "Cancellation Request",
                                    ),
                                ),
                            ),
                            (
                                "GUEST",
                                (
                                    (
                                        "guest_approved_reservation",
                                        "Approved reservation",
                                    ),
                                    (
                                        "guest_cancellation_request",
                                        "Cancellation Request",
                                    ),
                                ),
                            ),
                        ],
                        max_length=200,
                    ),
                ),
                ("created_when", models.DateTimeField(auto_now_add=True)),
                (
                    "receiver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
