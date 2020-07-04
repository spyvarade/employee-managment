from django.urls import path

from .views import (
		EmployeeListCreateView,
		EmployeeRetrieveUpdateDeleteView,	
	)


urlpatterns = [
	path('',EmployeeListCreateView.as_view()),
    path('<int:pk>/',EmployeeRetrieveUpdateDeleteView.as_view()),
]