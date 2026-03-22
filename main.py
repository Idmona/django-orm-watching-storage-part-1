import os

import django
from django.utils.timezone import activate

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':

    passcards = Passcard.objects.all()
    active_passcards = Passcard.objects.filter(is_active=True)
    print(f"""
Всего пропусков {len(passcards)} 
Активных пропусков {len(active_passcards)} 
""")
