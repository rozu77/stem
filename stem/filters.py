import django_filters

from .models import *

class StudentFilter(django_filters.FilterSet):
    lrn = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    middle_name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = STUDENT_INFO
        fields = ['lrn','last_name','first_name','middle_name','track', 'strand', 'grade_level_to_enroll','sex','d1_walking']