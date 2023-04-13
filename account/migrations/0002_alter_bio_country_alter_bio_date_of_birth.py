# Generated by Django 4.2 on 2023-04-11 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bio',
            name='country',
            field=models.CharField(blank=True, choices=[('NP', 'Nepal'), ('IN', 'India'), ('CH', 'China')], default='Nepal', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='bio',
            name='date_of_birth',
            field=models.DateField(blank=True, default='1990-01-01', null=True),
        ),
    ]
