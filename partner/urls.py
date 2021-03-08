from rest_framework import routers
from .views import *

router = routers.SimpleRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'partners', PartnerViewSet)

