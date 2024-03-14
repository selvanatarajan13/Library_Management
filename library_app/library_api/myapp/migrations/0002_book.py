# Generated by Django 5.0.3 on 2024-03-12 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookID', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('authors', models.CharField(max_length=200)),
                ('average_rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('isbn', models.CharField(max_length=20)),
                ('isbn13', models.CharField(max_length=20)),
                ('language_code', models.CharField(max_length=20)),
                ('num_pages', models.IntegerField()),
                ('ratings_count', models.IntegerField()),
                ('text_reviews_count', models.IntegerField()),
                ('publication_date', models.DateField()),
                ('publisher', models.CharField(max_length=100)),
            ],
        ),
    ]
