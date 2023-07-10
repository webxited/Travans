# Generated by Django 4.1.6 on 2023-02-07 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeapp', '0017_landingpagetestimonialheadings'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('contact_text', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=255)),
                ('facebook_link', models.CharField(max_length=1000)),
                ('instagram_link', models.CharField(max_length=1000)),
                ('opening_text', models.CharField(max_length=20)),
                ('days_list_one', models.CharField(max_length=255)),
                ('timing_days_list_one', models.CharField(max_length=255)),
                ('days_list_two', models.CharField(max_length=255)),
                ('timing_days_list_two', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=2500)),
            ],
        ),
    ]
