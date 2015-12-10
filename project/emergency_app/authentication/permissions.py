"""
Authentication permissions are used to decicde permission level.

1. **IsAccountOwner** - check is account owner
2. **IsAccountOwnerOrSupperUser** - check if login user are authenticated to view the patient or not, except supper user (current use).
3. **IsPatientAssignedOrSupperUser** - (no longer use)

----
"""

from rest_framework import permissions

class IsAccountOwner(permissions.BasePermission):
	'''
	:desc: extent the BasePermission
	'''
	def has_object_permission(self, request, view, account):
		'''
		:desc: override the function - compare request username with account name 

		:return: boolean
		'''
		if request.user:
			return account == request.user
		return False

class IsAccountOwnerOrSupperUser(permissions.BasePermission):
	'''
	:desc: extent the BasePermission
	'''
	def has_object_permission(self, request, view, obj):
		'''
		:desc: override the function - 

				1). check if supper user

				2). compare request username with account name 

		:return: boolean
		'''
		if request.user:
			if request.user.is_staff:
				return True
			else:
				if hasattr(obj, 'user_id'):
					print 'user_id'
					return obj.user_id == request.user.username
				elif hasattr(obj, 'username'):
					print 'username'
					return obj.username == request.user.username
		return False


class IsPatientAssignedOrSupperUser(permissions.BasePermission):
	def has_object_permission(self, request, view, obj):
		if request.user:
			if request.user.is_staff:
				return True
			else:
				try:
					reviewer = obj.user.username
					return reviewer == request.user.username
				except:
					return False
		return False