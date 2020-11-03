from django.db import models
import statistics
from statistics import NormalDist
from django.db.models import Avg, StdDev

# Create your models here.
class ReadingQuerySet(models.QuerySet):
	pass

class ReadingManager(models.Manager):
	def get_queryset(self):
		return ReadingQuerySet(self.model, using=self._db)

class Reading(models.Model):
	date = models.DateField(auto_now=True)
	pressure =models.FloatField(default=0)
	flowrate =models.FloatField(default=0)
	detection = models.CharField(max_length=12, blank=False)
	probability = models.DecimalField(max_digits=8, default=0, decimal_places=4)
	timestamp =models.TimeField(auto_now_add=True)

	objects = ReadingManager()
	
	def __str__(self):
		return str(self.timestamp) + ' ' + 'Pressure: ' + str(self.pressure) + ' ' + 'Flowrate: ' + str(self.flowrate)

	def detect_leak(self):
		a = self.pressure
		b = self.flowrate
		mupre = Reading.objects.all().aggregate(Avg('pressure')).get('pressure__avg')
		muflo = Reading.objects.all().aggregate(Avg('flowrate')).get('flowrate__avg')
		stdpre = Reading.objects.all().aggregate(StdDev('pressure')).get('pressure__stddev')
		stdflo = Reading.objects.all().aggregate(StdDev('flowrate')).get('flowrate__stddev')
		proba = NormalDist(mupre, stdpre).pdf(a)
		probb = NormalDist(muflo, stdflo).pdf(b)
		gaussnorm = proba*probb
		if gaussnorm > 0.02:
			return 'No Leakage'
		else:
			return 'Leakage'

	def gaussian_probability(self):
		x = self.pressure
		y = self.flowrate
		muprex = Reading.objects.all().aggregate(Avg('pressure')).get('pressure__avg')
		mufloy = Reading.objects.all().aggregate(Avg('flowrate')).get('flowrate__avg')
		stdprex = Reading.objects.all().aggregate(StdDev('pressure')).get('pressure__stddev')
		stdfloy = Reading.objects.all().aggregate(StdDev('flowrate')).get('flowrate__stddev')
		probx = NormalDist(muprex, stdprex).pdf(x)
		proby = NormalDist(mufloy, stdfloy).pdf(y)
		gauss = probx*proby
		return gauss

	def save(self, *args, **kwargs):
		self.detection = self.detect_leak()
		self.probability = self.gaussian_probability()
		super(Reading, self).save(*args, **kwargs)