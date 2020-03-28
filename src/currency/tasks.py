from celery import shared_task
import requests
from currency.models import Rate
from currency import model_choices as mch
from decimal import Decimal
from bs4 import BeautifulSoup


def vkurse():
    url = 'http://vkurse.dp.ua/course.json'
    response = requests.get(url)
    r_json = response.json()
    print(r_json)

    for rate in r_json:
        if rate == 'Dollar':
            currency = mch.CURR_USD

            rate_kwargs = {
                'currency': currency,
                'buy': Decimal(r_json['Dollar']['buy']),
                'sale': Decimal(r_json['Dollar']['sale']),
                'source': mch.SR_VKURSE,
            }

            new_rate = Rate(**rate_kwargs)
            last_rate = Rate.objects.filter(currency=currency, source=mch.SR_VKURSE).last()

            if last_rate is None or (last_rate and new_rate.buy != last_rate.buy or new_rate.sale != last_rate.sale):
                new_rate.save()

        elif rate == 'Euro':
            currency = mch.CURR_EUR

            rate_kwargs = {
                'currency': currency,
                'buy': round(Decimal(r_json['Euro']['buy']), 2),
                'sale': round(Decimal(r_json['Euro']['sale']), 2),
                'source': mch.SR_VKURSE,
            }

            new_rate = Rate(**rate_kwargs)
            last_rate = Rate.objects.filter(currency=currency, source=mch.SR_VKURSE).last()

            if last_rate is None or (last_rate and new_rate.buy != last_rate.buy or new_rate.sale != last_rate.sale):
                new_rate.save()


def pumb():
    page = requests.get("https://about.pumb.ua/info/currency_converter")
    soup = BeautifulSoup(page.content, 'html.parser')
    rates = soup.find(class_="exchange-rate")

    curr_rate = rates.find_all('td')
    currencies = []
    usd_buy = curr_rate[1].get_text()
    usd_sell = curr_rate[2].get_text()
    currencies.append({
        'currency': mch.CURR_USD,
        'buy': round(Decimal(usd_buy), 2),
        'sale': round(Decimal(usd_sell), 2),
        'source': mch.SR_PUMB,
    })

    eur_buy = curr_rate[4].get_text()
    eur_sell = curr_rate[5].get_text()
    currencies.append({
        'currency': mch.CURR_EUR,
        'buy': round(Decimal(eur_buy), 2),
        'sale': round(Decimal(eur_sell), 2),
        'source': mch.SR_PUMB,
    })

    for rate_kwargs in currencies:
        Rate.objects.create(**rate_kwargs)
        new_rate = Rate(**rate_kwargs)
        last_rate = Rate.objects.filter(currency=rate_kwargs['currency'], source=rate_kwargs['source']).last()

        if last_rate is None or (last_rate and new_rate.buy != last_rate.buy or new_rate.sale != last_rate.sale):
            new_rate.save()


def privat():
    url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    response = requests.get(url)
    r_json = response.json()
    print(r_json)

    for rate in r_json:
        if rate['ccy'] in {'USD', 'EUR'}:  # 0(1) if we use list it would be 0(n)
            # print(rate['ccy'], rate['buy'], rate['sale'])
            currency = mch.CURR_USD if rate['ccy'] == 'USD' else mch.CURR_EUR

            rate_kwargs = {
                'currency': currency,
                'buy': Decimal(rate['buy']),
                'sale': Decimal(rate['sale']),
                'source': mch.SR_PRIVAT,
            }

            # Rate.objects.create(**rate_kwargs)
            new_rate = Rate(**rate_kwargs)
            last_rate = Rate.objects.filter(currency=currency, source=mch.SR_PRIVAT).last()

            # print(Rate.objects.filter(currency=currency, source=mch.SR_PRIVAT).query)
            if last_rate is None or (last_rate and new_rate.buy != last_rate.buy or new_rate.sale != last_rate.sale):
                new_rate.save()


def mono():
    url = 'https://api.monobank.ua/bank/currency'
    response = requests.get(url)
    r_json = response.json()
    print(r_json)

    for rate in r_json:
        if rate['currencyCodeA'] in {840, 978} and rate['currencyCodeB'] == 980:
            currency = mch.CURR_USD if rate['currencyCodeA'] == 840 else mch.CURR_EUR

            rate_kwargs = {
                'currency': currency,
                'buy': round(Decimal(rate['rateBuy']), 2),
                'sale': round(Decimal(rate['rateSell']), 2),
                'source': mch.SR_MONO,
            }

            new_rate = Rate(**rate_kwargs)
            last_rate = Rate.objects.filter(currency=currency, source=mch.SR_MONO).last()

            if last_rate is None or (last_rate and new_rate.buy != last_rate.buy or new_rate.sale != last_rate.sale):
                new_rate.save()


@shared_task(bind=True)
def parse_rates(self):
    privat()
    mono()
    vkurse()
    pumb()




