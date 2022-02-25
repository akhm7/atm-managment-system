from datetime import datetime,timezone,timedelta
from time import strptime
import json
import pytz
from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import PCIPTS, Atm, AtmImage, AtmModel, AtmModelFunction, chatHistory, telegramUser, ticket, telegramMsg, brokenCategory, MfoStruct, Profile
from myapi.models import RequestData, RegdevData, RegtseData, RequestDataTest, RegdevDataTest, RegtseDataTest
from .forms import AtmForm, AtmImageForm, AtmModelForm, AtmModelFunctionForm, ticketStatusForm, UpdateUserForm, UpdateProfileForm
from django.views.generic import ListView, DetailView
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .filters import AtmFilter
import csv
import xlwt
import requests
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

# class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
#     template_name = 'users/password_reset.html'
#     email_template_name = 'users/password_reset_email.html'
#     subject_template_name = 'users/password_reset_subject'
#     success_message = "We've emailed you instructions for setting your password, " \
#                       "if an account exists with the email you entered. You should receive them shortly." \
#                       " If you don't receive an email, " \
#                       "please make sure you've entered the address you registered with, and check your spam folder."
#     success_url = reverse_lazy('users-home')

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'users/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('profile')

class IndexView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    template_name = "crudapp/index.html"
    context_object_name = 'atm_list'

    def get_queryset(self):
        return Atm.objects.all()

class AtmStaticView(ListView):
    template_name = "crudapp/statistic_atm.html"
    context_object_name = 'atm_list'

    def get_queryset(self):
        return Atm.objects.all()

class TestAtmView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    template_name = "crudapp/atms-filter-list.html"
    context_object_name = 'atm_list'
    model = Atm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = AtmFilter(self.request.GET,queryset=self.get_queryset())
        return context

    def get_queryset(self):
        return Atm.objects.all()


class ModelAtmView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    template_name = "crudapp/model-list.html"
    context_object_name = 'model_list'

    def get_queryset(self):
        return AtmModel.objects.all()

class ModelRequestTestView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    template_name = "crudapp/request-list-test.html"
    context_object_name = 'request_list_test'

    def get_queryset(self):
        queryset = RequestDataTest.objects.all().order_by('-id')
        re = []
        for r in queryset:
            
            temp_r = {'id':r.id, 'table_name':'', 'endpoint':r.endpoint, 'request':r.request, 'dt':r.createdAt,'scheme':r.scheme,'method':r.method, 'data':{}}
            try:
                data = json.loads(r.request)
                temp_r['data'] = data['data']
                #print(temp_r)
                if 'data' in data and 'TABLE' in data["data"][0]:
                    temp_r['table_name'] = data["data"][0]["TABLE"]
                else:
                    temp_r['table_name'] = 'Not formattabled'
                temp_r['request'] = json.dumps(data, indent=4)
            except Exception as e:
                temp_r['table_name'] = 'Not formattabled'
            re.append(temp_r)
            #re[r.id]=temp_r
        return re



class ModelTseTestView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    template_name = "crudapp/tse-list-test.html"
    context_object_name = 'tse_list_test'
        
    def get_queryset(self):
        return RegtseDataTest.objects.all()

class ModelDeviceTestView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    template_name = "crudapp/device-list-test.html"
    context_object_name = 'device_list_test'
    
    def get_queryset(self):
        return RegdevDataTest.objects.all()

class ModelTicketView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    template_name = "crudapp/servicedesk.html"
    context_object_name = 'servicedesk'
    
    def get_queryset(self):
        return ticket.objects.filter(status__in=[0,3,4]).order_by('-id')

class ModelTicketClosedView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    template_name = "crudapp/servicedesk-close.html"
    context_object_name = 'servicedesk'
    
    def get_queryset(self):
        return ticket.objects.filter(status__in=[1,2,5]).order_by('-id')
#lol
class ModelTicketAtmView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    template_name = "crudapp/servicedesk-atm.html"
    context_object_name = 'servicedesk'
    # br = brokenCategory.objects.all()
    # stats_br = {}
    # for i in br:
    #     stats_br[i['title']]=ticket.objects.filter(status__in=[1,0,3,4])

    def get_queryset(self):
        atm_id = self.kwargs.get('id')
        return ticket.objects.filter(atm__id = atm_id).filter(status__in=[1,0,3,4]).order_by('-id')

class ModelTicketUsersView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    template_name = "crudapp/servicedesk-users.html"
    context_object_name = 'telegramUsers'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mfo_list'] = MfoStruct.objects.all()
        return context

    def get_queryset(self):
        return telegramUser.objects.all().order_by('-id')

class ModelPCIPTSView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    template_name = "crudapp/pcipts.html"
    context_object_name = 'pcipts'
    
    def get_queryset(self):
        return PCIPTS.objects.filter(show=1)

class ModelRequestView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    template_name = "crudapp/request-list.html"
    context_object_name = 'request_list'

    def get_queryset(self):
        queryset = RequestData.objects.all().order_by('-id')
        re = []
        for r in queryset:
            
            temp_r = {'id':r.id, 'table_name':'', 'endpoint':r.endpoint, 'request':r.request, 'dt':r.createdAt,'scheme':r.scheme,'method':r.method, 'data':{}}
            try:
                data = json.loads(r.request)
                temp_r['data'] = data['data']
                #print(temp_r)
                if 'data' in data and 'TABLE' in data["data"][0]:
                    temp_r['table_name'] = data["data"][0]["TABLE"]
                else:
                    temp_r['table_name'] = 'Not formattabled'
                temp_r['request'] = json.dumps(data, indent=4)
            except Exception as e:
                temp_r['table_name'] = 'Not formattabled'
            re.append(temp_r)
            #re[r.id]=temp_r
        return re

class ModelTseView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    template_name = "crudapp/tse-list.html"
    context_object_name = 'tse_list'
        
    def get_queryset(self):
        return RegtseData.objects.all()

class ModelDeviceView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    template_name = "crudapp/device-list.html"
    context_object_name = 'device_list'
    
    def get_queryset(self):
        return RegdevData.objects.all()


class FunctionModelAtmView(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    template_name = "crudapp/function-list.html"
    context_object_name = 'function_list'

    def get_queryset(self):
        return AtmModelFunction.objects.all()
    
class AtmDetailView(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login/'
    model = Atm
    template_name = 'crudapp/atm-detail.html'
    context_object_name = 'obj'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        queryset = AtmImage.objects.prefetch_related().all()
    
        imgs = []
        for img in queryset:
            if img.atmId == kwargs['object']:
                imgs.append(img)
        #imgs = reversed(imgs)
        context['imgs'] =imgs[-4:]
        return context


# class TicketMsgView(LoginRequiredMixin, DetailView):
#     login_url = '/ticket/'
#     model = ticket
#     template_name = 'crudapp/ticket_msg.html'
#     context_object_name = 'obj'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         queryset = telegramMsg.objects.prefetch_related().all()
    
#         msgs = []
#         for msg in queryset:
#             if img.atmId == kwargs['object']:
#                 imgs.append(img)
#         context['imgs'] =imgs
#         return context
        
@login_required
def IndexPage(request):
    return render(request, 'crudapp/main.html')

@login_required
def atmStatistic(request):
    statistics = []
    total = {}
    total['id'] = ''
    total['name'] = 'Итог'
    total['number_zfill'] = ''
    total['number'] = 0
    total['count'] = 0
    total['devicesTotalCashOut'] = 0
    total['devicesTotalCashIn'] = 0
    total['UzcardCashOut'] = 0
    total['UzcardCashIn'] = 0
    total['HumoCashOut'] = 0
    total['HumoCashIn'] = 0
    total['InHouseCashOut'] = 0
    total['InHouseCashIn'] = 0
    total['admsTotalCount'] = 0


    mfos = MfoStruct.objects.all()
    for m in mfos:
        if m.number == 1091:
            continue
        atms = Atm.objects.filter(mfo=m)
        stats = {}
        stats['count'] = atms.count()
        total['count'] += atms.count()
        stats['id'] = m.id
        stats['name'] = m.name
        stats['number_zfill'] = str(m.number).zfill(5)
        stats['number'] = m.number


        #общ колво устройств
        stats['devicesTotalCashOut'] = Atm.objects.filter(mfo=m).exclude(atmModelId__functions__name='Cash-In').count()
        stats['devicesTotalCashIn'] = Atm.objects.filter(mfo=m,atmModelId__functions__name='Cash-In').count()
        stats['UzcardCashOut'] = Atm.objects.filter(mfo=m, atmModelId__functions__name='Uzcard', inBankProcessing=0).exclude(atmModelId__functions__name='Cash-In').count()#узкард кэш аут общ
        stats['UzcardCashIn'] = Atm.objects.filter(mfo=m,atmModelId__functions__name='Uzcard', inBankProcessing=0).filter(atmModelId__functions__name='Cash-In').count()#узкард кэш ин общ
        stats['HumoCashOut'] = Atm.objects.filter(mfo=m,atmModelId__functions__name='Humo', inBankProcessing=0).exclude(atmModelId__functions__name='Cash-In').count()#хумо кэш аут общ
        stats['HumoCashIn'] = Atm.objects.filter(mfo=m,atmModelId__functions__name='Humo', inBankProcessing=0).filter(atmModelId__functions__name='Cash-In').count()#хумо кэш ин общ
        stats['InHouseCashOut'] = Atm.objects.filter(mfo=m,inBankProcessing=1).exclude(atmModelId__functions__name='Cash-In').count()
        stats['InHouseCashIn'] = Atm.objects.filter(mfo=m,inBankProcessing=1).filter(atmModelId__functions__name='Cash-In').count()
        stats['admsTotalCount'] = 0





        #общ колво устройств
        total['devicesTotalCashOut'] += Atm.objects.filter(mfo=m).exclude(atmModelId__functions__name='Cash-In').count()
        total['devicesTotalCashIn'] += Atm.objects.filter(mfo=m,atmModelId__functions__name='Cash-In').count()
        total['UzcardCashOut'] += Atm.objects.filter(mfo=m, atmModelId__functions__name='Uzcard', inBankProcessing=0).exclude(atmModelId__functions__name='Cash-In').count()#узкард кэш аут общ
        total['UzcardCashIn'] += Atm.objects.filter(mfo=m,atmModelId__functions__name='Uzcard', inBankProcessing=0).filter(atmModelId__functions__name='Cash-In').count()#узкард кэш ин общ
        total['HumoCashOut'] += Atm.objects.filter(mfo=m,atmModelId__functions__name='Humo', inBankProcessing=0).exclude(atmModelId__functions__name='Cash-In').count()#хумо кэш аут общ
        total['HumoCashIn'] += Atm.objects.filter(mfo=m,atmModelId__functions__name='Humo', inBankProcessing=0).filter(atmModelId__functions__name='Cash-In').count()#хумо кэш ин общ
        total['InHouseCashOut'] += Atm.objects.filter(mfo=m,inBankProcessing=1).exclude(atmModelId__functions__name='Cash-In').count()
        total['InHouseCashIn'] += Atm.objects.filter(mfo=m,inBankProcessing=1).count()
        total['admsTotalCount'] += 0
        statistics.append(stats)

    statistics.append(total)

    # atms = Atm.objects.filter(atmModelId__functions__name='Uzcard').exclude(atmModelId__functions__name='Cash-In')#.exclude(atmModelId__functions__name='Uzcard')
    # atms = Atm.objects.filter(atmModelId__functions__name='Humo').exclude(atmModelId__functions__name='Cash-In')#.exclude(atmModelId__functions__name='Uzcard')
    # atms = Atm.objects.filter(atmModelId__functions__name='Uzcard')
    # atms = Atm.objects.filter(atmModelId__functions__name='Humo')
    #atms = Atm.objects.filter(atmModelId__functions__name__in=['Uzcard'])

    return render(request,  'crudapp/statistic_atm.html', {'statistics':statistics})

def SendMessage(chat_id, text, parse_mode, reply_markup):
    data={'chat_id': chat_id, 'text': text, 'parse_mode': parse_mode, 'reply_markup': reply_markup}
    return requests.post(url="https://api.telegram.org/botTOKEN/sendMessage",data=data).json()

def telegramApi(request):
# POST \
#      -H 'Content-Type: application/json' \
#      -d '{"chat_id": "123456789", "text": "This is a test from curl", "disable_notification": true}' \
#      https://api.telegram.org/bot2100805689:AAEx1FFTJPdWdJDm4O05wkPmPlkDq9FHqgU/sendMessage

    keyboard = json.dumps({'inline_keyboard':[[{"text":"Ok 👌","callback_data":"notif_ok"}]]})

    s = SendMessage(976361202, "text" , parse_mode="HTML", reply_markup = keyboard)
    response = HttpResponse(json.dumps(s),content_type='application/json')
    return response


def export_report_csv(request):
    #writer.writerow(['ID','Название','Мфо','Устройства','Cash-Out','Cash-In','Uzcard [Cash-Out]','Uzcard [Cash-In]','Humo [Cash-Out]','Humo [Cash-In]','InHouse [Cash-Out]','InHouse [Cash-In]','ADM'])
    
    statistics = []
    total = {}
    total['id'] = ''
    total['number_zfill'] = ''
    total['name'] = 'Итог'
    total['count'] = 0
    total['devicesTotalCashOut'] = 0
    total['devicesTotalCashIn'] = 0
    total['UzcardCashOut'] = 0
    total['UzcardCashIn'] = 0
    total['HumoCashOut'] = 0
    total['HumoCashIn'] = 0
    total['InHouseCashOut'] = 0
    total['InHouseCashIn'] = 0
    total['admsTotalCount'] = 0
    mfos = MfoStruct.objects.all()
    for m in mfos:
        if m.number == 1091:
            continue
        atms = Atm.objects.filter(mfo=m)
        stats = {}
        stats['id'] = m.id
        stats['number_zfill'] = str(m.number).zfill(5)
        stats['name'] = "{0} филиали".format(m.name)
        stats['count'] = atms.count()
        total['count'] += atms.count()


        #общ колво устройств
        stats['devicesTotalCashOut'] = Atm.objects.filter(mfo=m).exclude(atmModelId__functions__name='Cash-In').count()
        stats['devicesTotalCashIn'] = Atm.objects.filter(mfo=m,atmModelId__functions__name='Cash-In').count()
        stats['UzcardCashOut'] = Atm.objects.filter(mfo=m, atmModelId__functions__name='Uzcard', inBankProcessing=0).exclude(atmModelId__functions__name='Cash-In').count()#узкард кэш аут общ
        stats['UzcardCashIn'] = Atm.objects.filter(mfo=m,atmModelId__functions__name='Uzcard', inBankProcessing=0).filter(atmModelId__functions__name='Cash-In').count()#узкард кэш ин общ
        stats['HumoCashOut'] = Atm.objects.filter(mfo=m,atmModelId__functions__name='Humo', inBankProcessing=0).exclude(atmModelId__functions__name='Cash-In').count()#хумо кэш аут общ
        stats['HumoCashIn'] = Atm.objects.filter(mfo=m,atmModelId__functions__name='Humo', inBankProcessing=0).filter(atmModelId__functions__name='Cash-In').count()#хумо кэш ин общ
        stats['InHouseCashOut'] = Atm.objects.filter(mfo=m,inBankProcessing=1).exclude(atmModelId__functions__name='Cash-In').count()
        stats['InHouseCashIn'] = Atm.objects.filter(mfo=m,inBankProcessing=1).filter(atmModelId__functions__name='Cash-In').count()
        stats['admsTotalCount'] = 0





        #общ колво устройств
        total['devicesTotalCashOut'] += Atm.objects.filter(mfo=m).exclude(atmModelId__functions__name='Cash-In').count()
        total['devicesTotalCashIn'] += Atm.objects.filter(mfo=m,atmModelId__functions__name='Cash-In').count()
        total['UzcardCashOut'] += Atm.objects.filter(mfo=m, atmModelId__functions__name='Uzcard', inBankProcessing=0).exclude(atmModelId__functions__name='Cash-In').count()#узкард кэш аут общ
        total['UzcardCashIn'] += Atm.objects.filter(mfo=m,atmModelId__functions__name='Uzcard', inBankProcessing=0).filter(atmModelId__functions__name='Cash-In').count()#узкард кэш ин общ
        total['HumoCashOut'] += Atm.objects.filter(mfo=m,atmModelId__functions__name='Humo', inBankProcessing=0).exclude(atmModelId__functions__name='Cash-In').count()#хумо кэш аут общ
        total['HumoCashIn'] += Atm.objects.filter(mfo=m,atmModelId__functions__name='Humo', inBankProcessing=0).filter(atmModelId__functions__name='Cash-In').count()#хумо кэш ин общ
        total['InHouseCashOut'] += Atm.objects.filter(mfo=m,inBankProcessing=1).exclude(atmModelId__functions__name='Cash-In').count()
        total['InHouseCashIn'] += Atm.objects.filter(mfo=m,inBankProcessing=1).count()
        total['admsTotalCount'] += 0
        statistics.append(stats)

    statistics.append(total)

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="cbu.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('ATM&ADM' , cell_overwrite_ok = True) # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    ws.col(2).width = int(30*260)
    for i in range(3, 12):
        ws.col(i).width = int(20*260)
    columns = ['№', 'МФО', 'Тижорат банклари', 'Жами банкомат ва АДМ сони', 'Cash out', 'Cash in-сash out reсycling', 'Cash out', 'Cash in-сash out reсycling', 'Cash out', 'Cash in-сash out reсycling', 'Cash out', 'Cash in-сash out reсycling', 'АДМлар сони']

# top_row = 0
# bottom_row = 0
# left_column = 0
# right_column = 1
    style = xlwt.XFStyle()
    style.alignment.wrap = 1
    style.font.bold = True

    ws.write_merge(0, 0, 4, 5, 'Total',style)
    ws.write_merge(0, 0, 6, 7, 'Uzcard',style)
    ws.write_merge(0, 0, 8, 9, 'Humo',style)
    ws.write_merge(0, 0, 10, 11, 'Процессинг',style)
    ws.write_merge(0, 1, 0, 0,'№',style)
    ws.write_merge(0, 1, 1, 1,'МФО',style)
    ws.write_merge(0, 1, 2, 2,'Филиал',style)
    ws.write_merge(0, 1, 3, 3,'Общее кол-во',style)
    ws.write_merge(0, 1, 12, 12,'Кол-во АДМ-ов',style)
    for i,s in enumerate(columns):
        ws.write(1,i,s,style)

    for i,s in enumerate(statistics):
        for j,cell in enumerate(s):
            if j==2:
                ws.write(i+2,j,s.get(cell),font_style)
            else:
                ws.write(i+2,j,s.get(cell))

        #ws.write(' ',s['number_zfill'],"{0} филиали".format(s['number_zfill']),s['count'],s['devicesTotalCashOut'],s['devicesTotalCashIn'],s['UzcardCashOut'],s['UzcardCashIn'],s['HumoCashOut'],s['HumoCashIn'],s['InHouseCashOut'],s['InHouseCashIn'],s['admsTotalCount'])  

    #for col_num in range(len(columns)):
    #    ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # # Sheet body, remaining rows
    # font_style = xlwt.XFStyle()

    # rows = User.objects.all().values_list('username', 'first_name', 'last_name', 'email')
    # for row in rows:
    #     row_num += 1
    #     for col_num in range(len(row)):
    #         ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response

@login_required
def create(request):
    if request.method == 'POST':
        form = AtmForm(request.POST)
        if form.is_valid():
            t = form.save()
            return redirect('detail', pk=t.id)
    form = AtmForm()
    return render(request, 'crudapp/create.html', {'form':form})

@login_required
def edit(request, pk, template_name = 'crudapp/edit.html'):
    atm = get_object_or_404(Atm, pk=pk)
    form = AtmForm(request.POST or None, instance=atm)
    if form.is_valid():
        t = form.save()
        return redirect('detail', pk=t.id)
    return render(request, template_name, {'form':form})

@login_required
def delete(request, pk, template_name='crudapp/confirm_delete.html'):
    atm = get_object_or_404(Atm, pk=pk)
    if request.method=='POST':
        atm.delete()
        return redirect('atms')
    return render(request, template_name, {'object':atm})


@login_required
def image_upload_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    if request.method == 'POST':
        form = AtmImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            if img_obj:
                return render(request, 'crudapp/image.html', {'form': form, 'img_obj': img_obj})
    else:
        try:
            atm = Atm.objects.get(pk=pk)
        except Atm.DoesNotExist:
            atm = None
        
        if atm:
            form = AtmImageForm(initial={'atmId': atm})
        else:
            form = AtmImageForm()
    return render(request, 'crudapp/image.html', {'form': form})

@login_required
def modelCreate(request):
    context = {}
    if request.method == "POST":
        form = AtmModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('model-list')
    else:
        form = AtmModelForm()
    context['form']= form
    return render(request, "crudapp/model-create.html", context)

@login_required
def modelDelete(request, pk, template_name='crudapp/model-delete.html'):
    atm_model = get_object_or_404(AtmModel, pk=pk)
    if request.method=='POST':
        atm_model.delete()
        return redirect('model-list')
    return render(request, template_name, {'object':atm_model})

@login_required
def modelEdit(request, pk, template_name = 'crudapp/model-edit.html'):
    atm_model = get_object_or_404(AtmModel, pk=pk)
    form = AtmModelForm(request.POST or None, request.FILES or None, instance=atm_model)
    if form.is_valid():
        form.save()
        return redirect('model-list')
    return render(request, template_name, {'form':form})

@login_required
def functionCreate(request):
    if request.method == 'POST':
        form = AtmModelFunctionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('function-list')
    form = AtmModelFunctionForm()

    return render(request, 'crudapp/function-create.html', {'form':form})

@login_required
def functionDelete(request, pk, template_name='crudapp/function-delete.html'):
    function_model = get_object_or_404(AtmModelFunction, pk=pk)
    if request.method=='POST':
        function_model.delete()
        return redirect('function-list')
    return render(request, template_name, {'object':function_model})

@login_required
def functionEdit(request, pk, template_name = 'crudapp/function-edit.html'):
    function_model = get_object_or_404(AtmModelFunction, pk=pk)
    form = AtmModelFunctionForm(request.POST or None, instance=function_model)
    if form.is_valid():
        form.save()
        return redirect('function-list')
    return render(request, template_name, {'form':form})

@login_required
def regdevStatusChange(request, pk):
    regdev = get_object_or_404(RegdevData, pk=pk)
    print(pk, request, regdev, regdev.status)
    if request.method=='GET':
        regdev.status = not regdev.status
        print(regdev.status)
        regdev.save()
    return redirect('device-list')

@login_required
def regtseStatusChange(request, pk):
    regtse = get_object_or_404(RegtseData, pk=pk)
    print(pk, request, regtse, regtse.status)
    if request.method=='GET':
        regtse.status = not regtse.status
        print(regtse.status)
        regtse.save()
    return redirect('tse-list')

@login_required
def tgUserChangeMfo(request, pk, mfo):
    tgUser = get_object_or_404(telegramUser, pk=pk)
    tgMfo = get_object_or_404(MfoStruct, id=mfo)
    #http://10.231.202.31:8081/tg/users/36/1
    if request.method=='GET':
        tgUser.status = 1
        tgUser.mfo = tgMfo
        tgUser.save()
    return redirect('servicedesk-users')

@login_required
def requestShow(request, pk, template_name='crudapp/show-request.html'):
    r = get_object_or_404(RequestData, pk=pk)
    data_str = ""
    try:
        data = json.loads(r.request)
        data_str = json.dumps(data, indent=4)
    except Exception as e:
        data_str = "Ошибка парсинга JSON."
    #print(pk, request, r)
    if request.method=='GET':
        return render(request, template_name, {'object':r, 'code':data_str})
        #return HttpResponse('<a href="../">Back to list</a><pre>'+r.request+'</pre>'+'<br><a href="../">Back to list</a> <a href="#top">Back to top</a>')
    return redirect('request-list')

@user_passes_test(lambda u: u.groups.filter(name='Colvir').exists())
def regdevTestStatusChange(request, pk):
    regdev = get_object_or_404(RegdevDataTest, pk=pk)
    print(pk, request, regdev, regdev.status)
    if request.method=='GET':
        regdev.status = not regdev.status
        print(regdev.status)
        regdev.save()
    return redirect('device-list-test')

@user_passes_test(lambda u: u.groups.filter(name='Colvir').exists())
def regtseTestStatusChange(request, pk):
    regtse = get_object_or_404(RegtseDataTest, pk=pk)
    print(pk, request, regtse, regtse.status)
    if request.method=='GET':
        regtse.status = not regtse.status
        print(regtse.status)
        regtse.save()
    return redirect('tse-list-test')

@login_required
def requestTestShow(request, pk, template_name='crudapp/show-request-test.html'):
    r = get_object_or_404(RequestDataTest, pk=pk)
    data_str = ""
    try:
        data = json.loads(r.request)
        data_str = json.dumps(data, indent=4)
    except Exception as e:
        data_str = "Ошибка парсинга JSON."
    if request.method=='GET':
        return render(request, template_name, {'object':r, 'code':data_str})
    return redirect('request-list-test')


@login_required
def TicketView(request, pk, template_name='crudapp/ticket_msg.html'):
    T = get_object_or_404(ticket, pk=pk)

    tmp_msgs = telegramMsg.objects.filter(t=T)
    msgs = []

    for i in tmp_msgs:
        tmp = json.loads(i.json, strict=False)
        tmp['date'] = datetime.fromtimestamp(tmp['date'])
        tmp['category'] = i.category
        tmp['path'] = i.path
        tmp['download'] = i.download
        tmp['operator'] = i.operator
        tmp['show'] = i.show
        if i.text:
            tmp['text'] = json.loads(i.text)
        if i.caption:
            tmp['caption'] = json.loads(i.caption)
        msgs.append(tmp)

    
    form = ticketStatusForm(T.atm.mfo, request.POST or None, instance=T)
    if form.is_valid():
        keyboard = json.dumps({'inline_keyboard':[[{"text":"Ok 👌","callback_data":"notif_ok"}]]})
        moderName = request.user.first_name +' '+ request.user.last_name
        if not T.operator:
            T.operator = moderName
        ''
        s = SendMessage(T.user.uid, "🔔 Administrator <b>{2}</b> - <code>#{0}</code> arizaning holatini <i>{1}</i>-ga o\'zgartirdi.".format(T.id, T.get_status_display(), moderName) , parse_mode="HTML", reply_markup = keyboard)
        #r = json.loads(s)
        chatHistory.objects.create(chat=T.user.uid, user=T.user.uid, message_id=s['result']['message_id'])

                
        ob = form.save()
        ob.dataClosed = datetime.now()
        ob.save()
        # Get the current instance object to display in the template
        return redirect('servicedesk')
    return render(request, template_name, {'form': form, 'obj':T, 'messages':msgs,})
    

# class TicketView(LoginRequiredMixin, DetailView):
#     model = ticket
#     template_name = 'crudapp/ticket_msg.html'
#     context_object_name = 'obj'

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         queryset = telegramMsg.objects.all()
    
#         msgs = []
#         for m in queryset:
#             if m.t == kwargs['object']:
#                 m.json = json.loads(m.json)
#                 msgs.append(m)
#         context['messages'] = msgs
#         return context


# @login_required
# def profile(request):
#     if request.method == 'POST':
#         user_form = UpdateUserForm(request.POST, instance=request.user)
#         profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Your profile is updated successfully')
#             return redirect(to='users-profile')
#     else:
#         user_form = UpdateUserForm(instance=request.user)
#         profile_form = UpdateProfileForm(instance=request.user.profile)

#     return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(instance=request.user, data=request.POST)
        profile_form = UpdateProfileForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'users/profile.html', {'user_form': user_form, 'profile_form': profile_form})