# Generated by Django 4.1.6 on 2023-02-04 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafeapp', '0013_landingpageaboutussection_delete_landingpageabout'),
    ]

    operations = [
        migrations.CreateModel(
            name='LandingPageMenuSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_text', models.CharField(max_length=20)),
                ('menu_heading', models.CharField(max_length=100)),
                ('menu_breakfast_description', models.CharField(max_length=20)),
                ('menu_breakfast_text', models.CharField(max_length=20)),
                ('menu_lunch_description', models.CharField(max_length=20)),
                ('menu_lunch_text', models.CharField(max_length=20)),
                ('menu_dinner_description', models.CharField(max_length=20)),
                ('menu_dinner_text', models.CharField(max_length=20)),
                ('menu_breakfast_item1_img', models.ImageField(upload_to='img/%y')),
                ('menu_breakfast_item1_name', models.CharField(max_length=150)),
                ('menu_breakfast_item1_description', models.CharField(max_length=255)),
                ('menu_breakfast_item1_price', models.IntegerField()),
                ('menu_breakfast_item2_img', models.ImageField(upload_to='img/%y')),
                ('menu_breakfast_item2_name', models.CharField(max_length=150)),
                ('menu_breakfast_item2_description', models.CharField(max_length=255)),
                ('menu_breakfast_item2_price', models.IntegerField()),
                ('menu_breakfast_item3_img', models.ImageField(upload_to='img/%y')),
                ('menu_breakfast_item3_name', models.CharField(max_length=150)),
                ('menu_breakfast_item3_description', models.CharField(max_length=255)),
                ('menu_breakfast_item3_price', models.IntegerField()),
                ('menu_breakfast_item4_img', models.ImageField(upload_to='img/%y')),
                ('menu_breakfast_item4_name', models.CharField(max_length=150)),
                ('menu_breakfast_item4_description', models.CharField(max_length=255)),
                ('menu_breakfast_item4_price', models.IntegerField()),
                ('menu_breakfast_item5_img', models.ImageField(upload_to='img/%y')),
                ('menu_breakfast_item5_name', models.CharField(max_length=150)),
                ('menu_breakfast_item5_description', models.CharField(max_length=255)),
                ('menu_breakfast_item5_price', models.IntegerField()),
                ('menu_breakfast_item6_img', models.ImageField(upload_to='img/%y')),
                ('menu_breakfast_item6_name', models.CharField(max_length=150)),
                ('menu_breakfast_item6_description', models.CharField(max_length=255)),
                ('menu_breakfast_item6_price', models.IntegerField()),
                ('menu_breakfast_item7_img', models.ImageField(upload_to='img/%y')),
                ('menu_breakfast_item7_name', models.CharField(max_length=150)),
                ('menu_breakfast_item7_description', models.CharField(max_length=255)),
                ('menu_breakfast_item7_price', models.IntegerField()),
                ('menu_breakfast_item8_img', models.ImageField(upload_to='img/%y')),
                ('menu_breakfast_item8_name', models.CharField(max_length=150)),
                ('menu_breakfast_item8_description', models.CharField(max_length=255)),
                ('menu_breakfast_item8_price', models.IntegerField()),
                ('menu_lunch_item1_img', models.ImageField(upload_to='img/%y')),
                ('menu_lunch_item1_name', models.CharField(max_length=150)),
                ('menu_lunch_item1_description', models.CharField(max_length=255)),
                ('menu_lunch_item1_price', models.IntegerField()),
                ('menu_lunch_item2_img', models.ImageField(upload_to='img/%y')),
                ('menu_lunch_item2_name', models.CharField(max_length=150)),
                ('menu_lunch_item2_description', models.CharField(max_length=255)),
                ('menu_lunch_item2_price', models.IntegerField()),
                ('menu_lunch_item3_img', models.ImageField(upload_to='img/%y')),
                ('menu_lunch_item3_name', models.CharField(max_length=150)),
                ('menu_lunch_item3_description', models.CharField(max_length=255)),
                ('menu_lunch_item3_price', models.IntegerField()),
                ('menu_lunch_item4_img', models.ImageField(upload_to='img/%y')),
                ('menu_lunch_item4_name', models.CharField(max_length=150)),
                ('menu_lunch_item4_description', models.CharField(max_length=255)),
                ('menu_lunch_item4_price', models.IntegerField()),
                ('menu_lunch_item5_img', models.ImageField(upload_to='img/%y')),
                ('menu_lunch_item5_name', models.CharField(max_length=150)),
                ('menu_lunch_item5_description', models.CharField(max_length=255)),
                ('menu_lunch_item5_price', models.IntegerField()),
                ('menu_lunch_item6_img', models.ImageField(upload_to='img/%y')),
                ('menu_lunch_item6_name', models.CharField(max_length=150)),
                ('menu_lunch_item6_description', models.CharField(max_length=255)),
                ('menu_lunch_item6_price', models.IntegerField()),
                ('menu_lunch_item7_img', models.ImageField(upload_to='img/%y')),
                ('menu_lunch_item7_name', models.CharField(max_length=150)),
                ('menu_lunch_item7_description', models.CharField(max_length=255)),
                ('menu_lunch_item7_price', models.IntegerField()),
                ('menu_lunch_item8_img', models.ImageField(upload_to='img/%y')),
                ('menu_lunch_item8_name', models.CharField(max_length=150)),
                ('menu_lunch_item8_description', models.CharField(max_length=255)),
                ('menu_lunch_item8_price', models.IntegerField()),
                ('menu_dinner_item1_img', models.ImageField(upload_to='img/%y')),
                ('menu_dinner_item1_name', models.CharField(max_length=150)),
                ('menu_dinner_item1_description', models.CharField(max_length=255)),
                ('menu_dinner_item1_price', models.IntegerField()),
                ('menu_dinner_item2_img', models.ImageField(upload_to='img/%y')),
                ('menu_dinner_item2_name', models.CharField(max_length=150)),
                ('menu_dinner_item2_description', models.CharField(max_length=255)),
                ('menu_dinner_item2_price', models.IntegerField()),
                ('menu_dinner_item3_img', models.ImageField(upload_to='img/%y')),
                ('menu_dinner_item3_name', models.CharField(max_length=150)),
                ('menu_dinner_item3_description', models.CharField(max_length=255)),
                ('menu_dinner_item3_price', models.IntegerField()),
                ('menu_dinner_item4_img', models.ImageField(upload_to='img/%y')),
                ('menu_dinner_item4_name', models.CharField(max_length=150)),
                ('menu_dinner_item4_description', models.CharField(max_length=255)),
                ('menu_dinner_item4_price', models.IntegerField()),
                ('menu_dinner_item5_img', models.ImageField(upload_to='img/%y')),
                ('menu_dinner_item5_name', models.CharField(max_length=150)),
                ('menu_dinner_item5_description', models.CharField(max_length=255)),
                ('menu_dinner_item5_price', models.IntegerField()),
                ('menu_dinner_item6_img', models.ImageField(upload_to='img/%y')),
                ('menu_dinner_item6_name', models.CharField(max_length=150)),
                ('menu_dinner_item6_description', models.CharField(max_length=255)),
                ('menu_dinner_item6_price', models.IntegerField()),
                ('menu_dinner_item7_img', models.ImageField(upload_to='img/%y')),
                ('menu_dinner_item7_name', models.CharField(max_length=150)),
                ('menu_dinner_item7_description', models.CharField(max_length=255)),
                ('menu_dinner_item7_price', models.IntegerField()),
                ('menu_dinner_item8_img', models.ImageField(upload_to='img/%y')),
                ('menu_dinner_item8_name', models.CharField(max_length=150)),
                ('menu_dinner_item8_description', models.CharField(max_length=255)),
                ('menu_dinner_item8_price', models.IntegerField()),
            ],
        ),
    ]
