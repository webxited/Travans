# Generated by Django 4.1.6 on 2023-02-07 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeapp', '0016_remove_landingpagetestimonial_testimonial_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandingPageTestimonialHeadings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testimonial_text', models.CharField(max_length=30)),
                ('testimonial_description', models.CharField(max_length=100)),
            ],
        ),
    ]
