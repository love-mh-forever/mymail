# Generated by Django 2.0.3 on 2018-05-15 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addresss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recv', models.CharField(max_length=50, verbose_name='收件人')),
                ('phone', models.CharField(max_length=11, null=True, verbose_name='联系方式')),
                ('province', models.CharField(max_length=50, verbose_name='省份')),
                ('city', models.CharField(max_length=50, verbose_name='城市')),
                ('country', models.CharField(max_length=50, null=True, verbose_name='县区')),
                ('intro', models.TextField(verbose_name='详细地址')),
                ('status', models.BooleanField(default=False)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Areainfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='地址')),
                ('parea', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Areainfo')),
            ],
        ),
    ]
