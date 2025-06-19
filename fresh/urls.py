from django.urls import path
from django.views.generic import TemplateView

app_name = 'fresh'

urlpatterns = [
    path('', TemplateView.as_view(template_name='fresh/index.html')),
    
]