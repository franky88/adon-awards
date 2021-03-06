# Generated by Django 3.2.7 on 2021-09-28 12:21

import awards.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0005_certbg_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdonLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_name', models.CharField(blank=True, max_length=200, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to=awards.models.background_directory_path)),
            ],
        ),
        migrations.AlterModelOptions(
            name='awardee',
            options={'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='awardee',
            name='award_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='awards.awardtitle'),
        ),
        migrations.AlterField(
            model_name='awardee',
            name='background',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='awards.certbg', verbose_name='background theme'),
        ),
        migrations.AlterField(
            model_name='awardee',
            name='date',
            field=models.DateField(help_text='Date of the awarding ceremony', verbose_name='date of awarding'),
        ),
    ]
