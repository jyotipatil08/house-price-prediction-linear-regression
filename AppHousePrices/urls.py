from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('Admin_login/', views.Admin_login, name='Admin_login'),
    path('User_login/', views.User_login, name='User_login'),
    path('Register/', views.Register, name='Register'),
    path('ChangePassword/', views.ChangePassword, name='ChangePassword'),
    path('Analyze/', views.Analyze, name='Analyze'),
    path('WriteFeedback/', views.WriteFeedback, name='WriteFeedback'),
    path('ViewFeedback/', views.ViewFeedback, name='ViewFeedback'),
    path('ViewUser/', views.ViewUser, name='ViewUser'),
    path('AddTrainingData/', views.AddTrainingData, name='AddTrainingData'),
    path('ViewLocation/', views.ViewLocation, name='ViewLocation'),
    path('AddLocation/', views.AddLocation, name='AddLocation'),
    path('AddDensity/', views.AddDensity, name='AddDensity'),
    path('get_response/', views.get_response, name='get_response'),
    path('AddLandData/', views.AddLandData, name='AddLandData'),
    path('AnalyseLandPrice/', views.AnalyseLandPrice, name='AnalyseLandPrice'),
    path('get_response1/', views.get_response1, name='get_response1'),
    
]