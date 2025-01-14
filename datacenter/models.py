from django.db import models
from django.utils import timezone
import datetime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        entered_at = timezone.localtime(self.entered_at)
        if not self.leaved_at:
            now = timezone.localtime(timezone.now())
            time_spent = now - entered_at
            return datetime.timedelta(seconds=time_spent.total_seconds())
        else:
            leaved_at = timezone.localtime(self.leaved_at)
            duration = leaved_at - entered_at
            return datetime.timedelta(seconds=duration.total_seconds())

    def is_visit_long(self, minutes=60):
        duration = datetime.timedelta(minutes=minutes)
        if self.leaved_at and (self.leaved_at - self.entered_at) >= duration:
            return True
        elif not self.leaved_at:
            duration = self.get_duration()
            if duration >= datetime.timedelta(minutes=minutes):
                return True
        return False
