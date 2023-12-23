from . import views
from django.urls import path
app_name='ecomapp'

urlpatterns = [
    # path('',views.home,name='home'),
    path('', views.allProductCategory, name='allProductCategory'),
    path('<slug:c_slug>/', views.allProductCategory, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='productCatdetail'),

]