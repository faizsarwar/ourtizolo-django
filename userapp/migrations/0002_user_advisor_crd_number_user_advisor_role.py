# Generated by Django 4.1 on 2022-10-02 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='advisor_crd_number',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='advisor_role',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
