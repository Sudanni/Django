# Generated by Django 2.1.7 on 2019-05-20 05:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='default name', max_length=50)),
                ('blog_id', models.IntegerField(default=1, unique=True)),
                ('user_id', models.IntegerField(default=1, null=True)),
                ('user_name', models.CharField(default='default name', max_length=50)),
                ('content', models.CharField(default='请填写内容', max_length=9999)),
                ('create_at', models.IntegerField(default=1558330488, null=True)),
            ],
        ),

        migrations.CreateModel(
            name='img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_info', models.TextField(default='请填写内容')),
            ],
        ),
    ]
