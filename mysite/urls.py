from django.contrib import admin
from django.urls import path, include
from .views import HomeView                           # !!!

urlpatterns = [
    path('', HomeView.as_view(), name='home'),    # !!!
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # !!!
    path('blog/', include('blog.urls')),
]
