# Generated by Django 4.1.6 on 2023-02-07 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeapp', '0014_landingpagemenusection'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandingPageTestimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimonial_text', models.CharField(max_length=30)),
                ('testimonial_description', models.CharField(max_length=100)),
                ('client_name', models.CharField(max_length=100)),
                ('client_profession', models.CharField(max_length=100)),
                ('client_comment', models.CharField(max_length=1000)),
                ('client_image', models.ImageField(upload_to='img/%y')),
            ],
        ),
    ]
