from django.contrib import admin
from .models import HeadingsAndDescription
from .models import RotatingImageInLandingPage
from .models import LadningPageServices
from .models import LandingPageAboutUsSection
from .models import LandingPageTestimonial
from .models import LandingPageTestimonialHeadings
from .models import FooterDetails
from .models import LandingPageMenuHeadings
from .models import LandingPageMenuBreakfast
from .models import LandingPageMenuLunch
from .models import LandingPageMenuDinner
from .models import ThreeDImage
from .models import GalleryImage

class HeadingsAndDescriptionsAdmin(admin.ModelAdmin):
    list_display = ('headingOne','headingTwo','description')

class RotatingImageInLandingPageAdmin(admin.ModelAdmin):
    list_display = ('backgroundImage','caption',)

class LadningPageServicesAdmin(admin.ModelAdmin):
    list_display = ('icon','service','description',)

class LandingPageAboutUsSectionAdmin(admin.ModelAdmin):
    list_display = ('about_text','welcome_text','restaurant_name','img1','img2','img3','img4','description_1','description_2','counter1_num','counter1_text1',
                    'counter1_text2','counter2_num','counter2_text1','counter2_text2','button_text','button_link')
class LandingPageTestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name','client_profession','client_comment','client_image',)

class LandingPageTestimonialHeadingsAdmin(admin.ModelAdmin):
    list_display = ('testimonial_text','testimonial_description',)

class FooterDetailsAdmin(admin.ModelAdmin):
    list_display = ('company_name','contact_text','address','phone','email','facebook_link','instagram_link','opening_text','days_list_one',
                    'timing_days_list_one','days_list_two','timing_days_list_two','location',)
    
class LandingPageMenuHeadingsAdmin(admin.ModelAdmin):
    list_display = ('menu_text','menu_heading','menu_breakfast_description','menu_breakfast_text','menu_lunch_description','menu_lunch_text',
                    'menu_dinner_description','menu_dinner_text',)
    
class LandingPageMenuBreakfastAdmin(admin.ModelAdmin):
    list_display = ('menu_breakfast_item_name','menu_breakfast_item_description','menu_breakfast_item_price','menu_breakfast_item_img',)

class LandingPageMenuLunchAdmin(admin.ModelAdmin):
    list_display = ('menu_breakfast_item_name','menu_breakfast_item_description','menu_breakfast_item_price','menu_breakfast_item_img',)

class LandingPageMenuDinnerAdmin(admin.ModelAdmin):
    list_display = ('menu_breakfast_item_name','menu_breakfast_item_description','menu_breakfast_item_price','menu_breakfast_item_img',)

class ThreeDImageAdmin(admin.ModelAdmin):
    list_display = ('object_description','object_file')

class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('gallery_image_heading','gallery_image_description','gallery_image',)

# Register your models here.

admin.site.register(HeadingsAndDescription,HeadingsAndDescriptionsAdmin)
admin.site.register(RotatingImageInLandingPage,RotatingImageInLandingPageAdmin)
admin.site.register(LadningPageServices,LadningPageServicesAdmin)
admin.site.register(LandingPageAboutUsSection,LandingPageAboutUsSectionAdmin)
admin.site.register(LandingPageTestimonial,LandingPageTestimonialAdmin)
admin.site.register(LandingPageTestimonialHeadings,LandingPageTestimonialHeadingsAdmin)
admin.site.register(FooterDetails,FooterDetailsAdmin)
admin.site.register(LandingPageMenuHeadings,LandingPageMenuHeadingsAdmin)
admin.site.register(LandingPageMenuBreakfast,LandingPageMenuBreakfastAdmin)
admin.site.register(LandingPageMenuLunch,LandingPageMenuLunchAdmin)
admin.site.register(LandingPageMenuDinner,LandingPageMenuDinnerAdmin)
admin.site.register(ThreeDImage,ThreeDImageAdmin)
admin.site.register(GalleryImage,GalleryImageAdmin)