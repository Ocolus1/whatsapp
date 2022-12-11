import json
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateTimeField, OneToOneField, CASCADE, TextField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_enum_choices.fields import EnumChoiceField
from django_celery_beat.models import IntervalSchedule, PeriodicTask
from .constants import TimeInterval, SetupStatus
from django.utils import timezone
import random


class User(AbstractUser):
    name = CharField(_("Name of User"), blank=True, max_length=255, default="cypherspot")
    activity = TextField()
    phone = CharField(max_length=255, blank=True, null=True)
    status = EnumChoiceField(SetupStatus, default=SetupStatus.disabled)
    time_interval = EnumChoiceField(TimeInterval, default=TimeInterval.three_min)
    created_at = DateTimeField(
        "timestamp", auto_now_add=True, editable=False, db_index=True
    )
    updated_at = DateTimeField(auto_now=True)
    task = OneToOneField(
        PeriodicTask,
        on_delete=CASCADE,
        null=True,
        blank=True
    )
    last_name = None
    first_name = None


    def __str__(self) -> str:
        return self.username

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})

    @property
    def generate_random(self):
        random_string = ''

        for _ in range(10):
            # Considering only upper and lowercase letters
            random_integer = random.randint(97, 97 + 26 - 1)
            flip_bit = random.randint(0, 1)
            # Convert to lowercase if the flip bit is on
            random_integer = random_integer - 32 if flip_bit == 1 else random_integer
            # Keep appending random characters using chr(x)
            random_string += (chr(random_integer))

        return random_string

    def delete(self, *args, **kwargs):
        if self.task is not None:
            self.task.delete()
        return super(User, self).delete(*args, **kwargs)

    def setup_task(self):
        self.task = PeriodicTask.objects.create(
            name=self.generate_random,
            task='computation_heavy_task',
            interval=self.interval_schedule,
            args=json.dumps([self.name]),
            start_time=timezone.now(),
            enabled=False
        )


    @property
    def interval_schedule(self):
        if self.time_interval == TimeInterval.three_min:
            return IntervalSchedule.objects.get_or_create(
                every=3,
                period=IntervalSchedule.MINUTES
            )[0]
        elif self.time_interval == TimeInterval.six_hours:
            return IntervalSchedule.objects.get_or_create(
                every=6,
                period=IntervalSchedule.HOURS
            )[0]
        elif self.time_interval == TimeInterval.twelve_hours:
            return IntervalSchedule.objects.get_or_create(
                every=12,
                period=IntervalSchedule.HOURS
            )[0]
