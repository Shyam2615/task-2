from django.contrib import admin
from django.urls import path
from home.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('register/', register),
    path('login/', login_page),
    path('dashboard/', dashboard),
    path('blog/', blog),
    path('create-blog/', create_blog),
    path('drafts/', drafts_page),
    path('upload_post/<int:draft_id>/', upload_post, name='upload_post'),
    path('delete_post/<int:draft_id>/', delete_post, name='delete_post'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
