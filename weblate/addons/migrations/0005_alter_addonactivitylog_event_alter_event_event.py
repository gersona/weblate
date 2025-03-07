# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 5.1.6 on 2025-03-05 09:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("addons", "0004_alter_addonactivitylog_event_alter_event_event"),
    ]

    operations = [
        migrations.AlterField(
            model_name="addonactivitylog",
            name="event",
            field=models.IntegerField(
                choices=[
                    (1, "Repository post-push"),
                    (2, "Repository post-update"),
                    (3, "Repository pre-commit"),
                    (4, "Repository post-commit"),
                    (5, "Repository post-add"),
                    (6, "Unit pre-create"),
                    (7, "Storage post-load"),
                    (8, "Unit post-save"),
                    (9, "Repository pre-update"),
                    (10, "Repository pre-push"),
                    (11, "Daily"),
                    (12, "Component update"),
                    (13, "Event change"),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="event",
            field=models.IntegerField(
                choices=[
                    (1, "Repository post-push"),
                    (2, "Repository post-update"),
                    (3, "Repository pre-commit"),
                    (4, "Repository post-commit"),
                    (5, "Repository post-add"),
                    (6, "Unit pre-create"),
                    (7, "Storage post-load"),
                    (8, "Unit post-save"),
                    (9, "Repository pre-update"),
                    (10, "Repository pre-push"),
                    (11, "Daily"),
                    (12, "Component update"),
                    (13, "Event change"),
                ]
            ),
        ),
    ]
