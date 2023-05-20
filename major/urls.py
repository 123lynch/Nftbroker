from django.urls import path
from major import views

app_name = 'major'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('explore/', views.Explore.as_view(), name='explore'),
    path('faq/', views.Faq.as_view(), name='faq'),
    path('news/', views.News.as_view(), name='news'),
    path('connectwallet/', views.ConnectWallet.as_view(), name='connect'),
]