# Generated by Django 5.0.6 on 2024-08-16 09:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_drafts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drafts',
            name='draft',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.blog'),
        ),
    ]
