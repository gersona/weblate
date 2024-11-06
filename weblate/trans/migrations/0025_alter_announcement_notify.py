# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 5.0.3 on 2024-10-25 17:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("trans", "0024_component_key_filter"),
    ]

    operations = [
        migrations.AlterField(
            model_name="announcement",
            name="notify",
            field=models.BooleanField(
                blank=True,
                default=False,
                help_text="Send notification to subscribed users.",
                verbose_name="Notify users",
            ),
        ),
    ]
