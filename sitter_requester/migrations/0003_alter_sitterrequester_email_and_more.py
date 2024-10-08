# Generated by Django 4.2.15 on 2024-09-27 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitter_requester', '0002_alter_sitterrequester_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitterrequester',
            name='email',
            field=models.CharField(max_length=256, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='sitterrequester',
            name='sitter_requester_id',
            field=models.IntegerField(default=1727424120627803, editable=False, unique=True),
        ),
    ]
