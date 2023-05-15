# Generated by Django 4.2 on 2023-05-10 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=20)),
                ('type', models.CharField(max_length=10)),
                ('name', models.CharField(blank=True, default='', max_length=10)),
                ('token', models.CharField(blank=True, default='', max_length=20)),
                ('overview', models.CharField(blank=True, default='', max_length=255)),
                ('cover', models.CharField(blank=True, default='', max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='student',
        ),
    ]
