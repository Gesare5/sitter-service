# Generated by Django 4.2.15 on 2024-09-27 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitter',
            name='service_type',
            field=models.IntegerField(choices=[(0, 'Pet'), (1, 'House')], default=0),
        ),
        migrations.AlterField(
            model_name='sitter',
            name='email',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='sitter',
            name='sitter_id',
            field=models.IntegerField(default=1727423458767881, editable=False, unique=True),
        ),
    ]
