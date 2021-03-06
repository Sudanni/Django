# Generated by Django 2.1.7 on 2019-05-22 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vir_machine',
            fields=[
                ('vir_name', models.CharField(max_length=50, null=True)),
                ('vir_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('vir_ip', models.CharField(max_length=50, null=True)),
                ('phy_name', models.CharField(max_length=50, null=True)),
                ('img_name', models.CharField(max_length=100)),
                ('os_name', models.CharField(max_length=100)),
                ('account_id', models.CharField(max_length=50)),
                ('account_name', models.CharField(max_length=50)),
                ('vir_cpu', models.IntegerField(max_length=50)),
                ('vir_cpu_rate', models.CharField(max_length=50, null=True)),
                ('vir_memory', models.IntegerField(max_length=9999)),
                ('vir_memory_rate', models.CharField(max_length=50, null=True)),
                ('disk_type', models.CharField(max_length=100, null=True)),
                ('disk_total', models.IntegerField(max_length=50, null=True)),
                ('create_time', models.CharField(max_length=100, null=True)),
                ('belong_sys', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'vir_machine',
            },
        ),
    ]
