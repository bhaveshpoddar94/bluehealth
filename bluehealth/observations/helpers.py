from django.db.models import Avg


def hour_data(orderedEntries):
    labels, values = [], []
    for hour in range(0, 24):
        qs = orderedEntries.filter(created_at__hour = hour)
        if qs:
            avgval = orderedEntries.filter(
                created_at__hour = hour).aggregate(Avg('value'))
            labels.append("{} hrs".format(hour))
            values.append(avgval['value__avg'])
    return labels, values

def all_data(orderedEntries):
    count, labels, values = 1, [], []
    for entry in orderedEntries:
        values.append(entry.value)
        labels.append(count)
        count += 1
    return labels, values
