# Generated by Django 4.0.2 on 2022-02-24 03:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0011_alter_author_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='id',
            field=models.UUIDField(auto_created=True, default=uuid.UUID('68962672-0de3-4f7b-8fbf-0160e5f0f412'), primary_key=True, serialize=False, verbose_name='作者编号'),
        ),
    ]
