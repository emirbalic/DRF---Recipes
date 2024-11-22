# from django.urls import path, include

from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, RecipeViewSet, TagViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet, basename='recipe')
# router.register(r'recipes', CategoryViewSet, basename='recipe')
router.register(r'categories', CategoryViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = router.urls


# urlpatterns = [
#     path('recipes/', include(router.urls)),
# ]


# from django.urls import include, path

# from reporting.views import OrderViewSet, ReportingViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('orders', OrderViewSet, basename='orders')

# urlpatterns = [
#     path('reporting/', ReportingViewSet.as_view(), name='reporting'),

#     path('', include(router.urls))
  
# ]
