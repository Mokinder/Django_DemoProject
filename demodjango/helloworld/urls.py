from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name='Home'),
    path('product/',views.product_lists.as_view(),name='Products'),
    path('product/<int:pk>',views.product_detail.as_view(),name='product-detail'),
    path('product/add/',views.product_add.as_view(),name='product-add'),
    path('bill/add/',views.billgeneration,name='bill-add'),
    path('bill/sum/<int:pk>',views.calsum,name='calc-sum'),
    path('bill/<int:pk>',views.bill_detail.as_view(),name='bill-detail')
]
