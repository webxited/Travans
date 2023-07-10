from django.shortcuts import render
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
#from django.http import HttpResponse

# Create your views here.

def index(request):
    headingsAndDescription = HeadingsAndDescription.objects.all()
    rotatingImageInLandingPage = RotatingImageInLandingPage.objects.all()
    services = LadningPageServices.objects.all()
    aboutUs = LandingPageAboutUsSection.objects.all()
    testimonial = LandingPageTestimonial.objects.all()
    testimonial_heading = LandingPageTestimonialHeadings.objects.all()
    footer = FooterDetails.objects.all()
    menu_heading = LandingPageMenuHeadings.objects.all()
    menu_breakfast = LandingPageMenuBreakfast.objects.all()
    menu_lunch  = LandingPageMenuLunch.objects.all()
    menu_dinner = LandingPageMenuDinner.objects.all()
    threeD = ThreeDImage.objects.all()
    return render(request, 'index.html',{
        'headingsAndDescription':headingsAndDescription,
        'rotatingImageInLandingPage':rotatingImageInLandingPage,
        'services':services,
        'aboutUs':aboutUs,
        'testimonial' : testimonial,
        'testimonial_heading' : testimonial_heading,
        'footer' : footer,
        'menu_heading' : menu_heading,
        'menu_breakfast' : menu_breakfast,
        'menu_lunch' : menu_lunch,
        'menu_dinner' : menu_dinner,
        'threeD' : threeD
        })

def about(request):
    headingsAndDescription = HeadingsAndDescription.objects.all()
    aboutUs = LandingPageAboutUsSection.objects.all()
    footer = FooterDetails.objects.all()
    return render(request,'about.html',{
        'headingsAndDescription':headingsAndDescription,
        'aboutUs':aboutUs,
        'footer' : footer,
        })

def services(request):
    headingsAndDescription = HeadingsAndDescription.objects.all()
    services = LadningPageServices.objects.all()
    footer = FooterDetails.objects.all()
    return render(request,'services.html',{
        'headingsAndDescription':headingsAndDescription,
        'services':services,
        'footer' : footer,
        })

def menu(request):
    headingsAndDescription = HeadingsAndDescription.objects.all()
    menu_heading = LandingPageMenuHeadings.objects.all()
    menu_breakfast = LandingPageMenuBreakfast.objects.all()
    menu_lunch  = LandingPageMenuLunch.objects.all()
    menu_dinner = LandingPageMenuDinner.objects.all()
    footer = FooterDetails.objects.all()
    return render(request,'menu.html',{
        'headingsAndDescription':headingsAndDescription,
        'menu_heading' : menu_heading,
        'menu_breakfast' : menu_breakfast,
        'menu_lunch' : menu_lunch,
        'menu_dinner' : menu_dinner,
        'footer' : footer,
        })

def testimonials(request):
    headingsAndDescription = HeadingsAndDescription.objects.all()
    testimonial = LandingPageTestimonial.objects.all()
    testimonial_heading = LandingPageTestimonialHeadings.objects.all()
    footer = FooterDetails.objects.all()
    return render(request,'testimonials.html',{
        'headingsAndDescription':headingsAndDescription,
        'testimonial' : testimonial,
        'testimonial_heading' : testimonial_heading,
        'footer' : footer,
        })

def gallery(request):
    headingsAndDescription = HeadingsAndDescription.objects.all()
    gallery = GalleryImage.objects.all()
    footer = FooterDetails.objects.all()
    return render(request,'gallery.html',{
        'headingsAndDescription':headingsAndDescription,
        'gallery':gallery,
        'footer' : footer,
        })

#return HttpResponse("<h1>Welcome</h1>")