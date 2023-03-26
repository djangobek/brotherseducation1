from django.contrib import messages
from django.core.mail import message
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect , HttpResponse
from .models import *
from django.views.generic import TemplateView, ListView
from .form import *
from django.template import loader
class Mainopen(TemplateView):
    template_name = 'index.html'
class Table(ListView):
    model = Post
    template_name = 'tablepupil.html'
    context_object_name = 'object_post'
class Starter(TemplateView):
    template_name = 'forms/form_my_form.html'

def blog_post(request):
    context = {}
    context['form'] = (BlogForm)
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Siz muvafaqiyatli Ro`yxatdan O`tdingiz')
            return redirect("maindir")
    else:
        form = BlogForm
    return render(request, 'forms/form_my_form.html' ,{'form':form})

def feedback_view(request):
    context = {}
    context['form'] = Feedbakform
    if request.method == 'POST':
        form = Feedbakform(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS , 'Izohingiz Uchun Rahmat')
            return redirect("kurslarim")
    else :
        form = Feedbakform
    return render(request, 'feedback.html' ,{'form':form})

def courseBar(request):
    return render(request,'index.html',{
        'x' : Course_data.objects.first(),
        'i': Course_data.objects.all()[1],
        'y': Course_data.objects.all()[2],
        'p': Course_item.objects.first(),
        'p1': Course_item.objects.all()[1],
        'p2': Course_item.objects.all()[2],
        'im1': Image_class.objects.first(),
        'im2': Image_class.objects.all()[1],
        'im3': Image_class.objects.all()[2],
        'im4': Image_class.objects.all()[3],
        'im5': Image_class.objects.all()[4],
        'im6': Image_class.objects.all()[5],
        'im7': Image_class.objects.all()[6],
        'im8': Image_class.objects.all()[7],
        'im9': Image_class.objects.all()[8],
        'us1': Mentorlar.objects.first(),
        'us2': Mentorlar.objects.all()[1],
        'us3': Mentorlar.objects.all()[2],
        'us4': Mentorlar.objects.all()[3],
    })

def Newfilebar(request):
    return render (request, 'index1.html',{
        'x' : Course_data.objects.first(),
        'i12': Course_data.objects.all()[1],
        'y': Course_data.objects.all()[2],
        'x1': Feedbacks.objects.first(),
        'x4': Feedbacks.objects.all()[1],
        'x3': Feedbacks.objects.all()[2],
        'x2' : Feedbacks.objects.last(),
        'i': Course_data.objects.all()[3],
        'i1' : Course_data.objects.all()[4],
        'i2' : Course_data.objects.all()[5],
        'i3' : Course_data.objects.all()[6]
    })  