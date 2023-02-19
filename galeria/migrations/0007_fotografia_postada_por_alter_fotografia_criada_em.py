# Generated by Django 4.1.6 on 2023-02-19 21:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("galeria", "0006_alter_fotografia_categoria_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="fotografia",
            name="postada_por",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="usuario",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="fotografia",
            name="criada_em",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 2, 19, 18, 31, 56, 930805)
            ),
        ),
    ]
