from django.conf.urls import include, url
from django.contrib import admin


from services.urls import router

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/',include(router.urls)),
]
