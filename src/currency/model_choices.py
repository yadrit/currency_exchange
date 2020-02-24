CURR_USD, CURR_EUR = range(1, 3)

CURRENCY_CHOICES = (
    (CURR_USD, 'USD'),
    (CURR_EUR, 'EUR'),
)

SR_PRIVAT, SR_MONO, SR_VKURSE, SR_PUMB = range(1, 5)

SOURCE_CHOICES = (
    (SR_PRIVAT, 'PrivatBank'),
    (SR_MONO, 'Monobank'),
    (SR_VKURSE, 'Vkurse'),
    (SR_PUMB, 'Pumb'),
)