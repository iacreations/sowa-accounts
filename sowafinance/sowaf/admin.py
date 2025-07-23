from django.contrib import admin
from . models import Newcustomer,Newsupplier,Newclient,Newemployee,Newasset,Newinvoice,InvoiceItem
# Register your models here
admin.site.register(Newcustomer)
admin.site.register(Newsupplier)
admin.site.register(Newclient)
admin.site.register(Newemployee)
admin.site.register(Newasset)
admin.site.register(Newinvoice)
admin.site.register(InvoiceItem)