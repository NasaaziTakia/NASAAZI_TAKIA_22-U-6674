from django.urls import path,include,admin
from .views import moisuture_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myprojectapp.urls')),
]

