# Generated by Django 3.1.5 on 2021-01-13 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uniinf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rank', models.CharField(max_length=100)),
                ('Name_of_University', models.CharField(max_length=100)),
                ('Name_of_Course', models.CharField(max_length=100)),
                ('Link_to_the_program_highlights', models.CharField(max_length=200)),
                ('City', models.CharField(max_length=100)),
                ('Country', models.CharField(max_length=100)),
            ],
        ),
    ]
