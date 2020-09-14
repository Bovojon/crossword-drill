# Generated by Django 2.2.4 on 2020-09-14 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_text', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField()),
                ('byline', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Clue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clue_text', models.CharField(max_length=512)),
                ('theme', models.BooleanField(default=False)),
                ('entry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xword_data.Entry')),
                ('puzzle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xword_data.Puzzle')),
            ],
        ),
    ]