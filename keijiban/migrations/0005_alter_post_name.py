# Generated by Django 3.2.9 on 2021-11-07 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keijiban', '0004_auto_20211107_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(default='名無しさん', max_length=15),
        ),
    ]