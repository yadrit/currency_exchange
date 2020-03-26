import csv

from django.http import HttpResponse
from django.views.generic import View, ListView


from currency_exchange import settings
from currency.models import Rate


class RateCSV(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="rates.csv"'
        writer = csv.writer(response)
        headers = [
            'id',
            'created',
            'currency',
            'buy',
            'sale',
            'source,'
        ]
        writer.writerow(headers)
        for rate in Rate.objects.all().iterator():
            writer.writerow(map(str, [
                rate.id,
                rate.created,
                rate.get_currency_display(),
                rate.buy,
                rate.sale,
                rate.get_source_display(),
            ]))
        return response


class RatesList(ListView):
    template_name = 'rates_list.html'
    model = Rate
    paginate_by = 20

