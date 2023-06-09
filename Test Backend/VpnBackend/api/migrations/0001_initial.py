# Generated by Django 4.2 on 2023-04-24 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applogo', models.ImageField(upload_to='AppLogo/')),
                ('appname', models.CharField(max_length=100)),
                ('packagename', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='VpnAccountsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('privatekey', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=100)),
                ('dns', models.CharField(max_length=100)),
                ('publickey', models.CharField(max_length=150)),
                ('presharedkey', models.CharField(max_length=100)),
                ('endpoints', models.CharField(max_length=100)),
                ('allowed_ips', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_enable', models.BooleanField(default=True)),
            ],
        ),
    ]
