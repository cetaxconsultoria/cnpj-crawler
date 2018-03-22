from django.shortcuts import render
from django.http import HttpResponse
from dadoscnpj.models import CNPJ
import json
import re

def index(request):
    return render(request, 'index.html', {})

def results(request):
    cnpjs = request.POST.get('cnpjs')
    cnpjs = cnpjs.split()
    i = 0
    while(i<len(cnpjs)):
        try:
            cnpjs[i] = ''.join(re.split(r'[^0-9]+', cnpjs[i]))
            cnpjs[i] = CNPJ.objects.get(cnpj=cnpjs[i])
            i += 1
        except Exception as e:
            if(type(e).__name__ == 'DoesNotExist'):
                try:
                    with open('../data/'+str(cnpjs[i])+'.jl', 'r') as f:
                        CNPJ.objects.create(cnpj=cnpjs[i], attrs=json.loads(f.read()))
                        cnpjs[i] = CNPJ.objects.get(cnpj=cnpjs[i])
                        i += 1
                except Exception as e:
                    if(type(e).__name__ == 'FileNotFoundError'):
                        print('CALL TO CRAWLER')
                        cnpjs.pop(i)
    return render(request, 'results.html', {'cnpjs': cnpjs})
