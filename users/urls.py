#write the urls here
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from users.forms import LoginForm
from . import views
from django.contrib.auth.views import LoginView
app_name = 'users'
urlpatterns = [
    #login and register Page
    path('', include('django.contrib.auth.urls')),
    #Login page urls for the webapp
    path('login/', LoginView.as_view(authentication_form = LoginForm), name = 'login'),
    #Logged out page urls for the webapp
    path("logged_out/", views.logged_out, name ='logged_out'),
    #Register page urls for the webapp
    path("register/", views.register, name = 'register'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
