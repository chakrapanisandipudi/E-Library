# Generated by Django 4.2.1 on 2023-05-19 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_student_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
