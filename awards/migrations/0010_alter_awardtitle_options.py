# Generated by Django 3.2.7 on 2021-09-30 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0009_remove_awardee_gender'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='awardtitle',
            options={'ordering': ['-created']},
        ),
    ]
