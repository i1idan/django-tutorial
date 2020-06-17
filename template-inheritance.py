## create bas.html file type following codes:


<!-- <h1> Hellow World</h1>
{{request.user}}
<p> This is a template </p>-->
<!doctype html>
<html>
<head>
	<title> coding for Enterprenures id doing try Django</title> 
	<h1> This a nav bar </h1>
</head>
<body>
     {% block content %}
       replace me
     {% endblock %}
    </body>
</html>



## make this changes to your other template page files:



home.html 



{% extends "base.html" %}

{%block content%}

  <h1> Hellow World</h1>

  <p> This is a template </p>

{% endblock %}


contact.html



{% extends "base.html" %}

{% block content %}

 <h1> Contact </h1>
 <p> This is a template </p>

{% endblock %}


about.html




{% extends "base.html" %}

{%block content%}

  <h1> About </h1>

  <p> This is a template </p>

{% endblock %}



