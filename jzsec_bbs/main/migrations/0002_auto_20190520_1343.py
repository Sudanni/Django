# Generated by Django 2.1.7 on 2019-05-20 05:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discuss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='请填写内容')),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('comment_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Discuss',
            },
        ),
        migrations.AlterField(
            model_name='blog',
            name='create_at',
            field=models.IntegerField(default=1558330994, null=True),
        ),
        migrations.AddField(
            model_name='discuss',
            name='to_blog_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_blog_id', to='main.Blog', to_field='blog_id'),
        ),
        migrations.AddField(
            model_name='discuss',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
