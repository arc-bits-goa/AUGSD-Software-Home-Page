# Generated by Django 3.1.7 on 2021-04-28 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_auto_20210428_1755'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portal',
            old_name='Add_repo_link2',
            new_name='Add_repo_link',
        ),
        migrations.RenameField(
            model_name='script',
            old_name='Add_repo_link2',
            new_name='Add_repo_link',
        ),
        migrations.AlterField(
            model_name='portal',
            name='repo_link2',
            field=models.CharField(default='-', max_length=1000),
        ),
    ]