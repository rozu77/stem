from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import StudentRegisterForm, UserRegisterForm
from .models import STUDENT_INFO
from django.contrib.auth.models import User
from django.views.generic import (View, DetailView, ListView, CreateView, TemplateView)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .filter_mixin import ListFilteredMixin
from .filters import StudentFilter
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import get_object_or_404
from datetime import datetime

# Create your views here.
"""
def home(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        formset = ImageFormset(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            lrn = form.cleaned_data.get('lrn')
            messages.success(request, f'Submit Success')
            return redirect('stem:home')
    else:
        form = StudentRegisterForm()
    context={
        'form' : form,
    }
    return render(request, 'stem/enrol.html', context)"""

def pdf(request):
    user_e = request.user.id
    student = STUDENT_INFO.objects.get(student=user_e)
    context={
        'student': student,
        'user': user_e,
    }
    return render(request, 'stem/pdf_template.html', context)


class StudentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):#update
    model = STUDENT_INFO
    form_class = StudentRegisterForm
    success_message = "Thank you!"

    def form_valid(self, form_class):#update 
        form_class.instance.student = self.request.user
        return super().form_valid(form_class)

    def get_context_data(self, *args, **kwargs):
        try:
            user = self.request.user.id
            student = STUDENT_INFO.objects.get(student=user)
            context = super(StudentCreateView, self).get_context_data(**kwargs)
            context.update({
                'student': student,
                'user': user,
            })
            return context
        except STUDENT_INFO.DoesNotExist:
            student = '0'
            user = '0'
            context = super(StudentCreateView, self).get_context_data(**kwargs)
            context.update({
                'student': student,
                'user': user,
            })
            return context


class StudentListView(LoginRequiredMixin, ListFilteredMixin, ListView):
    model = STUDENT_INFO
    template_name = 'stem/list_student.html'
    context_object_name = 'students'
    paginate_by = 30
    filter_set = StudentFilter
    def get_queryset(self):
        qs = self.model.objects.all().order_by('last_name')
        student_filter = StudentFilter(self.request.GET, queryset=qs)
        return student_filter.qs

    def get_context_data(self, *args, **kwargs):
        try:
            date_today = datetime.now().strftime("%Y")

            d1g11 = STUDENT_INFO.objects.filter(d1_walking='True', grade_level_to_enroll='Grade 11').count()
            d1g12 = STUDENT_INFO.objects.filter(d1_walking='True', grade_level_to_enroll='Grade 12').count()
            d2g11 = STUDENT_INFO.objects.filter(d1_public_commute_landwater='True', grade_level_to_enroll='Grade 11').count()
            d2g12 = STUDENT_INFO.objects.filter(d1_public_commute_landwater='True', grade_level_to_enroll='Grade 12').count()
            d3g11 = STUDENT_INFO.objects.filter(d1_family_owned_vehicle='True', grade_level_to_enroll='Grade 11').count()
            d3g12 = STUDENT_INFO.objects.filter(d1_family_owned_vehicle='True', grade_level_to_enroll='Grade 12').count()
            d4g11 = STUDENT_INFO.objects.filter(d1_school_service='True', grade_level_to_enroll='Grade 11').count()
            d4g12 = STUDENT_INFO.objects.filter(d1_school_service='True', grade_level_to_enroll='Grade 12').count()

            e1g11 = STUDENT_INFO.objects.filter(d4_cable_tv='True', grade_level_to_enroll='Grade 11').count()
            e1g12 = STUDENT_INFO.objects.filter(d4_cable_tv='True', grade_level_to_enroll='Grade 12').count()
            e2g11 = STUDENT_INFO.objects.filter(d4_noncable_tv='True', grade_level_to_enroll='Grade 11').count()
            e2g12 = STUDENT_INFO.objects.filter(d4_noncable_tv='True', grade_level_to_enroll='Grade 12').count()
            e3g11 = STUDENT_INFO.objects.filter(d4_basic_cp='True', grade_level_to_enroll='Grade 11').count()
            e3g12 = STUDENT_INFO.objects.filter(d4_basic_cp='True', grade_level_to_enroll='Grade 12').count()
            e4g11 = STUDENT_INFO.objects.filter(d4_smartphone='True', grade_level_to_enroll='Grade 11').count()
            e4g12 = STUDENT_INFO.objects.filter(d4_smartphone='True', grade_level_to_enroll='Grade 12').count()
            e5g11 = STUDENT_INFO.objects.filter(d4_tablet='True', grade_level_to_enroll='Grade 11').count()
            e5g12 = STUDENT_INFO.objects.filter(d4_tablet='True', grade_level_to_enroll='Grade 12').count()
            e6g11 = STUDENT_INFO.objects.filter(d4_radio='True', grade_level_to_enroll='Grade 11').count()
            e6g12 = STUDENT_INFO.objects.filter(d4_radio='True', grade_level_to_enroll='Grade 12').count()
            e7g11 = STUDENT_INFO.objects.filter(d4_desktop='True', grade_level_to_enroll='Grade 11').count()
            e7g12 = STUDENT_INFO.objects.filter(d4_desktop='True', grade_level_to_enroll='Grade 12').count()
            e8g11 = STUDENT_INFO.objects.filter(d4_laptop='True', grade_level_to_enroll='Grade 11').count()
            e8g12 = STUDENT_INFO.objects.filter(d4_laptop='True', grade_level_to_enroll='Grade 12').count()
            e9g11 = STUDENT_INFO.objects.filter(d4_none='True', grade_level_to_enroll='Grade 11').count()
            e9g12 = STUDENT_INFO.objects.filter(d4_none='True', grade_level_to_enroll='Grade 12').count()

            f1g11 = STUDENT_INFO.objects.filter(d6_own_mobile_data='True', grade_level_to_enroll='Grade 11').count()
            f1g12 = STUDENT_INFO.objects.filter(d6_own_mobile_data='True', grade_level_to_enroll='Grade 12').count()
            f2g11 = STUDENT_INFO.objects.filter(d6_own_broadband_internet='True', grade_level_to_enroll='Grade 11').count()
            f2g12 = STUDENT_INFO.objects.filter(d6_own_broadband_internet='True', grade_level_to_enroll='Grade 12').count()
            f3g11 = STUDENT_INFO.objects.filter(d6_computer_shop='True', grade_level_to_enroll='Grade 11').count()
            f3g12 = STUDENT_INFO.objects.filter(d6_computer_shop='True', grade_level_to_enroll='Grade 12').count()
            f4g11 = STUDENT_INFO.objects.filter(d6_other_places='True', grade_level_to_enroll='Grade 11').count()
            f4g12 = STUDENT_INFO.objects.filter(d6_other_places='True', grade_level_to_enroll='Grade 12').count()
            f5g11 = STUDENT_INFO.objects.filter(d6_none='True', grade_level_to_enroll='Grade 11').count()
            f5g12 = STUDENT_INFO.objects.filter(d6_none='True', grade_level_to_enroll='Grade 12').count()


            g1g11 = STUDENT_INFO.objects.filter(d7_ol_learning='True', grade_level_to_enroll='Grade 11').count()
            g1g12 = STUDENT_INFO.objects.filter(d7_ol_learning='True', grade_level_to_enroll='Grade 12').count()
            g2g11 = STUDENT_INFO.objects.filter(d7_tv='True', grade_level_to_enroll='Grade 11').count()
            g2g12 = STUDENT_INFO.objects.filter(d7_tv='True', grade_level_to_enroll='Grade 12').count()
            g3g11 = STUDENT_INFO.objects.filter(d7_radio='True', grade_level_to_enroll='Grade 11').count()
            g3g12 = STUDENT_INFO.objects.filter(d7_radio='True', grade_level_to_enroll='Grade 12').count()
            g4g11 = STUDENT_INFO.objects.filter(d7_modular='True', grade_level_to_enroll='Grade 11').count()
            g4g12 = STUDENT_INFO.objects.filter(d7_modular='True', grade_level_to_enroll='Grade 12').count()
            g5g11 = STUDENT_INFO.objects.filter(d7_f2f_w_modalities='True', grade_level_to_enroll='Grade 11').count()
            g5g12 = STUDENT_INFO.objects.filter(d7_f2f_w_modalities='True', grade_level_to_enroll='Grade 12').count()


            h1g11 = STUDENT_INFO.objects.filter(d8_lack_gadgets='True', grade_level_to_enroll='Grade 11').count()
            h1g12 = STUDENT_INFO.objects.filter(d8_lack_gadgets='True', grade_level_to_enroll='Grade 12').count()
            h2g11 = STUDENT_INFO.objects.filter(d8_insufficient_load='True', grade_level_to_enroll='Grade 11').count()
            h2g12 = STUDENT_INFO.objects.filter(d8_insufficient_load='True', grade_level_to_enroll='Grade 12').count()
            h3g11 = STUDENT_INFO.objects.filter(d8_unstable_internet='True', grade_level_to_enroll='Grade 11').count()
            h3g12 = STUDENT_INFO.objects.filter(d8_unstable_internet='True', grade_level_to_enroll='Grade 12').count()
            h4g11 = STUDENT_INFO.objects.filter(d8_health_conditions='True', grade_level_to_enroll='Grade 11').count()
            h4g12 = STUDENT_INFO.objects.filter(d8_health_conditions='True', grade_level_to_enroll='Grade 12').count()
            h5g11 = STUDENT_INFO.objects.filter(d8_difficulty_independent_learning='True', grade_level_to_enroll='Grade 11').count()
            h5g12 = STUDENT_INFO.objects.filter(d8_difficulty_independent_learning='True', grade_level_to_enroll='Grade 12').count()
            h6g11 = STUDENT_INFO.objects.filter(d8_con_other_activities='True', grade_level_to_enroll='Grade 11').count()
            h6g12 = STUDENT_INFO.objects.filter(d8_con_other_activities='True', grade_level_to_enroll='Grade 12').count()
            h7g11 = STUDENT_INFO.objects.filter(d8_hi_elec_consump='True', grade_level_to_enroll='Grade 11').count()
            h7g12 = STUDENT_INFO.objects.filter(d8_hi_elec_consump='True', grade_level_to_enroll='Grade 12').count()
            h8g11 = STUDENT_INFO.objects.filter(d8_distractions='True', grade_level_to_enroll='Grade 11').count()
            h8g12 = STUDENT_INFO.objects.filter(d8_distractions='True', grade_level_to_enroll='Grade 12').count()


            enrol = STUDENT_INFO.objects.filter(school_year1='2020', school_year2='2021').count()
            g11 = STUDENT_INFO.objects.filter(grade_level_to_enroll='Grade 11').count()
            g12 = STUDENT_INFO.objects.filter(grade_level_to_enroll='Grade 12').count()
            at = STUDENT_INFO.objects.filter(track='Academic Track').count()
            atg11 = STUDENT_INFO.objects.filter(track='Academic Track', grade_level_to_enroll='Grade 11').count()
            atg12 = STUDENT_INFO.objects.filter(track='Academic Track', grade_level_to_enroll='Grade 12').count()
            tvl = STUDENT_INFO.objects.filter(strand='Technical-Vocational-Livelihood').count()
            tvlg11 = STUDENT_INFO.objects.filter(strand='Technical-Vocational-Livelihood',grade_level_to_enroll='Grade 11').count()
            tvlg12 = STUDENT_INFO.objects.filter(strand='Technical-Vocational-Livelihood',grade_level_to_enroll='Grade 12').count()
            stem = STUDENT_INFO.objects.filter(strand='Science, Technology, Engineering, and Mathematics').count()
            stem11 = STUDENT_INFO.objects.filter(strand='Science, Technology, Engineering, and Mathematics', grade_level_to_enroll='Grade 11').count()
            stem12 = STUDENT_INFO.objects.filter(strand='Science, Technology, Engineering, and Mathematics', grade_level_to_enroll='Grade 12').count()
            humss = STUDENT_INFO.objects.filter(strand='Humanities and Social Sciences').count()
            humss11 = STUDENT_INFO.objects.filter(strand='Humanities and Social Sciences', grade_level_to_enroll='Grade 11').count()
            humss12 = STUDENT_INFO.objects.filter(strand='Humanities and Social Sciences', grade_level_to_enroll='Grade 12').count()
            gas = STUDENT_INFO.objects.filter(strand='General Academic Strand').count()
            gas11 = STUDENT_INFO.objects.filter(strand='General Academic Strand', grade_level_to_enroll='Grade 11').count()
            gas12 = STUDENT_INFO.objects.filter(strand='General Academic Strand', grade_level_to_enroll='Grade 12').count()
            abm = STUDENT_INFO.objects.filter(strand='Accountancy, Business and Management').count()
            abm12 = STUDENT_INFO.objects.filter(strand='Accountancy, Business and Management', grade_level_to_enroll='Grade 11').count()
            abm11 = STUDENT_INFO.objects.filter(strand='Accountancy, Business and Management', grade_level_to_enroll='Grade 12').count()

            context = super(StudentListView, self).get_context_data(**kwargs)
            context.update({
                'd1g11': d1g11,
                'd1g12': d1g12,
                'd2g11': d2g11,
                'd2g12': d2g12,
                'd3g11': d3g11,
                'd3g12': d3g12,
                'd4g11': d4g11,
                'd4g12': d4g12,
                'e1g11': e1g11,
                'e1g12': e1g12,
                'e2g11': e2g11,
                'e2g12': e2g12,
                'e3g11': e3g11,
                'e3g12': e3g12,
                'e4g11': e4g11,
                'e4g12': e4g12,
                'e5g11': e5g11,
                'e5g12': e5g12,
                'e6g11': e6g11,
                'e6g12': e6g12,
                'e7g11': e7g11,
                'e7g12': e7g12,
                'e8g11': e8g11,
                'e8g12': e8g12,
                'e9g11': e9g11,
                'e9g12': e9g12,
                'f1g11': f1g11,
                'f1g12': f1g12,
                'f2g11': f2g11,
                'f2g12': f2g12,
                'f3g11': f3g11,
                'f3g12': f3g12,
                'f4g11': f4g11,
                'f4g12': f4g12,
                'f5g11': f5g11,
                'f5g12': f5g12,
                'g1g11': g1g11,
                'g1g12': g1g12,
                'g2g11': g2g11,
                'g2g12': g2g12,
                'g3g11': g3g11,
                'g3g12': g3g12,
                'g4g11': g4g11,
                'g4g12': g4g12,
                'g5g11': g5g11,
                'g5g12': g5g12,
                'h1g11': h1g11,
                'h1g12': h1g12,
                'h2g11': h2g11,
                'h2g12': h2g12,
                'h3g11': h3g11,
                'h3g12': h3g12,
                'h4g11': h4g11,
                'h4g12': h4g12,
                'h5g11': h5g11,
                'h5g12': h5g12,
                'h6g11': h6g11,
                'h6g12': h6g12,
                'h7g11': h7g11,
                'h7g12': h7g12,
                'h8g11': h8g11,
                'h8g12': h8g12,

                'enrol': enrol,
                'g11': g11,
                'g12': g12,
                'stem': stem,
                'stem11': stem11,
                'stem12': stem12,
                'humss': humss,
                'humss11': humss11,
                'humss12': humss12,
                'gas': gas,
                'gas11': gas11,
                'gas12': gas12,
                'abm': abm,
                'abm11': abm11,
                'abm12': abm12,
                'atg11': atg11,
                'atg12': atg12,
                'tvlg11': tvlg11,
                'tvlg12': tvlg12,
                'at': at,
                'tvl': tvl,

                'date_today': date_today,
            })
            return context
        except STUDENT_INFO.DoesNotExist:
            stem = '0'
            
            context = super(StudentListView, self).get_context_data(**kwargs)
            context.update({
                'd1g11': stem,
                'd1g12': stem,
                'd2g11': stem,
                'd2g12': stem,
                'd3g11': stem,
                'd3g12': stem,
                'd4g11': stem,
                'd4g12': stem,
                'e1g11': stem,
                'e1g12': stem,
                'e2g11': stem,
                'e2g12': stem,
                'e3g11': stem,
                'e3g12': stem,
                'e4g11': stem,
                'e4g12': stem,
                'e5g11': stem,
                'e5g12': stem,
                'e6g11': stem,
                'e6g12': stem,
                'e7g11': stem,
                'e7g12': stem,
                'e8g11': stem,
                'e8g12': stem,
                'e9g11': stem,
                'e9g12': stem,
                'f1g11': stem,
                'f1g12': stem,
                'f2g11': stem,
                'f2g12': stem,
                'f3g11': stem,
                'f3g12': stem,
                'f4g11': stem,
                'f4g12': stem,
                'f5g11': stem,
                'f5g12': stem,
                'g1g11': stem,
                'g1g12': stem,
                'g2g11': stem,
                'g2g12': stem,
                'g3g11': stem,
                'g3g12': stem,
                'g4g11': stem,
                'g4g12': stem,
                'g5g11': stem,
                'g5g12': stem,
                'h1g11': stem,
                'h1g12': stem,
                'h2g11': stem,
                'h2g12': stem,
                'h3g11': stem,
                'h3g12': stem,
                'h4g11': stem,
                'h4g12': stem,
                'h5g11': stem,
                'h5g12': stem,
                'h6g11': stem,
                'h6g12': stem,
                'h7g11': stem,
                'h7g12': stem,
                'h8g11': stem,
                'h8g12': stem,
                'enrol': stem,
                'g11': stem,
                'g12': stem,
                'stem': stem,
                'stem11': stem,
                'stem12': stem,
                'humss': stem,
                'humss11': stem,
                'humss12': stem,
                'gas': stem,
                'gas11': stem,
                'gas12': stem,
                'abm': stem,
                'abm11': stem,
                'abm12': stem,
                'atg11': stem,
                'atg12': stem,
                'tvlg11': stem,
                'tvlg12': stem,
                'at': stem,
                'tvl': stem,

                'date_today': stem,
            })
            return context



class StudentDetailView(LoginRequiredMixin, DetailView):
    model = STUDENT_INFO
    template_name = 'stem/student_info_detail.html'


#update
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('stem:login')
    else:
        form = UserRegisterForm()
    return render(request, 'stem/register.html', {'form': form})


