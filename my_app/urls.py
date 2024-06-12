from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DayViewSet, SpeakerViewSet, SessionViewSet, 
    SectionViewSet, FeeViewSet, SponsorViewSet,
    ConferenceInfoViewSet, CommitteeViewSet, MahshulotViev, AuthorInformationViewSet
)

router = DefaultRouter()
router.register(r'days', DayViewSet)
router.register(r'speakers', SpeakerViewSet)
router.register(r'sessions', SessionViewSet)
router.register(r'sections', SectionViewSet)
router.register(r'fees', FeeViewSet)
router.register(r'sponsors', SponsorViewSet)
router.register(r'conference-info', ConferenceInfoViewSet)
router.register(r'mahshulot', MahshulotViev)
router.register(r'author_information', AuthorInformationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('organizing-committee/', CommitteeViewSet.as_view({'get': 'list'}), name='organizing-committee'),
    path('scientific-committee/', CommitteeViewSet.as_view({'get': 'list'}), name='scientific-committee'),
    path('keynote-speakers/', CommitteeViewSet.as_view({'get': 'list'}), name='keynote-speakers'),
]
