# Generated by Django 3.2.6 on 2021-08-26 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20210825_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batterywarranty',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='batterywarranty',
            name='shop_name',
            field=models.CharField(default='NOT SET', max_length=50, verbose_name='Shop Name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]