from rest_framework import serializers

from app.models import Reading

class ReadingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reading
		fields = ['id','date','timestamp','pressure','flowrate','probability','detection']
		read_only_fields = ['detection', 'probability']