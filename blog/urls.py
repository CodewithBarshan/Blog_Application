from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),  # Added name='home' for URL reversal
    path('blog/<slug:url>/', views.post_detail, name='post_detail'),  # Added name='post_detail' for URL reversal
    path('category/<slug:url>/', views.category_detail, name='category_detail'),  # Added name='category_detail' for URL reversal
    path('about', views.about, name='about'),
]

# Add this line to serve media files during development
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
