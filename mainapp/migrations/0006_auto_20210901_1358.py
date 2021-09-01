# Generated by Django 2.2.5 on 2021-09-01 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20210901_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.CharField(default='NOT SET', max_length=10, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='brief_info',
            field=models.CharField(default='NOT SET', max_length=20, verbose_name='Background Infomation'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='facebook',
            field=models.CharField(default='NOT SET', max_length=15, verbose_name='Facebook'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='home_address',
            field=models.CharField(default='NOT SET', max_length=30, verbose_name='Home Address'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='home_district',
            field=models.CharField(default='NOT SET', max_length=10, verbose_name='Home District'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='home_postalcode',
            field=models.CharField(default='NOT SET', max_length=10, verbose_name='Home Postal Code'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='home_province',
            field=models.CharField(default='NOT SET', max_length=10, verbose_name='Home Province'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='line',
            field=models.CharField(default='NOT SET', max_length=10, verbose_name='LINE'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter',
            field=models.CharField(default='NOT SET', max_length=15, verbose_name='Twitter'),
        ),
    ]