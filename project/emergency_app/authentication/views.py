from django.shortcuts import render
from rest_framework import permissions, viewsets, status, views
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from authentication.models import AuthUser
from authentication.serializers import AccountSerializer
from authentication.permissions import IsAccountOwnerOrSupperUser, IsAccountOwner
import json

# Create your views here.
class AccountViewSet(viewsets.ModelViewSet):
	'''
	:param: viewsets.ModelViewSet - extend rest_framework viewset
	:model: input datatable
	:lookup_field: key
	:queryset: input
	:serializer_class: method to serialize
	:permission_classes: use list of permission
	'''	
	model = AuthUser
	lookup_field = 'username'
	queryset = AuthUser.objects.all()
	serializer_class = AccountSerializer
	permission_classes = (permissions.IsAuthenticated, IsAccountOwnerOrSupperUser)

	def get_queryset(self):
		'''
		:desc: only supper user can see all
		'''	
		queryset = super(AccountViewSet, self).get_queryset()
		if (self.request.user.is_staff): return queryset
		queryset = queryset.filter(username=self.request.user)
		return queryset


class LoginView(views.APIView):
	'''
	:param: views.APIView - extend rest_framework views
	:desc: control login
	'''
	def post(self, request, format=None):
		'''
		:desc: handle post
		:username: get from request
		:password: get from request
		:account: call authenticate function from django
		:return: Response - response from API
		'''
		data = json.loads(request.body)
		username = data.get('username', None)
		password = data.get('password', None)

		account = authenticate(username=username, password=password)
		if account is not None:
			if account.is_active:
				login(request, account)

				serialized = AccountSerializer(account)
				return Response(serialized.data)
			else:
				return Response({
					'status': 'Unauthorized',
					'message': 'Username/password combination invalid.'
					}, status=status.HTTP_401_UNAUTHORIZED)
		else:
				return Response({
				    'status': 'Unauthorized',
				    'message': 'Username/password combination invalid.'
				}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(views.APIView):
	'''
	:param: views.APIView - extend rest_framework views
	:desc: control logout
	'''
	permission_classes = (permissions.IsAuthenticated,)

	def post(self, request, format=None):
		'''
		:desc: handle post
		:logout: call logout function from django
		:return: Response - response from API
		'''
		logout(request)

		return Response({}, status=status.HTTP_204_NO_CONTENT)
