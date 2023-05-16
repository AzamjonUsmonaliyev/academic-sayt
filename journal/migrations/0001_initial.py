# Generated by Django 4.2.1 on 2023-05-16 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('image', models.FileField(upload_to='journal/image')),
                ('text', models.TextField()),
                ('issue', models.CharField(max_length=100)),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('publication_fees', models.TextField()),
                ('address', models.TextField()),
                ('ISSN', models.CharField(blank=True, max_length=15, null=True)),
                ('SJIF', models.FloatField(blank=True, null=True)),
                ('factor', models.FloatField(blank=True, null=True)),
                ('contact', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('DOI', models.URLField()),
                ('keywords', models.CharField(max_length=250)),
                ('abstract', models.TextField()),
                ('file', models.FileField(upload_to='journal/pdf')),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('text_cite', models.TextField()),
                ('section', models.CharField(blank=True, max_length=50, null=True)),
                ('start_page', models.PositiveSmallIntegerField()),
                ('end_page', models.PositiveSmallIntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.category')),
            ],
        ),
    ]
