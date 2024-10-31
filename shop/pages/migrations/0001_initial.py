# Generated by Django 5.1.1 on 2024-10-14 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActionCatogory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='category_images')),
                ('title', models.CharField(max_length=64)),
                ('page_keywords', models.TextField()),
                ('page_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, max_length=64)),
                ('color', models.CharField(blank=True, max_length=64)),
                ('quantity', models.SmallIntegerField()),
                ('timer', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='category_images')),
                ('title', models.CharField(max_length=64)),
                ('slug', models.SlugField(unique=True)),
                ('page_keywords', models.TextField()),
                ('page_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('surname', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('svaluedesteny', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('adress', models.CharField(blank=True, max_length=255)),
                ('message', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('slug', models.SlugField(unique=True)),
                ('context', models.TextField()),
                ('page_keywords', models.TextField()),
                ('page_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product_images')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('short_description', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField()),
                ('page_keywords', models.TextField()),
                ('page_description', models.TextField()),
                ('size', models.CharField(blank=True, max_length=255)),
                ('color', models.CharField(blank=True, max_length=255)),
                ('price', models.FloatField()),
                ('sale', models.BooleanField()),
                ('prise_on_sale', models.FloatField()),
                ('image', models.ImageField(upload_to='product_images')),
                ('visible', models.BooleanField()),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Subcategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='category_images')),
                ('title', models.CharField(max_length=64)),
                ('slug', models.SlugField(unique=True)),
                ('page_keywords', models.TextField()),
                ('page_description', models.TextField()),
            ],
        ),
    ]
