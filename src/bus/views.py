from django.shortcuts import render
from django.http import HttpResponse
from .models import BusInfo, BusDropArea, BusPickArea

import json

def index(request, template_name='bus_resrv_system.html'):
    page_title = 'Bus'
    return render(request, template_name, locals())

def search_bus(request, template_name='bus/search_bus.html'):
    page_title = 'Book a ticket'
    
    if request.method == 'POST':
        post_data = request.POST.copy()
        area_from_id = post_data.get('area_from')
        area_to_id = post_data.get('area_to')
        bus_info_list = BusInfo.objects.filter(arriving_from__area_name=area_from_id, depature_at__area_name=area_to_id)
    return render(request, template_name, locals())


def autocomplete_pick(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        drugs = BusPickArea.objects.filter(area_name__icontains=q)[:20]
        results = []
        for drug in drugs:
            drug_json = {}
            drug_json['id'] = drug.id
            drug_json['label'] = drug.area_name
            drug_json['value'] = drug.area_name
            results.append(drug_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, content_type=mimetype)


def autocomplete_drop(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        drugs = BusDropArea.objects.filter(area_name__icontains=q)[:20]
        results = []
        for drug in drugs:
            drug_json = {}
            drug_json['id'] = drug.id
            drug_json['label'] = drug.area_name
            drug_json['value'] = drug.area_name
            results.append(drug_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, content_type=mimetype)
