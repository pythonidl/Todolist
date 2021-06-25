from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from. import views

urlpatterns=[
        path('',views.home,name='home'),
         path('delete/<int:taskid>/',views.delete,name='delete'),
         path('update/<int:taskid>/',views.update,name='update'),
         path('taskview/', views.taskview.as_view(), name='taskview'),
         path('detailview/<int:pk>/', views.detailview.as_view(), name='detailview'),
        path('updateview/<int:pk>/', views.updateview.as_view(), name='updateview'),
    path('deleteview/<int:pk>/', views.deleteview.as_view(), name='deleteview')

]
urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

