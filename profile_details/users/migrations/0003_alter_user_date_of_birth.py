# Generated by Django 5.1 on 2024-09-02 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_delete_profiledetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Date of birth'),
        ),
    ]
