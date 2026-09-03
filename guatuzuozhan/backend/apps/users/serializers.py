from django.utils import timezone
from rest_framework import serializers
from .models import Department, User

POSITIONS = {'general_manager', 'deputy_general_manager', 'section_chief', 'deputy_section_chief', 'team_leader', 'member'}

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name', 'code')

class UserSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    class Meta:
        model = User
        exclude = ('password_hash',)

class RegisterSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50, trim_whitespace=True)
    password = serializers.CharField(write_only=True, min_length=6)
    confirm_password = serializers.CharField(write_only=True)
    position = serializers.ChoiceField(choices=sorted(POSITIONS))
    department_id = serializers.IntegerField()
    job_title = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    responsibility = serializers.CharField(required=False, allow_blank=True, allow_null=True)

    def validate_name(self, value):
        if User.objects.filter(name=value, is_deleted=False).exists(): raise serializers.ValidationError('姓名已存在')
        return value
    def validate(self, data):
        if data['password'] != data['confirm_password']: raise serializers.ValidationError({'confirm_password': '两次密码不一致'})
        if not Department.objects.filter(id=data['department_id'], is_deleted=False, status=1).exists(): raise serializers.ValidationError({'department_id': '部门不存在或已停用'})
        data['job_title'] = data.get('job_title') or None
        return data

class LoginSerializer(serializers.Serializer):
    name = serializers.CharField()
    password = serializers.CharField(write_only=True)

class AdminUserWriteSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True, required=False, allow_blank=False)
    position = serializers.ChoiceField(choices=sorted(POSITIONS))
    department_id = serializers.IntegerField()
    job_title = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    responsibility = serializers.CharField(required=False, allow_blank=True, allow_null=True)
    is_system_admin = serializers.BooleanField(required=False, default=False)
    account_status = serializers.ChoiceField(choices=['enabled', 'disabled'], required=False, default='disabled')
    register_status = serializers.ChoiceField(choices=['pending', 'approved', 'rejected'], required=False, default='pending')

    def validate_department_id(self, value):
        if not Department.objects.filter(id=value, is_deleted=False).exists(): raise serializers.ValidationError('部门不存在')
        return value
