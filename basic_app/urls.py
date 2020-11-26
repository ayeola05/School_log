from django.urls import path
from basic_app import views
from django.conf import settings
from django.conf.urls.static import static




app_name = 'basic_app'

urlpatterns = [
	path('', views.HomeView.as_view(), name='home'),
	path('list/', views.ProfileListView.as_view(), name='list'),
	path('detail/<int:pk>/', views.ProfileDetailView.as_view(), name='detail'),
	path('create/', views.ProfileCreateView.as_view(), name='create'),
	path('update/<int:pk>/', views.ProfileUpdateView.as_view(), name='update'),
	path('delete/<int:pk>/',views.ProfileDeleteView.as_view(), name='delete')
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

