# Generated by Django 2.1.3 on 2018-12-04 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20181203_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=45)),
                ('contrasena', models.CharField(max_length=45)),
            ],
        ),
    ]