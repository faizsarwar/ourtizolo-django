# Generated by Django 3.2.7 on 2022-04-06 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0002_press'),
    ]

    operations = [
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crop', models.CharField(max_length=100)),
                ('ProductUsed', models.CharField(max_length=100)),
                ('result_In_Percentage', models.IntegerField()),
                ('protocol', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
