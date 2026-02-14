from django.core.management.base import BaseCommand
from produk.utils import get_fastprint_data

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        get_fastprint_data()
