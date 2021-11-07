# Generated by Django 3.2.9 on 2021-11-06 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('keijiban', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='creator',
        ),
        migrations.AddField(
            model_name='post',
            name='ipID',
            field=models.CharField(blank=True, default='xxxxxxxx', max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('A', '雑談'), ('B', '質問'), ('C', 'その他')], default='A', max_length=1),
        ),
    ]