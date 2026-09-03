import os
from django.core.management.base import BaseCommand, CommandError
from apps.users.models import Department, User


class Command(BaseCommand):
    help = 'Create or update the configured system administrator idempotently.'

    def handle(self, *args, **options):
        name = os.getenv('ADMIN_NAME')
        password = os.getenv('ADMIN_PASSWORD')
        if not name or not password:
            raise CommandError('ADMIN_NAME and ADMIN_PASSWORD must be set in the environment')
        department = Department.objects.filter(name='领导班子', is_deleted=False).first()
        if not department:
            raise CommandError('Department 领导班子 does not exist')
        user = User.objects.filter(name=name).first()
        if user:
            user.set_password(password)
            user.is_system_admin = True; user.account_status = 'enabled'; user.register_status = 'approved'; user.is_deleted = False; user.department_id = department.id
            user.save(update_fields=['password_hash','is_system_admin','account_status','register_status','is_deleted','department_id','updated_at'])
            self.stdout.write(self.style.SUCCESS('Administrator already exists; updated safely.'))
            return
        User.objects.create_user(name=name, password=password, position='general_manager', department_id=department.id, job_title='系统管理员', responsibility=None, is_system_admin=True, account_status='enabled', register_status='approved', is_deleted=False)
        self.stdout.write(self.style.SUCCESS('Administrator created.'))
