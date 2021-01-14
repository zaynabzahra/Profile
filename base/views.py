from django.shortcuts import render

from django.core.mail import send_mail


# Create your views here.


def home(request):
    return render(request, 'base/home.html',)

def resume(request):
    return render(request, 'base/resume.html',)

def projects(request):
    return render(request, 'base/projects.html',)    

def contact(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        #send an email 
        send_mail(
            'Email From Contact Form from ' + name,
            message,
            email,
            ['zaynabzahra@googlemail.com'],
        )

        print(name)

        return render(request, 'base/contact.html',{'name':name})


    else:  
        return render(request, 'base/contact.html',)   


       
    