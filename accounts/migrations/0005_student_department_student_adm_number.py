# Generated by Django 4.2.1 on 2023-05-20 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_student_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Department',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='adm_number',
            field=models.CharField(blank=True, max_length=3),
        ),
    ]
