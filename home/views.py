from django.shortcuts import render
from .forms import ContactForm
from .models import Teacher

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid:
            form.save()
            form = ContactForm()
    else:
        form = ContactForm()

    context = {
        'form': form
    }

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html' )

def teacher(request):
    teacher = Teacher.objects.all()
    context = {
        'teachers': teacher,
    }
    return render(request, 'teacher.html', context)

# Create your views here.
