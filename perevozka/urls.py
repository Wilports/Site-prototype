
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path("", index, name ="Home"),
    path("order_page/", orders, name="Orders"),
    path("News/", NewsHome.as_view(), name="news"),
    path('News/<str:slug>/', NewsDetailView.as_view(), name="post"),
    path("Comments", comments, name="Comments"),
    path("thanks", thanks, name = 'thanks'),
    path("Pays", pays, name = 'Pays'),
    path("Trucks", trucks, name = 'Trucks'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
