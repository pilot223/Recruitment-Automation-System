# Generated by Django 4.1.2 on 2022-10-18 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("Company", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Questions",
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
                ("question", models.TextField()),
                ("score", models.IntegerField()),
                (
                    "companyId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Company.companies",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Options",
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
                ("option", models.TextField()),
                (
                    "questionId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="exams.questions",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Answers",
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
                    "optionId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="exams.options"
                    ),
                ),
                (
                    "questionId",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="exams.questions",
                    ),
                ),
            ],
        ),
    ]
