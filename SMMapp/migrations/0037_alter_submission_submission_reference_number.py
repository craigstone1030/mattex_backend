# Generated by Django 4.0.4 on 2022-07-29 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SMMapp', '0036_submission_submission_reference_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='submission_reference_number',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='Submission reference number'),
        ),
    ]