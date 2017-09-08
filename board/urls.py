from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'sprints', views.SprintViewSet, base_name='sprints')
router.register(r'tasks', views.TaskViewSet, base_name='tasks')
router.register(r'user', views.UserViewSet, base_name='user')
