from django.db import models
from django.utils import timezone


class Train(models.Model):

    NOT_TRAINED, TRAINING, TRAINED = 0, 1, 2
    STATUSES = (
        (NOT_TRAINED, 'Not trained yet'),
        (TRAINING, 'Training'),
        (TRAINED, 'Trained'),
    )

    dataset_uuid = models.UUIDField('DataSet UUID')
    created = models.DateTimeField(default=timezone.now)
    status = models.SmallIntegerField(choices=STATUSES, default=NOT_TRAINED)
    trained_model = models.FileField(null=True, blank=True)
    dataset_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return str(self.dataset_uuid)

