# Generated by Django 4.1.4 on 2023-03-02 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebox_plugin', '0004_alter_number_created_alter_number_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='number',
            name='is_owner',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='number',
            name='ported_out',
            field=models.BooleanField(default=False),
        ),
    ]
