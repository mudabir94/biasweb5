from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    url(r'^test/',views.test, name='test'),
    url(r'^ind/',views.ind, name='ind'),
    url(r'^on/',views.on, name='on'),
    url(r'^globalFunc/',views.globalFunc,name='gf'),
    
    url(r'^$',views.signup, name='signup'),
    
    url(r'^admin_setup/',views.admin_setup, name='admin_setup'),
    url(r'^signup/', views.signup, name='signup'), 
    url(r'^blog/', views.blogview.as_view(), name='blog'), 
    url(r'^mobile/',views.mobile_phone_view.as_view(),name='mobileview'),
    path('mobile_info/<int:id>',views.mobile_phone_view.one_mobile_func, name='mobileinfo'),
    url(r'^filter/',views.filter.as_view(), name='filter'),
    url(r'^showfilter/',views.showFilter.as_view(), name='showfilter'),
   
]
