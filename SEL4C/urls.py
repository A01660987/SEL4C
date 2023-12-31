from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers
from rest_framework_extensions.routers import ExtendedSimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from SEL4C.views import *

router: ExtendedSimpleRouter = ExtendedSimpleRouter()

router = routers.DefaultRouter()
# router.register(r'user', UserViewSet)
router.register(r'student', StudentViewSet)
router.register(r'institution', InstitutionViewSet)
router.register(r'degree', DegreeViewSet)
router.register(r'discipline', DisciplineViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/upload/', FileUploadView.as_view(), name='upload'),
    path('api/answer/', AnswerViewSet.as_view(), name='answer'),
    path('api/schema/', SpectacularAPIView.as_view(api_version='v2'), name='schema'),
    path('schema/swagger/', SpectacularSwaggerView.as_view()), 
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/change-email/', ChangeEmailView.as_view(), name='change-email'), 
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    # path('token/verify/', TokenVerifyView.as_view(), name='token_refresh'), 
    path('api/', include(router.urls)), 
    path('', include('web.urls'))
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Include file view in browser when DEBUG=TRUE
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)