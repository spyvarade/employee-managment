from django.shortcuts import render
from django.http import Http404
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import filters

from .models import Employee
from .serializers import EmployeeSerializer
from .tasks import send_welcome_email_to_employee


class EmployeeListCreateView(APIView):
	""" 
	List all employee , or create a new employee
	"""

	# permission_classes = [IsAuthenticated]


	def get(self, request, format=None):
		"""
			Retirive all Employee List ordered by first_name
		"""
		employee = Employee.objects.all()

		if request.query_params:
			#get search query param from urls
			search = request.query_params.get('search')
			#filter with first_name and last_name of employee
			employee = Employee.objects.filter(Q(first_name__icontains=search) | Q(last_name__icontains=search))

		serializer = EmployeeSerializer(employee, many=True)
		return Response(serializer.data)

	def post(self, request, fromat=None):
		"""
			Create Employee
		"""
		serializer = EmployeeSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			# Sending mail using celery and redis 
			# function is define in employee.tasks.py file 
			send_welcome_email_to_employee.delay('spyvarade@gmail.com')

			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class EmployeeRetrieveUpdateDeleteView(APIView):
	"""
		Retrieve, Update, or delete  EmployeeView
	"""

	permission_classes = [IsAuthenticated]


	def get_object(self, pk):
		"""
			Check if primary key is exsit or not 
		"""
		try: 
			return  Employee.objects.get(pk=pk)
		except Employee.DoseNotExist:
			return Http404

	def get(self, request, pk, format=None):
		"""
			Retitive employee 
		"""
		employee = self.get_object(pk)
		serializer = EmployeeSerializer(employee)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		"""
			Update Employee 
		"""
		employee = self.get_object(pk)
		serializer  = EmployeeSerializer(employee, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.error, status=status.HTTP_404_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		"""
			Delete Employee 
		"""
		employee = self.get_object(pk)
		employee.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


