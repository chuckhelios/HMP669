"""
Authentication serializers are used to make flat database to JSON format.

1. **AccountSerializer** 
----
"""

from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers
from authentication.models import AuthUser

class AccountSerializer(serializers.ModelSerializer):

	class Meta:
		model = AuthUser
		