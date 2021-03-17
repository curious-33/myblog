from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User

class CustomUserAdmin(UserAdmin):
    list_display = ['username','job','last_login']
    fieldsets = ( 
        ('Authentication Info', 
                {'fields': ('username','email','password')}), 
        ('Personal info', 
                {'fields': ('first_name', 'last_name','job','avatar')}),
        ('Contact links', 
                {'fields':('url','telegram','instagram','twitter')}),
        ('Important dates', 
                {'fields': ('last_login', 'date_joined')}),
        ('Permissions', 
                {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',
                                                        'user_permissions')}), 
                                                        )

admin.site.register(User,CustomUserAdmin)