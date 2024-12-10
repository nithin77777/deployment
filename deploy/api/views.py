from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer

class UserCRUSView(APIView):
    """
    View to perform Create, Retrieve, Update, and Search operations on CustomUser.
    """

    def get(self, request, pk=None):
        """
        Retrieve or search users. If a query parameter (e.g., username) is provided, perform a search.
        """
        # query = request.query_params.get('username', None)
        if pk:
            try:
                user = Employee.objects.get(pk=pk)
                serializer = EmployeeSerializer(user)
                return Response(serializer.data)
            except Employee.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Handle the case where no pk is provided, e.g., retrieve all users
            users = Employee.objects.all()
            serializer = EmployeeSerializer(users, many=True)
            return Response(serializer.data)

    def post(self, request):
        """
        Create a new user.
        """
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """
        Update an existing user. Requires the user ID (pk) in the request.
        """
        try:
            user = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
