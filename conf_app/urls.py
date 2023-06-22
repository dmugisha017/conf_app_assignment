
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # www.conference.rw/admin/
    path('admin/', admin.site.urls),
    path('speakers/',include('speaker.urls'))

]