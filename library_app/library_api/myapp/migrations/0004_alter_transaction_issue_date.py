# Generated by Django 5.0.3 on 2024-03-14 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_transaction_alter_book_authors_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='issue_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]