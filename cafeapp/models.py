from django.db import models

# Create your models here.
class HeadingsAndDescription(models.Model):
    headingOne = models.CharField(max_length=1000)
    headingTwo = models.CharField(max_length=1000)
    description = models.CharField(max_length=2500)

class RotatingImageInLandingPage(models.Model):
    caption = models.CharField(max_length=255)
    backgroundImage = models.ImageField(upload_to="img/%y")

class LadningPageServices(models.Model):
    icon = models.CharField(max_length=255)
    service = models.CharField(max_length=255)
    description = models.CharField(max_length=500)

class LandingPageAboutUsSection(models.Model):
    about_text = models.CharField(max_length=20)
    welcome_text = models.CharField(max_length=20)
    restaurant_name = models.CharField(max_length=20)
    img1 = models.ImageField(upload_to="img/%y")
    img2 = models.ImageField(upload_to="img/%y")
    img3 = models.ImageField(upload_to="img/%y")
    img4 = models.ImageField(upload_to="img/%y")
    description_1 = models.CharField(max_length=1000)
    description_2 = models.CharField(max_length=1000)
    counter1_num = models.IntegerField()
    counter1_text1 = models.CharField(max_length=20)
    counter1_text2 = models.CharField(max_length=20)
    counter2_num = models.IntegerField()
    counter2_text1 = models.CharField(max_length=20)
    counter2_text2 = models.CharField(max_length=20)
    button_text = models.CharField(max_length=20)
    button_link = models.CharField(max_length=2500)

class LandingPageMenuHeadings(models.Model):
    menu_text = models.CharField(max_length=20)
    menu_heading = models.CharField(max_length=100)
    menu_breakfast_description = models.CharField(max_length=20)
    menu_breakfast_text = models.CharField(max_length=20)
    menu_lunch_description = models.CharField(max_length=20)
    menu_lunch_text = models.CharField(max_length=20)
    menu_dinner_description = models.CharField(max_length=20)
    menu_dinner_text = models.CharField(max_length=20)

class LandingPageMenuBreakfast(models.Model):
    menu_breakfast_item_name = models.CharField(max_length=150)
    menu_breakfast_item_description = models.CharField(max_length=255)
    menu_breakfast_item_price = models.IntegerField()
    menu_breakfast_item_img = models.ImageField(upload_to="img/%y")
    
class LandingPageMenuLunch(models.Model):
    menu_breakfast_item_name = models.CharField(max_length=150)
    menu_breakfast_item_description = models.CharField(max_length=255)
    menu_breakfast_item_price = models.IntegerField()
    menu_breakfast_item_img = models.ImageField(upload_to="img/%y")
    
class LandingPageMenuDinner(models.Model):
    menu_breakfast_item_name = models.CharField(max_length=150)
    menu_breakfast_item_description = models.CharField(max_length=255)
    menu_breakfast_item_price = models.IntegerField()
    menu_breakfast_item_img = models.ImageField(upload_to="img/%y")

class LandingPageTestimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_profession = models.CharField(max_length=100)
    client_comment = models.CharField(max_length=1000)
    client_image = models.ImageField(upload_to="img/%y")

class LandingPageTestimonialHeadings(models.Model):
    testimonial_text = models.CharField(max_length=30)
    testimonial_description = models.CharField(max_length=100)

class FooterDetails(models.Model):
    company_name = models.CharField(max_length=255)
    contact_text = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=255)
    facebook_link = models.CharField(max_length=1000)
    instagram_link = models.CharField(max_length=1000)
    opening_text = models.CharField(max_length=20)
    days_list_one = models.CharField(max_length=255)
    timing_days_list_one = models.CharField(max_length=255)
    days_list_two = models.CharField(max_length=255)
    timing_days_list_two = models.CharField(max_length=255)
    location = models.CharField(max_length=2500)

class ThreeDImage(models.Model):
    object_description = models.CharField(max_length=100)
    object_file = models.FileField(upload_to="img/%y")

class GalleryImage(models.Model):
    gallery_image_heading = models.CharField(max_length=50)
    gallery_image_description = models.CharField(max_length=255)
    gallery_image = models.ImageField(upload_to="img/%y")
