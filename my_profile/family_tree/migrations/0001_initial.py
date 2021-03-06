# Generated by Django 3.2.5 on 2021-07-29 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='familyData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(unique=True)),
                ('first', models.CharField(max_length=20)),
                ('second', models.CharField(max_length=20)),
                ('third', models.CharField(max_length=20)),
                ('last', models.CharField(max_length=20)),
                ('father', models.IntegerField(null=True)),
                ('mother', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='accessRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='family_tree.familydata')),
            ],
        ),
    ]
