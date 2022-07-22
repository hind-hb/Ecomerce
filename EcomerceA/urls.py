from django.urls import path 
from EcomerceA.views import ListCategory , DetailCatgory ,  ListProduct , DetailProduct ,ProductListView


urlpatterns = [

    path('categories',ListCategory.as_view(),name='categories'),
    path('categories/<int:pk>/', DetailCatgory.as_view(),name='singelCategories'),
    path('product',ListProduct.as_view(),name='product'),
    path('product/<int:pk>/', DetailProduct.as_view(),name='singelproduct'),

    
   


 

]