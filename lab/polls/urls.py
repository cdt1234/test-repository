from django.urls import path

from . import views

urlpatterns = [
    path('1234/', views.index, name='index'),
    path('main/',views.main),
    path('main/render/',views.rende),
    path('main/biao/',views.biao),
    path('main/tiao',views.tiao),
    path('main/bing',views.bing),
    path('main/data',views.data)
    # path('main/render/',views.render)
]