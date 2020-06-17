## create templates folder in src
## create your html files in templates folder

## exmaple file for home.html

<h1> Hellow World</h1>
<p> This is a template </p>


##  change views.py in pages app 


from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
	#return HttpResponse('<h1>Hello World</h1>')
     return render(request,"home.html",{})
     
def contact_view(request, *args, **kwargs):
	#return HttpResponse('<h1>Contact page</h1>')
	return render(request,"contact.html",{})
	
	     
def about_view(request, *args, **kwargs):
	#return HttpResponse('<h1>About page</h1>')
    return render(request,"about.html",{})



### change template directory in settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,"templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
