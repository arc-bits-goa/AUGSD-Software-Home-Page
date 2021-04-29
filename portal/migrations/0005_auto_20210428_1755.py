# Generated by Django 3.1.7 on 2021-04-28 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_auto_20210428_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='portal',
            name='Add_repo_link2',
            field=models.BooleanField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='script',
            name='Add_repo_link2',
            field=models.BooleanField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='portal',
            name='repo_link2',
            field=models.BooleanField(default='-', max_length=1000),
        ),
        migrations.AlterField(
            model_name='script',
            name='repo_link2',
            field=models.CharField(default='-', max_length=1000),
        ),
    ]