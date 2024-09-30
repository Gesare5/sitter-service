# Generated by Django 4.2.15 on 2024-09-27 08:20

from django.db import migrations, models
import sitterapi.utils


class Migration(migrations.Migration):

    dependencies = [
        ('sitter', '0003_alter_sitter_email_alter_sitter_sitter_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitter',
            name='sitter_id',
            field=models.IntegerField(default=sitterapi.utils.create_id_from_timestamp, editable=False, unique=True),
        ),
    ]
