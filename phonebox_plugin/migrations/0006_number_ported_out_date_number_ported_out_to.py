# Generated by Django 4.1.4 on 2023-03-08 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebox_plugin', '0005_number_is_owner_number_ported_out'),
    ]

    operations = [
        migrations.AddField(
            model_name='number',
            name='ported_out_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='number',
            name='ported_out_to',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
