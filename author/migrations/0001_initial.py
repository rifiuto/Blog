# Generated by Django 4.0.1 on 2022-01-10 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='作者编号')),
                ('username', models.CharField(max_length=50, verbose_name='登陆帐号')),
                ('password', models.CharField(max_length=50, verbose_name='登陆密码')),
                ('realname', models.CharField(max_length=20, verbose_name='作者姓名')),
            ],
            options={
                'verbose_name_plural': '作者',
            },
        ),
    ]