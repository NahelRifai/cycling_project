from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from posts import views as post_views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^posts/', include('posts.urls')),
    url(r'^about/$',views.about),
    url(r'^$',post_views.post_list,name='home'),
    url(r'^accounts/',include('accounts.urls'))

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
