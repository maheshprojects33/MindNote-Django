# Generated by Django 4.1.7 on 2023-04-18 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_bio_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='country',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
