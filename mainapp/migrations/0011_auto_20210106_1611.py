# Generated by Django 3.1.1 on 2021-01-06 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_auto_20210106_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='user_id',
            field=models.IntegerField(default=''),
        ),
    ]