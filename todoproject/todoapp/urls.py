from django.urls import path

from . import views
app_name='todoapp'

urlpatterns=[

    path('',views.homepage,name='homepage'),
    path('delete/<int:taskid>/',views.delete, name='delete'),
    path('update/<int:id>/',views.update,name='update')
    # path('detail/',views.detail,name='detail')
]