# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse
from xtinebooks.bookapp.models import BookPost

def archive(request):
    posts = BookPost.objects.all()
    t = loader.get_template("archive.html")
    c = Context({ 'posts': posts })
    return HttpResponse(t.render(c))