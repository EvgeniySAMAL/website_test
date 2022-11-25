# Generated by Django 4.1.3 on 2022-11-25 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('task', models.TextField(verbose_name='Описание')),
                ('technology', models.CharField(max_length=50)),
            ],
        ),
    ]
