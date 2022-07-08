from django.urls import include, path
from django.conf.urls.static import static
from rest_framework import routers
from auth import views as auth_views
from gallery import views as gallery_views
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'gallery', gallery_views.ImagesViewSet, basename='gallery')
urlpatterns = [
                  path('api/', include(router.urls)),
                  path('api/login', auth_views.LoginView.as_view()),
                  path('api/logout', auth_views.LogoutView.as_view()),
                  path('api/register', auth_views.RegisterView.as_view()),
                  path('api/user', auth_views.GetUserView.as_view()),
                  path('api/remove_all', gallery_views.RemoveAllView.as_view())
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
