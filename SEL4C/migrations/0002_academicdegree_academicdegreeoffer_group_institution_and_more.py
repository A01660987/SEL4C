# Generated by Django 4.2.4 on 2023-09-28 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SEL4C', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicDegree',
            fields=[
                ('identificator', models.SmallAutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('denomination', models.CharField(max_length=25, unique=True, verbose_name='Academic Degree')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Academic Degree',
                'verbose_name_plural': 'Academic Degrees',
                'db_table': 'academicdegree',
                'ordering': ['identificator'],
            },
        ),
        migrations.CreateModel(
            name='AcademicDegreeOffer',
            fields=[
                ('identificator', models.SmallAutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('denomination', models.CharField(max_length=25, unique=True, verbose_name='Academic Degree Offer')),
                ('description', models.CharField(max_length=50, null=True, verbose_name='Description')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('academicDegree', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='SEL4C.academicdegree', verbose_name='Academic Degree')),
            ],
            options={
                'verbose_name': 'Academic Degree Offer',
                'verbose_name_plural': 'Academic Degree Offers',
                'db_table': 'academicdegreeoffer',
                'ordering': ['identificator'],
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('identificator', models.SmallAutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('denomination', models.CharField(max_length=25, unique=True, verbose_name='Group')),
                ('description', models.CharField(max_length=50, null=True, verbose_name='Description')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
                'db_table': 'group',
                'ordering': ['identificator'],
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('identificator', models.SmallAutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('denomination', models.CharField(max_length=25, unique=True, verbose_name='Institution')),
                ('description', models.CharField(max_length=50, null=True, verbose_name='Description')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Institution',
                'verbose_name_plural': 'Institutions',
                'db_table': 'institution',
                'ordering': ['identificator'],
            },
        ),
        migrations.AlterField(
            model_name='country',
            name='identificator',
            field=models.SmallAutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='gender',
            name='identificator',
            field=models.SmallAutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SEL4C.country', verbose_name='Country'),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('identificator', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='SEL4C.user', unique=True, verbose_name='ID')),
                ('code', models.CharField(max_length=25, unique=True, verbose_name='Code')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SEL4C.group', verbose_name='Group')),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
                'db_table': 'student',
                'ordering': ['identificator'],
            },
        ),
        migrations.CreateModel(
            name='AcademicDiscipline',
            fields=[
                ('identificator', models.SmallAutoField(editable=False, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('denomination', models.CharField(max_length=25, unique=True, verbose_name='Academic Discipline')),
                ('description', models.CharField(max_length=50, null=True, verbose_name='Description')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('academicDegreeOffer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SEL4C.academicdegreeoffer', verbose_name='Academic Degree Offer')),
            ],
            options={
                'verbose_name': 'Academic Discipline',
                'verbose_name_plural': 'Academic Disciplines',
                'db_table': 'academicdiscipline',
                'ordering': ['identificator'],
            },
        ),
        migrations.AddField(
            model_name='academicdegreeoffer',
            name='institution',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='SEL4C.institution', verbose_name='Institution'),
        ),
        migrations.AlterUniqueTogether(
            name='academicdegreeoffer',
            unique_together={('institution', 'academicDegree')},
        ),
    ]
