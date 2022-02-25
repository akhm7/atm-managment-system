from django.db import models
from datetime import datetime, timezone
import json


class RequestData(models.Model):
    createdAt = models.DateTimeField("Создан", auto_now_add = True)
    method = models.TextField("Метод", blank = True, null = True)
    scheme = models.TextField("Схема", blank = True, null = True)
    headers = models.TextField("Заголовок", blank = True, null = True)
    request = models.TextField("Запрос", blank = True, null = True)
    endpoint = models.CharField("API", max_length=255, blank = True, null = True)

    class Meta:
        verbose_name = "Запросы"
        verbose_name_plural = "Запросы"

    def __str__(self):
        temp = json.loads(self.request)
        value = "None"
        if 'data' in temp:
            if 'MERCHANT' in temp["data"][0]:
                value = temp["data"][0]["MERCHANT"]
            elif 'TERMINAL_ID' in temp["data"][0]:
                value = temp["data"][0]["TERMINAL_ID"]
            else:
                value = "None"

        return value

class RegtseData(models.Model):
    MERCHANT = models.CharField("MERCHANT", max_length=255, blank = False, null = False)
    PARENT = models.CharField("PARENT", max_length=255, blank = True, null = True)
    ABRV_NAME = models.CharField("ABRV_NAME", max_length=255, blank = True, null = True)
    FULL_NAME = models.CharField("FULL_NAME", max_length=255, blank = True, null = True)
    CNTRY = models.CharField("CNTRY", max_length=255, blank = True, null = True)
    CITY = models.CharField("CITY", max_length=255, blank = True, null = True)
    STREET = models.CharField("STREET", max_length=255, blank = True, null = True)
    REG_NR = models.CharField("REG_NR", max_length=255, blank = True, null = True)
    PHONE = models.CharField("PHONE", max_length=255, blank = True, null = True)
    MCC = models.CharField("MCC", max_length=255, blank = True, null = True)
    POST_IND = models.CharField("POST_IND", max_length=255, blank = True, null = True)
    MRC_PHONE = models.CharField("MRC_PHONE", max_length=255, blank = True, null = True)
    req = models.TextField("req", blank = True, null = True)
    status = models.BooleanField("STATUS",default=False)
    dt = models.DateTimeField("dt", default=datetime.now())

    class Meta:
        verbose_name = "Мерчанты"
        verbose_name_plural = "Мерчанты"
    
    def __str__(self):
        return self.MERCHANT


class RegdevData(models.Model):
    TERMINAL_ID = models.CharField("Terminal Id", max_length=255, blank = False, null = False)
    ACCEPTOR_ID = models.CharField("Acceptor Id", max_length=255, blank = False, null = False)
    TERM_TYPE = models.CharField("Type", max_length=255, blank = True, null = True)
    POINT_CODE = models.CharField("Point Code", max_length=255, blank = True, null = True)
    SERIAL_NR = models.CharField("Serial Number", max_length=255, blank = True, null = True)
    INV_NR = models.CharField("Inventory Number", max_length=255, blank = True, null = True)
    CURRENCY = models.CharField("Currency", max_length=255, blank = True, null = True)
    regtseId = models.ForeignKey(related_name='regtseId', to=RegtseData, on_delete=models.CASCADE)
    req = models.TextField("req", blank = True, null = True)
    status = models.BooleanField("STATUS", default=False)
    dt = models.DateTimeField("dt", default=datetime.now())

    class Meta:
        verbose_name = "Устройства"
        verbose_name_plural = "Устройства"

    def __str__(self):
        return self.TERMINAL_ID

class RequestDataTest(models.Model):
    createdAt = models.DateTimeField("Создан", auto_now_add = True)
    method = models.TextField("Метод", blank = True, null = True)
    scheme = models.TextField("Схема", blank = True, null = True)
    headers = models.TextField("Заголовок", blank = True, null = True)
    request = models.TextField("Запрос", blank = True, null = True)
    endpoint = models.CharField("API", max_length=255, blank = True, null = True)

    class Meta:
        verbose_name = "Запросы (test)"
        verbose_name_plural = "Запросы (test)"

    def __str__(self):
        temp = json.loads(self.request)
        value = "None"
        if 'data' in temp:
            if 'MERCHANT' in temp["data"][0]:
                value = temp["data"][0]["MERCHANT"]
            elif 'TERMINAL_ID' in temp["data"][0]:
                value = temp["data"][0]["TERMINAL_ID"]
            else:
                value = "None"

        return value

class RegtseDataTest(models.Model):
    MERCHANT = models.CharField("MERCHANT", max_length=255, null = False)
    PARENT = models.CharField("PARENT", max_length=255, null = False)
    ABRV_NAME = models.CharField("ABRV_NAME", max_length=255, blank = True, null = True)
    FULL_NAME = models.CharField("FULL_NAME", max_length=255, blank = True, null = True)
    CNTRY = models.CharField("CNTRY", max_length=255, blank = True, null = True)
    CITY = models.CharField("CITY", max_length=255, blank = True, null = True)
    STREET = models.CharField("STREET", max_length=255, blank = True, null = True)
    REG_NR = models.CharField("REG_NR", max_length=255, blank = True, null = True)
    PHONE = models.CharField("PHONE", max_length=255, blank = True, null = True)
    MCC = models.CharField("MCC", max_length=255, blank = True, null = True)
    POST_IND = models.CharField("POST_IND", max_length=255, blank = True, null = True)
    MRC_PHONE = models.CharField("MRC_PHONE", max_length=255, blank = True, null = True)
    req = models.TextField("req", blank = True, null = True)
    status = models.BooleanField("STATUS",default=False)
    dt = models.DateTimeField("dt", default=datetime.now())

    class Meta:
        verbose_name = "Мерчанты (test)"
        verbose_name_plural = "Мерчанты (test)"
    
    def __str__(self):
        return self.MERCHANT


class RegdevDataTest(models.Model):
    TERMINAL_ID = models.CharField("Terminal Id", max_length=255, blank = False, null = False)
    ACCEPTOR_ID = models.CharField("Acceptor Id", max_length=255, blank = False, null = False)
    TERM_TYPE = models.CharField("Type", max_length=255, blank = True, null = True)
    POINT_CODE = models.CharField("Point Code", max_length=255, blank = True, null = True)
    SERIAL_NR = models.CharField("Serial Number", max_length=255, blank = True, null = True)
    INV_NR = models.CharField("Inventory Number", max_length=255, blank = True, null = True)
    CURRENCY = models.CharField("Currency", max_length=255, blank = True, null = True)
    regtseId = models.ForeignKey(related_name='regtseId', to=RegtseDataTest, on_delete=models.CASCADE)
    req = models.TextField("req", blank = True, null = True)
    status = models.BooleanField("STATUS", default=False)
    dt = models.DateTimeField("dt", default=datetime.now())

    class Meta:
        verbose_name = "Устройства (test)"
        verbose_name_plural = "Устройства (test)"

    def __str__(self):
        return self.TERMINAL_ID