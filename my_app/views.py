from rest_framework import viewsets, generics, permissions
from rest_framework.pagination import PageNumberPagination
from .models import Day, Speaker, Session, Section, Submission, Fee, Sponsor, ConferenceInfo, Mahshulot
from .serializers import DaySerializer, SpeakerSerializer, SessionSerializer, SectionSerializer, SubmissionSerializer, FeeSerializer, SponsorSerializer, ConferenceInfoSerializer, MahshulotSerializer, Author_information, Authorinformation


class SmallPagination(PageNumberPagination):
    page_size = 3

class SpeakerViewSet(viewsets.ModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer
    pagination_class = SmallPagination

    def get_queryset(self):
        category = self.request.query_params.get('category')
        if category:
            return self.queryset.filter(category=category)
        return self.queryset

class OrganizingCommitteeViewSet(viewsets.ModelViewSet):
    queryset = Speaker.objects.filter(category='Organizing Committee')
    serializer_class = SpeakerSerializer
    pagination_class = SmallPagination

class ScientificCommitteeViewSet(viewsets.ModelViewSet):
    queryset = Speaker.objects.filter(category='Scientific Committee')
    serializer_class = SpeakerSerializer
    pagination_class = SmallPagination

class KeynoteSpeakersViewSet(viewsets.ModelViewSet):
    queryset = Speaker.objects.filter(category='Keynote Speaker')
    serializer_class = SpeakerSerializer
    pagination_class = None

class DayViewSet(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer

class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class FeeViewSet(viewsets.ModelViewSet):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer

class SponsorViewSet(viewsets.ModelViewSet):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer

class ConferenceInfoViewSet(viewsets.ModelViewSet):
    queryset = ConferenceInfo.objects.all()
    serializer_class = ConferenceInfoSerializer

class CommitteeViewSet(generics.ListAPIView):
    serializer_class = SpeakerSerializer
    pagination_class = SmallPagination

    def get_queryset(self):
        category = self.kwargs['category']
        return Speaker.objects.filter(category=category)

class CommitteeViewSet(viewsets.ModelViewSet):
    serializer_class = SpeakerSerializer
    pagination_class = SmallPagination

    def get_queryset(self):
        category = self.request.query_params.get('category')
        if category:
            return Speaker.objects.filter(category=category)
        return Speaker.objects.all()

class MahshulotViev(viewsets.ModelViewSet):
    queryset = Mahshulot.objects.all()
    serializer_class = MahshulotSerializer

class MahshulotViev(viewsets.ModelViewSet):
    queryset = Mahshulot.objects.all()
    serializer_class = MahshulotSerializer


class IsSuperUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_superuser
        return True

class AuthorInformationViewSet(viewsets.ModelViewSet):
    queryset = Author_information.objects.all()
    serializer_class = Authorinformation
    permission_classes = [IsSuperUserOrReadOnly]

    def perform_create(self, serializer):
        instance = serializer.save()
        self.send_notification_email(instance)

    def send_notification_email(self, instance):
        from django.core.mail import send_mail

        subject = f'New Author Information Submitted by {instance.frist_name_your} {instance.last_name_your}'
        message = f'''
        A new author information entry has been submitted.

        Your Details:
        Name: {instance.frist_name_your} {instance.last_name_your}
        Email: {instance.email_your}
        Phone: {instance.phone_your}
        Affiliation: {instance.affiliation_your}
        Country: {instance.country_your}

        Author Details:
        Name: {instance.frist_name_autor} {instance.last_name_autor}
        Email: {instance.email_autor}
        Phone: {instance.phone_autor}
        Affiliation: {instance.affiliation_autor}
        Country: {instance.country_autor}

        Paper Details:
        Title: {instance.title_paper}
        Section: {instance.section_paper}
        Keyword: {instance.keyword_paper}

        '''
        admin_email = 'alijonovasilbek058@gmail.com'
        send_mail(subject, message, 'no-reply@example.com', [admin_email])
