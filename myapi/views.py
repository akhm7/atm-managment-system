import json
from django.http import response
from django.shortcuts import render
import base64
from django.http.response import HttpResponse, JsonResponse
from rest_framework import status, decorators
from rest_framework.decorators import api_view, parser_classes
from myapi.models import RegdevData, RegtseData, RequestData, RequestDataTest, RegdevDataTest, RegtseDataTest



@api_view(['POST'])
def ReceivingData(request):
    #if request.content_type != 'application/xml' or request.content_type != 'text/plain':
    #    return HttpResponse('<xml><result>Failed. The request content_type is not "application/xml" or xml-file.</result></xml>', status=status.HTTP_405_METHOD_NOT_ALLOWED, content_type='application/xml')
  
    #file = request.data['file']

    #request.body.decode('utf-8')

    answer = {
        'request_id': 0,
        'count': 0,
        'success': 0,
        'fail': 0,
        'records': [
            {
                'status': 'ok',
                'index': 0,
                'record_id': 0,
                'errors': {}
            },
        ]
    }

    try:
        RequestObj = RequestData.objects.create(request=request.body.decode('utf-8'), endpoint='ReceivingData', method=request.method, scheme=request.scheme, headers=request.headers)
        RequestObj.save()
        answer['request_id']=RequestObj.pk
        answer['records'][0]['record_id']=RequestObj.pk
        data = json.loads(request.body.decode('utf-8'))

        table = ""
        file_type = ""
        if 'TABLE' in data["data"][0]:
            table = data["data"][0]["TABLE"]
        else:
            file_type = 'Not field'

        if table == 'MERCHANTS_ALL':
            file_type = 'REGTSE'
        elif table == 'SET0_ACC_TR_ALL':
            file_type = 'REGDEV'
        else:
            file_type = 'Unknown'

        if 'MERCHANT' in data["data"][0]:
            if data["data"][0]["MERCHANT"]!="":
                if file_type == 'REGTSE':
                    regtse = RegtseData.objects.create(MERCHANT=data["data"][0]["MERCHANT"], PARENT=data["data"][0]["PARENT"], ABRV_NAME=data["data"][0]["ABRV_NAME"], FULL_NAME=data["data"][0]["FULL_NAME"], CNTRY=data["data"][0]["CNTRY"], CITY=data["data"][0]["CITY"], STREET=data["data"][0]["STREET"], REG_NR=data["data"][0]["REG_NR"], PHONE=data["data"][0]["PHONE"], MCC=data["data"][0]["MCC"], POST_IND=data["data"][0]["POST_IND"], MRC_PHONE=data["data"][0]["MRC_PHONE"], req=request.body.decode('utf-8'), dt=RequestObj.createdAt)
                    regtse.save()
                    answer['records'][0]['record_id']=regtse.pk
                    answer['success'] = 1
                    return JsonResponse(answer, status=status.HTTP_202_ACCEPTED)
        elif ('TERMINAL_ID' in data["data"][0] and 'ACCEPTOR_ID' in data["data"][0]):
            if data["data"][0]["TERMINAL_ID"]!="" and data["data"][0]["ACCEPTOR_ID"]!="":
                if file_type == 'REGDEV':
                    regtse_obj = RegtseData.objects.filter(MERCHANT=data["data"][0]["ACCEPTOR_ID"])
                    print(regtse_obj.first())
                    if regtse_obj.first():
                        regdev = RegdevData.objects.create(TERMINAL_ID=data["data"][0]["TERMINAL_ID"], ACCEPTOR_ID=data["data"][0]["ACCEPTOR_ID"], TERM_TYPE=data["data"][0]["TERM_TYPE"], POINT_CODE=data["data"][0]["POINT_CODE"], SERIAL_NR=data["data"][0]["SERIAL_NR"], INV_NR=data["data"][0]["INV_NR"], CURRENCY="", regtseId=regtse_obj.first(), req=request.body.decode('utf-8'), dt=RequestObj.createdAt)
                        regdev.save()
                        answer['records'][0]['record_id']=regdev.pk
                        answer['success'] = 1
                        return JsonResponse(answer, status=status.HTTP_202_ACCEPTED)
        print("Not analyzed data. ", table)
        answer['records'][0]['status']='error'
        answer['records'][0]['errors']={ 'REQ_ERROR': ['Not analyzed data.'] }
        answer['count'] = 1
        answer['fail'] = 1
        return JsonResponse(answer, status=status.HTTP_406_NOT_ACCEPTABLE)
    except Exception as e:
        print("ReceivingData: ", e)
        print(request)
        answer['records'][0]['status']='error'
        answer['records'][0]['errors']={ 'REQ_ERROR': [str(e)] }
        answer['count'] = 1;
        answer['fail'] = 1;
        return JsonResponse(answer, status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['POST'])
def ReceivingDataTest(request):
    answer = {
        'request_id': 0,
        'count': 0,
        'success': 0,
        'fail': 0,
        'records': [
            {
                'status': 'ok',
                'index': 0,
                'record_id': 0,
                'errors': {}
            },
        ]
    }

    try:
        RequestObj = RequestDataTest.objects.create(request=request.body.decode('utf-8'), endpoint='ReceivingDataTest', method=request.method, scheme=request.scheme, headers=request.headers)
        RequestObj.save()
        answer['request_id']=RequestObj.pk
        answer['records'][0]['record_id']=RequestObj.pk
        data = json.loads(request.body.decode('utf-8'))

        table = ""
        file_type = ""
        if 'TABLE' in data["data"][0]:
            table = data["data"][0]["TABLE"]
        else:
            file_type = 'Not field'

        if table == 'MERCHANTS_ALL':
            file_type = 'REGTSE'
        elif table == 'SET0_ACC_TR_ALL':
            file_type = 'REGDEV'
        else:
            file_type = 'Unknown'

        if 'MERCHANT' in data["data"][0]:
            if data["data"][0]["MERCHANT"]!="":
                if file_type == 'REGTSE':
                    regtse = RegtseDataTest.objects.create(MERCHANT=data["data"][0]["MERCHANT"], PARENT=data["data"][0]["PARENT"], ABRV_NAME=data["data"][0]["ABRV_NAME"], FULL_NAME=data["data"][0]["FULL_NAME"], CNTRY=data["data"][0]["CNTRY"], CITY=data["data"][0]["CITY"], STREET=data["data"][0]["STREET"], REG_NR=data["data"][0]["REG_NR"], PHONE=data["data"][0]["PHONE"], MCC=data["data"][0]["MCC"], POST_IND=data["data"][0]["POST_IND"], MRC_PHONE=data["data"][0]["MRC_PHONE"], req=request.body.decode('utf-8'), dt=RequestObj.createdAt)
                    regtse.save()
                    answer['records'][0]['record_id']=regtse.pk
                    answer['success'] = 1
                    return JsonResponse(answer, status=status.HTTP_202_ACCEPTED)
        elif ('TERMINAL_ID' in data["data"][0] and 'ACCEPTOR_ID' in data["data"][0]):
            if data["data"][0]["TERMINAL_ID"]!="" and data["data"][0]["ACCEPTOR_ID"]!="":
                if file_type == 'REGDEV':
                    regtse_obj = RegtseDataTest.objects.filter(MERCHANT=data["data"][0]["ACCEPTOR_ID"])
                    print(regtse_obj.first())
                    if regtse_obj.first():
                        regdev = RegdevDataTest.objects.create(TERMINAL_ID=data["data"][0]["TERMINAL_ID"], ACCEPTOR_ID=data["data"][0]["ACCEPTOR_ID"], TERM_TYPE=data["data"][0]["TERM_TYPE"], POINT_CODE=data["data"][0]["POINT_CODE"], SERIAL_NR=data["data"][0]["SERIAL_NR"], INV_NR=data["data"][0]["INV_NR"], CURRENCY="", regtseId=regtse_obj.first(), req=request.body.decode('utf-8'), dt=RequestObj.createdAt)
                        regdev.save()
                        answer['records'][0]['record_id']=regdev.pk
                        answer['success'] = 1
                        return JsonResponse(answer, status=status.HTTP_202_ACCEPTED)
        print("Not analyzed data. ", table)
        answer['records'][0]['status']='error'
        answer['records'][0]['errors']={ 'REQ_ERROR': ['Not analyzed data.'] }
        answer['count'] = 1
        answer['fail'] = 1
        return JsonResponse(answer, status=status.HTTP_406_NOT_ACCEPTABLE)
    except Exception as e:
        print("ReceivingData: ", e)
        print(request)
        answer['records'][0]['status']='error'
        answer['records'][0]['errors']={ 'REQ_ERROR': [str(e)] }
        answer['count'] = 1;
        answer['fail'] = 1;
        return JsonResponse(answer, status=status.HTTP_406_NOT_ACCEPTABLE)