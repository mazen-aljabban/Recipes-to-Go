from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('chef', views.ChefViewSet)
router.register('collections', views.CollectionViewSet)
router.register('catagorys', views.CategoryViewSet)
router.register('ingredients', views.IngredientViewSet)


urlpatterns = router.urls
