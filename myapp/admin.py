from django.contrib import admin
from myapp.models import task
from django.contrib.auth.models import Permission
# Register your models here.


class taskAdmin(admin.ModelAdmin):
    llist_display = ('obj_project', 'parent_task', 'obj_user', 'uuid', 'type_task', 'name', 'overview',  'content', 'weight', 'token', 'period', 'gps_flag')


admin.site.register(Permission)


admin.site.register(task, taskAdmin)
