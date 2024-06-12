from rest_framework import serializers
from .models import Day, Speaker, Session, Section, Submission, Fee, Sponsor, ConferenceInfo, Mahshulot, Author_information

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = '__all__'

class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = '__all__'

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = '__all__'

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'

class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fee
        fields = '__all__'

class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'

class ConferenceInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConferenceInfo
        fields = '__all__'

class MahshulotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mahshulot
        fields = '__all__'

class Authorinformation(serializers.ModelSerializer):
    class Meta:
        model = Author_information
        fields = '__all__'
