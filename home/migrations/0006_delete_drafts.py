# Generated by Django 5.0.6 on 2024-08-16 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_drafts_draft'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Drafts',
        ),
    ]