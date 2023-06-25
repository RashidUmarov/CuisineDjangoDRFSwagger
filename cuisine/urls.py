from rest_framework import routers
from .api import CategoryViewSet, DishViewSet

router=routers.DefaultRouter()
router.register('api/categories',CategoryViewSet,'categories')
router.register('api/dishes',DishViewSet,'dishes')

urlpatterns=router.urls