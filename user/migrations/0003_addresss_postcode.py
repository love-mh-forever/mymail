# Generated by Django 2.0.3 on 2018-05-15 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_addresss_areainfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='addresss',
            name='postcode',
            field=models.CharField(default='000000', max_length=6, verbose_name='邮编'),
        ),
    ]