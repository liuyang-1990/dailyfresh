# Generated by Django 2.1 on 2018-08-14 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('df_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='mobilephone',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='postcode',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='recipients',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
