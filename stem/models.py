from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image, ExifTags
from django.dispatch import receiver
from datetime import datetime


YN_CHOICES = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]


SCHOOLTYPE_CHOICES = [
        ('Public', 'Public'),
        ('Private', 'Private'),
    ]

SEMESTER_CHOICES = [
        ('1st', '1st'),
        ('2nd', '2nd'),
    ]
    
STRAND_CHOICES = [
        ('',''),
        ('Accountancy, Business and Management', 'ABM'),
        ('Humanities and Social Sciences', 'HUMSS'),
        ('Science, Technology, Engineering, and Mathematics', 'STEM'),
        ('General Academic Strand', 'GAS'),
    ]

TRACK_CHOICES = [
        ('',''),
        ('Academic Track', 'Academic Track'),
        ('Technical-Vocational-Livelihood', 'Technical-Vocational-Livelihood'),
    ]

SEX_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

EDUCATTAIN_CHOICES = [
        ('',''),
        ('Elementary Graduate', 'Elementary Graduate'),
        ('High School Graduate', 'High School Graduate'),
        ('College Graduate', 'College Graduate'),
        ('Vocational', 'Vocational'),
        ('Masters/Doctorate degree', 'Masters/Doctorate degree'),
        ('Did not attend school', 'Did not attend school'),
    ]

EMPSTATUS_CHOICES = [
        ('Full time', 'Full time'),
        ('Part time', 'Part time'),
        ('Self employed', 'Self employed'),
        ('Unemployed due to ECQ', 'Unemployed due to ECQ'),
        ('Not working', 'Not working'),
    ]


GRADE_CHOICES = [
        ('Grade 11', 'Grade 11'),
        ('Grade 12', 'Grade 12'),
    ]



class STUDENT_INFO(models.Model):
    #update
    student = models.OneToOneField(User, on_delete=models.CASCADE)

    psa_cer_no = models.CharField(max_length=50, null=True, blank=True)
    lrn = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    extension_name = models.CharField(max_length=50, null=True, blank=True)
    birthdate = models.DateTimeField()
    age = models.CharField(max_length=3)
    sex = models.CharField(max_length=6, choices=SEX_CHOICES)
    ip = models.CharField(max_length=3, choices=YN_CHOICES, null=True, blank=True)
    ip_specify = models.CharField(max_length=100, null=True, blank=True)
    mother_tongue = models.CharField(max_length=50, null=True, blank=True)
    religion = models.CharField(max_length=50, null=True, blank=True)
    special_ed_needs = models.CharField(max_length=3, choices=YN_CHOICES, null=True, blank=True)
    speed_needs_specify = models.CharField(max_length=50, null=True, blank=True)
    technology_devices = models.CharField(max_length=3, choices=YN_CHOICES, null=True, blank=True)
    technology_devices_specify = models.CharField(max_length=50, null=True, blank=True)
    house_number_and_street = models.CharField(max_length=50, null=True, blank=True)
    barangay = models.CharField(max_length=50)
    city_municipality = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    region = models.CharField(max_length=50)

    school_year1 = models.CharField(max_length=4, default='2020')
    school_year2 = models.CharField(max_length=4, default='2021')
    wlrn = models.CharField(max_length=4, choices=YN_CHOICES)
    returning = models.CharField(max_length=4, choices=YN_CHOICES)
    grade_level_to_enroll = models.CharField(max_length=50, choices=GRADE_CHOICES)
    last_grade_level_com = models.CharField(max_length=50)
    last_school_year_com = models.CharField(max_length=20, default='2020')
    last_school_attended = models.CharField(max_length=200)
    school_id = models.CharField(max_length= 50)
    school_address = models.CharField(max_length= 200)
    school_type = models.CharField(max_length=8, choices=SCHOOLTYPE_CHOICES)
    school_to_enroll_in = models.CharField(max_length=200)
    school_id_to_enroll = models.CharField(max_length=50)
    school_address_to_enroll = models.CharField(max_length= 200)
    semester = models.CharField(max_length=4, choices=SEMESTER_CHOICES)
    track = models.CharField(max_length=100, choices= TRACK_CHOICES, null=True, blank=True)
    strand = models.CharField(max_length=100, choices= STRAND_CHOICES)

    father_full_name = models.CharField(max_length=100, null=True, blank=True)
    father_educ_attainment = models.CharField(max_length=50, choices= EDUCATTAIN_CHOICES, null=True, blank=True)
    father_employment_status = models.CharField(max_length=50, null=True, blank=True)
    father_working_from_home_due_to_ecq = models.CharField(max_length=3, choices=YN_CHOICES, null=True, blank=True)
    father_contact = models.CharField(max_length=13, null=True, blank=True)
    mother_full_name = models.CharField(max_length=100, null=True, blank=True)
    mother_educ_attainment = models.CharField(max_length=50, choices= EDUCATTAIN_CHOICES, null=True, blank=True)
    mother_employment_status = models.CharField(max_length=50, null=True, blank=True)
    mother_working_from_home_due_to_ecq = models.CharField(max_length=3, choices=YN_CHOICES, null=True, blank=True)
    mother_contact = models.CharField(max_length=13, null=True, blank=True)
    guardian_full_name = models.CharField(max_length=100, null=True, blank=True)
    guardian_educ_attainment = models.CharField(max_length=50, choices= EDUCATTAIN_CHOICES, null=True, blank=True)
    guardian_employment_status = models.CharField(max_length=50, null=True, blank=True)
    guardian_working_from_home_due_to_ecq = models.CharField(max_length=3, choices=YN_CHOICES, null=True, blank=True)
    guardian_contact = models.CharField(max_length=13, null=True, blank=True)

    d1_walking = models.BooleanField(null=True, blank=True)
    d1_public_commute_landwater = models.BooleanField(null=True, blank=True)
    d1_family_owned_vehicle = models.BooleanField(null=True, blank=True)
    d1_school_service = models.BooleanField(null=True, blank=True)

    kinder = models.CharField(max_length=3, null=True, blank=True)
    grade_1 = models.CharField(max_length=3, null=True, blank=True)
    grade_2 = models.CharField(max_length=3, null=True, blank=True)
    grade_3 = models.CharField(max_length=3, null=True, blank=True)
    grade_4 = models.CharField(max_length=3, null=True, blank=True)
    grade_5 = models.CharField(max_length=3, null=True, blank=True)
    grade_6 = models.CharField(max_length=3, null=True, blank=True)
    grade_7 = models.CharField(max_length=3, null=True, blank=True)
    grade_8 = models.CharField(max_length=3, null=True, blank=True)
    grade_9 = models.CharField(max_length=3, null=True, blank=True)
    grade_10 = models.CharField(max_length=3, null=True, blank=True)
    grade_11 = models.CharField(max_length=3, null=True, blank=True)
    grade_12 = models.CharField(max_length=3, null=True, blank=True)
    others = models.CharField(max_length=3, null=True, blank=True)

    d3_parents_or_guardians = models.BooleanField(null=True, blank=True)
    d3_elder_siblings = models.BooleanField(null=True, blank=True)
    d3_grandparents = models.BooleanField(null=True, blank=True)
    d3_extended_members = models.BooleanField(null=True, blank=True)
    d3_others = models.BooleanField(null=True, blank=True)
    d3_none = models.BooleanField(null=True, blank=True)
    d3_independent = models.BooleanField(null=True, blank=True)

    d4_cable_tv = models.BooleanField(null=True, blank=True)
    d4_noncable_tv = models.BooleanField(null=True, blank=True)
    d4_basic_cp = models.BooleanField(null=True, blank=True)
    d4_smartphone = models.BooleanField(null=True, blank=True)
    d4_tablet = models.BooleanField(null=True, blank=True)
    d4_radio = models.BooleanField(null=True, blank=True)
    d4_desktop = models.BooleanField(null=True, blank=True)
    d4_laptop = models.BooleanField(null=True, blank=True)
    d4_none = models.BooleanField(null=True, blank=True)
    d4_others = models.CharField(max_length=20, null=True, blank=True)

    have_internet = models.CharField(max_length=20, null=True, blank=True, choices=YN_CHOICES)

    d6_own_mobile_data = models.BooleanField(null=True, blank=True)
    d6_own_broadband_internet = models.BooleanField(null=True, blank=True)
    d6_computer_shop = models.BooleanField(null=True, blank=True)
    d6_other_places = models.BooleanField(null=True, blank=True)
    d6_none = models.BooleanField(null=True, blank=True)

    d7_ol_learning = models.BooleanField(null=True, blank=True)
    d7_tv = models.BooleanField(null=True, blank=True)
    d7_radio = models.BooleanField(null=True, blank=True)
    d7_modular = models.BooleanField(null=True, blank=True)
    d7_f2f_w_modalities = models.BooleanField(null=True, blank=True)
    d7_others = models.CharField(max_length=20, null=True, blank=True)

    d8_lack_gadgets = models.BooleanField(null=True, blank=True)
    d8_insufficient_load = models.BooleanField(null=True, blank=True)
    d8_unstable_internet = models.BooleanField(null=True, blank=True)
    d8_health_conditions = models.BooleanField(null=True, blank=True)
    d8_difficulty_independent_learning = models.BooleanField(null=True, blank=True)
    d8_con_other_activities = models.BooleanField(null=True, blank=True)
    d8_hi_elec_consump = models.BooleanField(null=True, blank=True)
    d8_distractions = models.BooleanField(null=True, blank=True)
    d8_others = models.CharField(max_length=20, null=True, blank=True)

    certify = models.BooleanField(null=True, blank=True)

    date_enrol = models.DateTimeField(default=timezone.now)

    image = models.FileField(default='default.png', upload_to='student_pics', blank=True, null=True)
    form_137 = models.FileField(default='default.png', upload_to='form_137', blank=True, null=True)
    birth_certificate = models.FileField(default='default.png', upload_to='birth_certificate', blank=True, null=True)

    def __str__(self):
        return self.last_name + self.first_name

    def get_absolute_url(self):
        return reverse('stem:dlpdf')#update