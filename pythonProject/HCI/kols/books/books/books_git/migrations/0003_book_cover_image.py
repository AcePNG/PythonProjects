# Generated by Django 4.2.1 on 2023-06-02 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_git', '0002_alter_book_isbn_alter_book_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='cover_images/'),
        ),
    ]