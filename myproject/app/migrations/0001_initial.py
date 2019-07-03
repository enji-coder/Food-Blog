# Generated by Django 2.2.2 on 2019-06-13 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=20)),
                ('password', models.CharField(max_length=30)),
                ('profile_pic', models.FileField(blank=True, upload_to='img/')),
            ],
        ),
    ]
