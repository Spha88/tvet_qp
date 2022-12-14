# Generated by Django 4.0.5 on 2022-08-04 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0002_questionpaper_date_added_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionpaper',
            name='marking_guideline',
            field=models.FileField(null=True, upload_to='marking_guidelines/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='markingguideline',
            name='question_paper',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='papers.questionpaper'),
        ),
    ]
