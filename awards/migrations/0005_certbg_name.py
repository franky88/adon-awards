# Generated by Django 3.2.7 on 2021-09-25 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0004_awardee_background'),
    ]

    operations = [
        migrations.AddField(
            model_name='certbg',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
