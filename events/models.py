from django.db import models

class Event(models.Model):
    event_name = models.CharField(max_length=30)
    group_name = models.CharField(max_length=40)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_location = models.CharField(max_length=50)

    def __str__(self) :
        return(self.event_name)

    class Meta :
        db_table = 'Event'

