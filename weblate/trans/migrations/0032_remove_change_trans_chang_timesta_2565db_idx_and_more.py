# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 5.1.8 on 2025-04-02 17:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lang", "0004_alter_language_direction"),
        ("screenshots", "0001_squashed_weblate_5"),
        ("trans", "0031_alter_change_action"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="change",
            name="trans_chang_timesta_2565db_idx",
        ),
        migrations.RemoveIndex(
            model_name="change",
            name="trans_chang_project_6d802b_idx",
        ),
        migrations.RemoveIndex(
            model_name="change",
            name="trans_chang_languag_33816c_idx",
        ),
        migrations.RemoveIndex(
            model_name="change",
            name="trans_chang_project_d37cd3_idx",
        ),
        migrations.RemoveIndex(
            model_name="change",
            name="trans_chang_compone_5e4964_idx",
        ),
        migrations.RemoveIndex(
            model_name="change",
            name="trans_chang_transla_36a8a9_idx",
        ),
        migrations.RemoveIndex(
            model_name="change",
            name="trans_chang_unit_id_6d86c1_idx",
        ),
        migrations.RemoveIndex(
            model_name="change",
            name="trans_chang_user_id_88ba38_idx",
        ),
        migrations.AddIndex(
            model_name="change",
            index=models.Index(
                fields=["-timestamp", "action"], name="trans_change_action_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="change",
            index=models.Index(
                condition=models.Q(("project__isnull", False)),
                fields=["project", "-timestamp", "action"],
                name="trans_change_project_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="change",
            index=models.Index(
                condition=models.Q(("language__isnull", False)),
                fields=["language", "-timestamp", "action"],
                name="trans_change_language_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="change",
            index=models.Index(
                condition=models.Q(
                    ("project__isnull", False), ("language__isnull", False)
                ),
                fields=["project", "language", "-timestamp", "action"],
                name="trans_change_prj_language_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="change",
            index=models.Index(
                condition=models.Q(("component__isnull", False)),
                fields=["component", "-timestamp", "action"],
                name="trans_change_component_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="change",
            index=models.Index(
                condition=models.Q(("translation__isnull", False)),
                fields=["translation", "-timestamp", "action"],
                name="trans_change_translation_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="change",
            index=models.Index(
                condition=models.Q(("unit__isnull", False)),
                fields=["unit", "-timestamp", "action"],
                name="trans_change_unit_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="change",
            index=models.Index(
                fields=["user", "-timestamp", "action"], name="trans_change_user_idx"
            ),
        ),
    ]
