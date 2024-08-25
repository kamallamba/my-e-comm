from django.urls import  path
from mystore import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.home,name="home"),
    path("category/<slug:val>/",views.categoryViews.as_view(),name="category"),
    path("detail/<int:id>/",views.product_detail.as_view(),name="product_details"),
    path('categorytitle/<slug:val>',views.Categorytitle.as_view(),name='category-title'),
    path('aboutus/',views.aboutus.as_view(),name='aboutus'),
    path('contactus/',views.contactus.as_view(),name='contactus'),

    #add to cart
    path('AddtoCart/<int:id>/',views.add_to_cart,name='Cart'),
    path('Showcart/',views.showcart,name='Showcart'),

    #Registration form 
    path('Registration/',views.Signup.as_view(), name='Registration'),
    path('Login/', views.user_Login.as_view(),name='Login'),
    path('Logout/',views.Logout.as_view(),name="Logout"),
    path('details/',views.Customerdetails.as_view(),name="details"),
    path('address/',views.address,name='address'),
    path("update/<int:pk>/",views.update.as_view(),name="update"),
    path('changepassword/',views.changepass,name="changepassword"),

    path('plusitem/<int:id>/',views.plusitem,name='plusitem'),
    path('minusitem/<int:id>/',views.minusitem,name='minusitem'),
    path('remove/<int:id>',views.remove,name='remove'),
    path('checkout/',views.checkout,name='checkout'),
    
]+static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

