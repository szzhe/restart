from django.contrib import admin
from sign.models import Event, Guest

class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'start_time','id']
    search_fields = ['name'] #搜索栏
    list_filter = ['status'] #过滤器

class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone','email','sign','create_time','event']
    search_fields = ['realname','phone'] #搜索栏
    list_filter = ['sign'] #过滤器

# 通知admin 管理工具为这些模块逐一提供界面
admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)