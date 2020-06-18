
views.py


from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home_view(request, *args, **kwargs):
	#return HttpResponse('<h1>Hello World</h1>')
     return render(request,"home.html",{})
     
def contact_view(request, *args, **kwargs):
	#return HttpResponse('<h1>Contact page</h1>')
	my_context = {
	     "my_text" : 'This is about us',  
	     "my_number" : "123"
	}
	return render(request,"contact.html", my_context)
	
def about_view(request, *args, **kwargs):
	#return HttpResponse('<h1>About page</h1>')
	my_context = {
	     "my_text" : 'This is about us',  
	     "my_number" : "123",
		 "my_list"	: [1, 2, 3] 
	}
	return render(request,"about.html", my_context)



about.html



{% extends "base.html" %}

{%block content%}

  <h1> About </h1>

  <p> This is a template </p>

<p>
{{ my_text }}, {{ my_number }},  {{ my_list }}
</p>

<ul>
    <li> Item 1 </li>
    <li>Item 2 </li>


</ul>


<ul>
{% for my_sub_item in my_list %}
<li>{{ my_sub_item }} </li>
{% endfor %}
</ul>

{% endblock %}





