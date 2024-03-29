from django.contrib import admin
from sign.models import Event, Guest
# # Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'address', 'start_time']
    search_fields = ['name']  # 搜索栏
    list_filter = ['status']  # 过滤器


class GuestAdmin(admin.ModelAdmin):
    list_display = ['real_name', 'phone', 'email', 'sign', 'creat_time', 'event']
    search_fields = ['real_name', 'phone']
    list_filter = ['sign']
# admin.site.register(Event)
# admin.site.register(Guest)


admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)

