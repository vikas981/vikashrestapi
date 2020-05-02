from django.urls import path, include
from .views import test_list, test_detail, TestAPIView, TestDetails, GenericApiView, TestViewSet,UserAuthentication
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('test', TestViewSet, basename='test')

urlpatterns = [
    path('', include(router.urls)),
    path('/<int:pk>/', include(router.urls)),
    #path('test/', TestAPIView.as_view()),
    path('api/auth/',UserAuthentication.as_view()),
    path('detail/<int:pk>/', test_detail),
    path('detail/<int:id>/', TestDetails.as_view()),
    path('test/<int:id>/', GenericApiView.as_view()),

]
