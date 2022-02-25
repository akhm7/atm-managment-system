from django.conf import settings
from django.db import models
from datetime import date, datetime, timezone
from django.forms.widgets import RadioSelect
from django.db.models.fields import NullBooleanField
from django.contrib.auth.models import User
from PIL import Image

#Филиалы
class MfoStruct(models.Model):
    name = models.CharField("Название", max_length=255, default='', blank = True, null = True)
    number = models.IntegerField("МФО", blank = True, null = True)

    class Meta:
        verbose_name = "MFO"
        verbose_name_plural = "MFO"

    def __str__(self):
        if not self.number or not self.name:
            return 'unknown'
        return self.name+' ('+str(self.number).zfill(5)+')'

class AtmModelFunction(models.Model):
    name = models.CharField("Название", max_length=255,blank = True, null = True)
    html = models.TextField(blank = True, null = False)
    description = models.TextField(blank = True, null = True)

    class Meta:
        verbose_name = "Параметр"
        verbose_name_plural = "Параметры"

    def __str__(self):
        return self.name

class AtmModelFunction(models.Model):
    name = models.CharField("Название", max_length=255,blank = True, null = True)
    html = models.TextField(blank = True, null = False)
    description = models.TextField(blank = True, null = True)

    class Meta:
        verbose_name = "Параметр"
        verbose_name_plural = "Параметры"

    def __str__(self):
        return self.name

class AtmModel(models.Model):
    name = models.CharField("Название", max_length=255,blank = True, null = True)
    company = models.CharField("Компания", max_length=255,blank = True, null = True)
    image = models.ImageField("Изображение", upload_to='model/model_img_'+datetime.now().strftime("%Y%m%d_%H-%M-%S"), blank=True, null = True)
    functions = models.ManyToManyField(AtmModelFunction, blank=True, verbose_name="Функционал")

    class Meta:
        verbose_name = "Модель ATM"
        verbose_name_plural = "Модели ATM"

    def __str__(self):
        return self.name

class serviceContract(models.Model):
    SERVICEDESK = (
        (0, 'Гарантийное'),
        (1, 'Сервисное'),
        (2, 'Отсуствует'),
    )
    name = models.CharField("Договор", max_length=255)
    dataBegin = models.DateField("Дата начала", blank = True, null = True)
    dataEnd = models.DateField("Дата конца", blank = True, null = True)
    company = models.CharField("Компания", max_length=255,blank = True, null = True)
    type = models.IntegerField("Вид", choices=SERVICEDESK, default=0)
    amt = models.FloatField("Стоимость", default=0, blank = True, null = True)

    def __str__(self):
        if self.dataEnd:
            return '{0} ({1}) - {2}'.format(self.name ,self.get_type_display(),self.dataEnd)
        return  '{0} ({1})'.format(self.name ,self.get_type_display())
    
    
    class Meta:
        verbose_name = "Сервис Компании"
        verbose_name_plural = "Сервис Компании"

#terminalId
class Atm(models.Model):
    AUTH_PROC = (
        (0, 'Внешний процессинг'),
        (1, 'Внутренний процессинг'),
    )
    SEL = (
        (0, 'Off'),
        (1, 'On'),
    )
    WT = (
        (0, '24/7'),
        (1, '09:00-18:00'),
        (2, '08:00-23:00'),
        (3, '08:00-01:00'),
    )
    name = models.CharField("Название", max_length=255,blank = True, null = True)
    serialNumber = models.PositiveBigIntegerField("Серийный номер")
    merchantId = models.CharField("Merchant ID", default='', max_length=255, blank = True, null = True)
    atmModelId = models.ForeignKey(verbose_name="Модель банкомата", to=AtmModel, on_delete=models.CASCADE)
    description = models.TextField("Описание", blank = True, null = True)
    createdAt = models.DateTimeField("Created At", auto_now_add = True)
    terminalId = models.CharField("Terminal ID", max_length=255, blank = True, null = True)
    mfo = models.ForeignKey(MfoStruct, on_delete=models.CASCADE)
    lat = models.FloatField(default=0.,blank = True, null = True)
    long = models.FloatField(default=0.,blank = True, null = True)
    mobile = models.TextField("Sim", blank = True, null = True)
    exDate = models.DateField("Эксплуатация", blank = True, null = True)
    inBankProcessing = models.IntegerField("Процессинговый центр", default = 0, choices=AUTH_PROC)
    NFC = models.IntegerField("NFC", default = 0, choices=SEL)
    RDSCommander = models.IntegerField("RDS Commander", default = 0, choices=SEL)
    service = models.ForeignKey(verbose_name="Обслуживание", to=serviceContract, null = True, on_delete=models.CASCADE)
    workTime = models.IntegerField("Время работы", default=0, choices=WT)

    class Meta:
        verbose_name = "Банкомат"
        verbose_name_plural = "Банкоматы"

    def __str__(self):
        return self.name
#{% for group_for in request.user.groups.all %}/{{group_for.name}}{% endfor %}
class AtmImage(models.Model):
    title = models.CharField(max_length=200, default="atm_img_"+datetime.now().strftime("%Y%m%d_%H-%M-%S"), null = True, blank=False)
    description = models.TextField(null = True, blank=True)
    image = models.ImageField(upload_to='atms/%Y/%m/%d/', blank=False)
    atmId = models.ForeignKey(related_name='atms', to=Atm, on_delete=models.CASCADE)
    uploadedAt = models.DateTimeField("uploadedAt", auto_now_add = True)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return self.title

class brokenCategory(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Категории поломок"
        verbose_name_plural = "Категории поломок"



class telegramUser(models.Model):
    AUTH_CHOICES = (
        (0, 'Неавторизован'),
        (1, 'Авторизован'),
    )
    LANG_CHOICES = (
        (0, 'Узбекский'),
        (1, 'Русский'),
    )
    uid = models.IntegerField(default=0, verbose_name='Telegram User ID')
    mfo = models.ForeignKey( MfoStruct, default=None, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Филиал')
    name = models.CharField("Имя", max_length=255,blank = True, null = True)
    stage = models.TextField(blank=True, null=True, default='', verbose_name='Действие')
    status = models.IntegerField(default=0, choices=AUTH_CHOICES, verbose_name='Авторизация')
    json_info = models.TextField(blank=True, null=True, default='', verbose_name='JSON')
    language = models.IntegerField(default=0, choices=LANG_CHOICES, verbose_name='Локализация') 

    def __str__(self):
        if not self.mfo:
            return str(self.uid)+' - '+self.name+' [not mfo]'
        return str(self.uid)+' - '+self.name+' ['+str(self.mfo.name)+']'


    class Meta:
        verbose_name = "Телеграм Пользователи"
        verbose_name_plural = "Телеграм Пользователи"

class ticket(models.Model):
    STATUS_CHOICES = (
        (0, 'Открыто'),
        (1, 'Закрыто'),
        (2, 'Отменено'),
        (3, 'Сервисное обслуживание'),
        (4, 'В работе'),
        (5, 'Неизвестно'),
    )
    broken = models.ManyToManyField(brokenCategory, blank=True, verbose_name="Проблема")
    atm = models.ForeignKey(Atm, default=None, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Банкомат')
    user = models.ForeignKey(telegramUser, default=None, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Пользователь (Telegram)')
    dataCreated = models.DateTimeField(default=datetime.now, blank=True, verbose_name='Создан')
    dataClosed = models.DateTimeField(null=True, blank=True, verbose_name='Закрыт')
    status = models.IntegerField(choices=STATUS_CHOICES, null=True, blank=True, default=5, verbose_name='Статус')
    operator = models.TextField(blank=True, null=True, default='', verbose_name='Модератор')
    description = models.TextField(blank=True, null=True, default='', verbose_name='Комментарий')
    edited = models.IntegerField(null=True, blank=True, default=0, verbose_name='Редактирование')

    def save(self):
        self.dataClosed = datetime.now()
        super(ticket, self).save()

    class Meta:
        verbose_name = "Тикеты"
        verbose_name_plural = "Тикеты"

class telegramMsg(models.Model):
    json = models.TextField()
    text = models.BinaryField(blank=True, null=True)
    caption = models.BinaryField(null=True, blank=True) 
    t = models.ForeignKey(related_name='ticket', to=ticket, default=None, blank=True, null=True, on_delete=models.CASCADE)
    category = models.TextField(default='')
    dt = models.DateTimeField(default=datetime.now, blank=True)
    path = models.TextField(default='', blank=True)
    download = models.BooleanField(default=False)
    operator = models.BooleanField(default=False)
    show = models.BooleanField(default=False)

class chatHistory(models.Model):
    chat = models.BigIntegerField(default=0)
    user = models.BigIntegerField(default=0)
    message_id = models.BigIntegerField(default=0)


class PCIPTS(models.Model):
    manufacturer_name = models.TextField("Компания",blank=True, null=True, default='')
    model_name = models.TextField(blank=True, null=True, default='')
    hardware_number = models.TextField(blank=True, null=True, default='')
    firmware_number = models.TextField(blank=True, null=True, default='')
    application_number = models.TextField(blank=True, null=True, default='')
    approval_number = models.TextField(blank=True, null=True, default='')
    version = models.TextField(blank=True, null=True, default='')
    approval_class = models.TextField("Наименование",blank=True, null=True, default='')
    product_type = models.TextField(blank=True, null=True, default='')
    expiry_date = models.DateField(default=datetime.now, blank=True)
    approval_class_1 = models.TextField(blank=True, null=True, default='')
    pin_support = models.TextField(blank=True, null=True, default='')
    pin_key_management = models.TextField(blank=True, null=True, default='')
    sred_key_management = models.TextField(blank=True, null=True, default='')
    prompt_control = models.TextField(blank=True, null=True, default='')
    pin_entry_technology = models.TextField(blank=True, null=True, default='')
    functions_provided = models.TextField(blank=True, null=True, default='')
    not_marketed = models.IntegerField( null=True, blank=True, default=0)
    show = models.IntegerField("Показывать на сайте?",null=True, blank=True, default=0)

    class Meta:
        verbose_name = "PCIPTS"
        verbose_name_plural = "PCIPTS"


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, blank=True, null=True,  on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    photo = models.ImageField(default='profile_images/default_image_aloqabank.png', upload_to='profile_images/%Y/%m/%d', blank=True)
    user_tg = models.OneToOneField(telegramUser, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
        #return 'Profile for user {}'.format(self.user.username)

    # resizing images
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.photo.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.photo.path)

    
    class Meta:
        verbose_name = "Профили"
        verbose_name_plural = "Профили"
