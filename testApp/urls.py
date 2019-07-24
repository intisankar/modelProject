from django.conf.urls import url,include
from django.conf import settings
from testApp import views
urlpatterns = [
    url(r'^test/',views.empdata),
    url(r'^testform/',views.form_view),
    url(r'^testpage/',views.empty_page,name='testpage'),
    url(r'^register',views.register,name='register'),
    url(r'^user_login',views.user_login,name='user_login'),
    url(r'^special',views.special,name='special')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url('^__debug__/',include(debug_toolbar.urls))
    ] + urlpatterns
