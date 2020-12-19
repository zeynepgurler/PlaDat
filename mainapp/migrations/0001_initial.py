# Generated by Django 3.1.4 on 2020-12-18 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('skill_1', models.CharField(default='', max_length=100)),
                ('condition_1', models.IntegerField(default=0)),
                ('skill_2', models.CharField(default='', max_length=100)),
                ('condition_2', models.IntegerField(default=0)),
                ('skill_3', models.CharField(default='', max_length=100)),
                ('condition_3', models.IntegerField(default=0)),
                ('skill_4', models.CharField(default='', max_length=100)),
                ('condition_4', models.IntegerField(default=0)),
                ('skill_5', models.CharField(default='', max_length=100)),
                ('condition_5', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=100)),
                ('job_description', models.CharField(max_length=100)),
                ('publish_time', models.DateTimeField(auto_now_add=True)),
                ('skill_1', models.CharField(default='', max_length=100)),
                ('condition_1', models.IntegerField(default=0)),
                ('skill_2', models.CharField(default='', max_length=100)),
                ('condition_2', models.IntegerField(default=0)),
                ('skill_3', models.CharField(default='', max_length=100)),
                ('condition_3', models.IntegerField(default=0)),
                ('skill_4', models.CharField(default='', max_length=100)),
                ('condition_4', models.IntegerField(default=0)),
                ('skill_5', models.CharField(default='', max_length=100)),
                ('condition_5', models.IntegerField(default=0)),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.employer')),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('apply_time', models.DateTimeField(auto_now_add=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.job')),
            ],
        ),
    ]