from django.contrib import admin
from .models import Parents, Children, Daycares, Clubs, Vouchers, ChildEnrollment

admin.site.register(Parents)
admin.site.register(Children)
admin.site.register(Daycares)
admin.site.register(Clubs)
admin.site.register(Vouchers)
admin.site.register(ChildEnrollment)
