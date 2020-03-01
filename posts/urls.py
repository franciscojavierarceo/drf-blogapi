from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import PostViewSet 
# from .views import PostList, PostDetail

router = SimpleRouter()
router.register('', PostViewSet, base_name='posts')

urlpatterns = [
    # path('<int:pk>/', PostDetail.as_view()),
    # path('', PostList.as_view()),
    path('', include(router.urls))
]

#urlpatterns += router.urls