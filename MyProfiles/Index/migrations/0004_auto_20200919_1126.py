# Generated by Django 3.0.3 on 2020-09-19 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0003_auto_20200919_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='password',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='social_media',
            field=models.CharField(max_length=264, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_name',
            field=models.CharField(max_length=264, null=True),
        ),
    ]