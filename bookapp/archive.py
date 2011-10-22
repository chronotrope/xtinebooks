# Create your views here.
{% for post in posts % }
<h2>{{post. book_title}}</h2>
<p>{{post.timestamp}}</p>
<p>{{post.book_desc}}</p>
{% endfor %}
