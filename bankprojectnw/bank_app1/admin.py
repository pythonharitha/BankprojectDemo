from django.contrib import admin

# Register your models here.
from bank_app1.models import District, Branch, Customer, Account_type

admin.site.register(District)
admin.site.register(Branch)
admin.site.register(Customer)
admin.site.register(Account_type)
