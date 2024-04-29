from django.contrib import admin
from .models import Parent, Child, Daycare, Club, Voucher, ChildEnrollment
admin.site.register(Parent)
admin.site.register(Child)
admin.site.register(Daycare)
admin.site.register(Club)
admin.site.register(Voucher)
admin.site.register(ChildEnrollment)
