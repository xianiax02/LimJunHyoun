# Generated by Django 3.2 on 2022-08-15 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '__first__'),
        ('imageSearch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('officialaccounts', models.CharField(blank=True, max_length=50, verbose_name='공식계정')),
                ('officialaccounts_id', models.CharField(blank=True, max_length=15, verbose_name='공식계정id')),
                ('scheduleaccount', models.CharField(blank=True, max_length=50, null=True, verbose_name='일정계정')),
                ('scheduleaccount_id', models.CharField(blank=True, max_length=15, null=True, verbose_name='일정계정_id')),
                ('refergroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.group', verbose_name='<django.db.models.query_utils.DeferredAttribute object at 0x000001DAFC6873D0>공식일정')),
            ],
            options={
                'verbose_name': '그룹공지',
                'verbose_name_plural': '그룹공지',
                'db_table': 'groupnotification_table',
            },
        ),
        migrations.RemoveField(
            model_name='fantweet',
            name='group',
        ),
        migrations.RemoveField(
            model_name='notice',
            name='author',
        ),
        migrations.DeleteModel(
            name='Content',
        ),
        migrations.DeleteModel(
            name='Fantweet',
        ),
        migrations.DeleteModel(
            name='Notice',
        ),
    ]
