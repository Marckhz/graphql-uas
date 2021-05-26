from django.core.management.base import BaseCommand


from commerce.models import Product, Reviews

from django.db import transaction

import pandas as pd

