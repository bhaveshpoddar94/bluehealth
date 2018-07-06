from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Attribute
from . import helpers

ATTR = {
    'f1': ['Ambient Temperature', '\u00b0C', '#ff4d4d'],
    'f2': ['Ambient Pressure', 'hPa', '#7fff7f'],
    'f3': ['Water Temperature', '\u00b0C', '#66b2ff'],
    'f4': ['Water Depth', 'cm', '#ffc04d'],
    'f5': ['GPS Latitude', '\u00b0', '#D2691E'],
    'f6': ['GPS Longitude', '\u00b0', '#D2691E'],
    'f7': ['Altitude', 'm', '#9F00B3'],
    'f8': ['Luminosity', 'lux', '#FFD700'],
}

# Create your views here.
# for future use


def home(request):
    if request.user.is_authenticated:
        return HttpResponse("Welcome {}".format(request.user.username))
    else:
        return HttpResponse("Kindly Login")


def list_latest(request):
    context_dict = {'data': {}}
    for attr in ATTR:
        try:
            instance = Attribute.objects.filter(
                obs_type=attr
            ).order_by('-created_at').first()
            context_dict["data"][ATTR[attr][0]] = [instance.value]
            context_dict["data"][ATTR[attr][0]].append(instance.created_at)
        except Exception as e:
            context_dict["data"][ATTR[attr]] = str(e)
    return render(request, "observations/test.html", context_dict)

# saves attributes to database


def save_attr(request):
    context_dict = {'success': True}
    res = {}
    for attr in ATTR.keys():
        value = request.GET.get(attr, "")
        if value:
            try:
                instance = Attribute(obs_type=attr, value=value)
                instance.save()
            except Exception as e:
                context_dict['success'] = False
                context_dict['error'] = str(e)
    return JsonResponse(context_dict)


def analytics(request):
    context_dict = {
        'data': {key: value[0] for (key, value) in ATTR.items()}
    }
    return render(request, "observations/analytics.html", context_dict)


def ajax_data(request):
    obv_type = request.GET.get('type', "f1")
    all_data = request.GET.get('all_data', True)
    context_dict = {
        'fieldname': ATTR[obv_type][0],
        'unit': ATTR[obv_type][1],
        'color': ATTR[obv_type][2]
    }
    orderedEntries = Attribute.objects.filter(obs_type=obv_type)
    if all_data:
        context_dict['labels'], context_dict['values'] =\
            helpers.all_data(orderedEntries)
    else:
        context_dict['labels'], context_dict['values'] =\
            helpers.hour_data(orderedEntries)
    return JsonResponse(context_dict)


def analytics_com(request):
    return render(request, "observations/analyticscom.html")


def ajax_com_data(request):
    obv_type1 = request.GET.get('type1', "f1")
    obv_type2 = request.GET.get('type2', "f3")
    all_data = request.GET.get('all_data', True)
    context_dict = {}
    context_dict['data1'] = {
        'fieldname': ATTR[obv_type1][0],
        'unit': ATTR[obv_type1][1],
        'color': ATTR[obv_type1][2]
    }
    context_dict['data2'] = {
        'fieldname': ATTR[obv_type2][0],
        'unit': ATTR[obv_type2][1],
        'color': ATTR[obv_type2][2]
    }
    orderedEntries1 = Attribute.objects.filter(obs_type=obv_type1)
    orderedEntries2 = Attribute.objects.filter(obs_type=obv_type2)
    if all_data:
        context_dict['data1']['labels'], context_dict['data1']['values'] =\
            helpers.all_data(orderedEntries1)
        context_dict['data2']['labels'], context_dict['data2']['values'] =\
            helpers.all_data(orderedEntries2)
    else:
        context_dict['data1']['labels'], context_dict['data1']['values'] =\
            helpers.hour_data(orderedEntries1)
        context_dict['data2']['labels'], context_dict['data2']['values'] =\
            helpers.hour_data(orderedEntries2)
    return JsonResponse(context_dict)


def ajax_add_data(request):
    obv_type = request.GET.get('type', "f1")
    last_label = request.GET.get('lastlabel', "")
    context_dict = {
        'labels': [],
        'values': []
    }
    orderedEntries = Attribute.objects.filter(obs_type=obv_type)
    if last_label and orderedEntries.count() > int(last_label):
        count = int(last_label) + 1
        for entry in orderedEntries:
            context_dict['labels'].append(count)
            context_dict['values'].append(entry.value)
            count += 1
    return JsonResponse(context_dict)


# def ajax_data(request):
#     obv_type = request.GET.get('type', "f1")
#     context_dict = {
#         'fieldname': ATTR[obv_type][0],
#         'unit'     : ATTR[obv_type][1],
#         'color'    : ATTR[obv_type][2]
#     }
#     orderedEntries = Attribute.objects.filter(obs_type=obv_type)
#     context_dict['labels'], context_dict['values'] = helpers.hour_data(
#              orderedEntries)
#     return JsonResponse(context_dict)
