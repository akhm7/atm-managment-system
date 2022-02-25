from django.contrib import admin

from crudapp.models import brokenCategory
from .models import Atm, AtmImage, AtmModel, AtmModelFunction, PCIPTS, Profile, telegramUser, serviceContract, ticket,brokenCategory

# Register your models here.

admin.site.register(AtmModelFunction)
admin.site.register(Atm)
admin.site.register(AtmImage)
admin.site.register(AtmModel)
admin.site.register(Profile)



#'broken', 'atm', 'user', 'dataCreated', 'dataClosed', 'status', 'operator', 'description', 'edited'
class serviceContractAdmin(admin.ModelAdmin):
    list_display=('company', 'name', 'type', 'amt', 'dataBegin', 'dataEnd')
    list_filter = ('company', 'type')
class ticketAdmin(admin.ModelAdmin):
    list_display=('atm', 'user', 'dataCreated', 'dataClosed', 'status', 'operator')
    list_filter = ('atm', 'user', 'status')

class PCIPTSAdmin(admin.ModelAdmin):
    list_display=('manufacturer_name', 'model_name', 'approval_number', 'version', 'approval_class', 'product_type', 'expiry_date', 'show')
    list_filter = ('approval_class', 'show', 'manufacturer_name')

class telegramUserAdmin(admin.ModelAdmin):
    list_display=('uid', 'mfo', 'name', 'status','stage')
    list_filter = ('mfo','status')
    readonly_fields = ('uid','json_info','stage',)
class brokenCategoryAdmin(admin.ModelAdmin):
    list_display=('title', 'description')

admin.site.register(PCIPTS, PCIPTSAdmin)
admin.site.register(serviceContract, serviceContractAdmin)
admin.site.register(ticket, ticketAdmin)
admin.site.register(brokenCategory,brokenCategoryAdmin)


admin.site.register(telegramUser, telegramUserAdmin)

