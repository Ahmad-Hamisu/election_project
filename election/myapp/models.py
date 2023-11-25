# models.py

from django.db import models


class State(models.Model):
    name = models.CharField(max_length=255)


class LGA(models.Model):
    name = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE)


class Ward(models.Model):
    name = models.CharField(max_length=255)
    lga = models.ForeignKey(LGA, on_delete=models.CASCADE)


class PollingUnit(models.Model):
    name = models.CharField(max_length=255)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
# myapp/models.py


class AnnouncedPuResult(models.Model):
    polling_unit = models.ForeignKey(PollingUnit, on_delete=models.CASCADE)
    party = models.CharField(max_length=255)
    party_score = models.IntegerField()

    def __str__(self):
        return f"{self.party} - {self.party_score}"


class AnnouncedLgaResult(models.Model):
    lga = models.ForeignKey(LGA, on_delete=models.CASCADE)
    party = models.CharField(max_length=255)
    party_score = models.IntegerField()
