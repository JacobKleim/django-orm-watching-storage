from django.shortcuts import get_object_or_404
from django.shortcuts import render

from datacenter.models import Passcard, Visit
from datacenter.utils import format_duration


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    passcard_visits = []
    for visit in visits:
        this_passcard_visits = {
                'entered_at': visit.entered_at,
                'duration': format_duration(visit.get_duration()),
                'is_strange': visit.is_visit_long(),
            }
        passcard_visits.append(this_passcard_visits)

    context = {
        'passcard': passcard,
        'this_passcard_visits': passcard_visits
    }
    return render(request, 'passcard_info.html', context)
