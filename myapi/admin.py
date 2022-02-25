import json
from django.contrib import admin
from django.db import models
from .models import RequestData, RegtseData, RegdevData, RegtseDataTest, RegdevDataTest, RequestDataTest
from crudapp.models import Atm, AtmImage, AtmModel, AtmModelFunction



class RequestDataAdmin(admin.ModelAdmin):
    list_display=('identity','table', 'endpoint',)
    readonly_fields = ('endpoint','scheme','method','request', 'headers','identity','table')
    list_filter = ('endpoint', )
    exclude = ('request',)

    def jsondata(self, obj):
        data = json.loads(obj.request)
        return data

    def identity(self, obj):
        data = json.loads(obj.request)
        value = "None"
        if 'data' in data:
            if 'MERCHANT' in data["data"][0]:
                value = data["data"][0]["MERCHANT"]
            elif 'TERMINAL_ID' in data["data"][0]:
                value = data["data"][0]["TERMINAL_ID"]
            else:
                value = "None"

        return value

    def table(self, obj):
        data = json.loads(obj.request)
        value = ""
        if data and 'data' in data and 'TABLE' in data["data"][0]:
            value = data["data"][0]["TABLE"]
        return value

# class RequestDataTestAdmin(admin.ModelAdmin):
#     list_display=('identity','table', 'endpoint','createdAt',)
#     readonly_fields = ('endpoint','scheme','method','createdAt','request', 'headers','identity','table')
#     list_filter = ('endpoint', 'createdAt',)
#     exclude = ('request',)

#     def jsondata(self, obj):
#         data = json.loads(obj.request)
#         return data

#     def identity(self, obj):
#         data = json.loads(obj.request)
#         value = "None"
#         if 'data' in data:
#             if 'MERCHANT' in data["data"][0]:
#                 value = data["data"][0]["MERCHANT"]
#             elif 'TERMINAL_ID' in data["data"][0]:
#                 value = data["data"][0]["TERMINAL_ID"]
#             else:
#                 value = "None"

#         return value

#     def table(self, obj):
#         data = json.loads(obj.request)
#         value = ""
#         if data and 'data' in data and 'TABLE' in data["data"][0]:
#             value = data["data"][0]["TABLE"]
#         return value


admin.site.register(RequestData, RequestDataAdmin)
#admin.site.register(RequestDataTest)#, RequestDataTestAdmin)
admin.site.register(RegdevData)
admin.site.register(RegdevDataTest)
admin.site.register(RegtseData)
admin.site.register(RegtseDataTest)