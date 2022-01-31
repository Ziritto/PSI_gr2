from django.urls import path

from . import views

urlpatterns = [
    path('client/', views.Clientlist.as_view(), name='Client_list'),
    path('client/<int:pk>', views.ClientDetale.as_view(), name='Client_detale'),

    path('alcohol/', views.alcohollist.as_view(), name='alcohol_list'),
    path('alcohol/<int:pk>', views.alcoholDetale.as_view(), name='alcohol_detale'),

    path('alcoholCategory/', views.alcoholCategorylist.as_view(), name='alcoholCategory_list'),
    path('alcoholCategory/<int:pk>', views.alcoholCategoryDetale.as_view(), name='alcoholCategory_detale'),

    path('Order/', views.Orderlist.as_view(), name='Order_list'),
    path('Order/<int:pk>', views.OrderDetale.as_view(), name='Order_detale'),
]