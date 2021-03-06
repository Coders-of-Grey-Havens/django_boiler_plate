from django.contrib import admin
from .models import Member
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm,UserLoginForm
class UserAdmin(BaseUserAdmin):
	add_form=UserCreationForm
	list_display=('username','email','is_admin',)
	list_filter=('is_admin',)
	fieldsets = (
			(None, {'fields': ('username','email','password')}),
			('Permissions', {'fields': ('is_admin',)})
		)
	search_fields = ('username','email')
	ordering = ('username','email')

	filter_horizontal = ()
admin.site.register(Member, UserAdmin)
admin.site.unregister(Group)
