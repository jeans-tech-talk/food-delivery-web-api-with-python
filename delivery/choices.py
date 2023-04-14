from django.db import models
from django.utils.translation import gettext_lazy as _


class PaymentMethod(models.TextChoices):
    CASH = 'Cash', _('Cash')
    CHECKS = 'Checks', _('Checks')
    DEBIT_CARDS = 'Debit cards', _('Debit cards')
    MOBILE_PAYMENTS = 'Mobile payments', _('Mobile payments')
    ELECTRONIC_BANK_TRANSFERS = 'Electronic bank transfers', _('Electronic bank transfer')
