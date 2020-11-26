# Generated by Django 3.0.7 on 2000-01-01 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=123, null=True)),
                ('last_name', models.CharField(max_length=123, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone_number', models.IntegerField()),
                ('passport', models.ImageField(blank=True, upload_to='passport_pic')),
                ('country', models.CharField(max_length=123, null=True)),
                ('address', models.CharField(max_length=123, null=True)),
                ('next_of_kin_name', models.CharField(max_length=123, null=True)),
                ('next_of_kin_email', models.EmailField(max_length=254, null=True)),
            ],
        ),
    ]
