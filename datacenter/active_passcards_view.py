from datacenter.models import Passcard
from django.shortcuts import render


def active_passcards_view(request):
    is_active = Passcard.objects.filter(is_active=True)
    context = {
        'active_passcards': is_active,  # люди с активными пропусками
    }
    return render(request, 'active_passcards.html', context)
