from django.urls import path
from .views import(RegisterAPI,LoginAPI, allUserDB, deleteUser,
                   filterMitre, filterCaja, filterMozo, deleteUser, modifyUser)
from knox import views as knox_views

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    #FILTRADO DE ROLES:
    path('api/allUser/', allUserDB),
    path('api/allMitre/', filterMitre),
    path('api/allMozo/', filterMozo),
    path('api/allCaja/', filterCaja),
    #DELETE, AGREGAR, MODIFICAR:
    path('api/deleteUser/', deleteUser),
    path('api/modifyUser/', modifyUser),
    
]

