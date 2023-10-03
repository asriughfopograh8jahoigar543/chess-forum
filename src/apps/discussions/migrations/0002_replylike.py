# Generated by Django 4.2.5 on 2023-10-02 15:14

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("discussions", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ReplyLike",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                (
                    "reply",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="likes", to="discussions.reply"
                    ),
                ),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "ordering": ("-date_added",),
                "abstract": False,
            },
        ),
    ]
