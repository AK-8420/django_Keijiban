# Generated by Django 3.2.9 on 2021-11-07 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keijiban', '0003_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='ipID',
            field=models.CharField(blank=True, default='xxxxxxxx', max_length=8),
        ),
    ]
