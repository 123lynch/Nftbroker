from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Index(TemplateView):
    template_name = 'major/index.html'

class Contact(TemplateView):
    template_name = 'major/contact.html'

class Explore(TemplateView):
    template_name = 'major/discover.html'

class Faq(TemplateView):
    template_name = 'major/how-it-works.html'

class News(TemplateView):
    template_name = 'major/news.html'

class ConnectWallet(TemplateView):
    template_name = 'major/connectwallet.html'