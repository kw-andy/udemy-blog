# Generated by Django 3.1.6 on 2023-02-17 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('published', models.BooleanField(default=False)),
                ('date', models.DateField(blank=True)),
                ('content', models.TextField()),
            ],
        ),
    ]
