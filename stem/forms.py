from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import STUDENT_INFO


YN_CHOICES = [
        ('No', 'No'),
        ('Yes', 'Yes'),
    ]


MYN_CHOICES = [
        ('No (proceed to D7)', 'No (proceed to D7)'),
        ('Yes', 'Yes'),
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


GRADE_CHOICES = [
        ('Grade 11', 'Grade 11'),
        ('Grade 12', 'Grade 12'),
    ]


LGRADE_CHOICES = [
        ('Grade 6', 'Grade 6'),
        ('Grade 7', 'Grade 7'),
        ('Grade 8', 'Grade 8'),
        ('Grade 9', 'Grade 9'),
        ('Grade 10', 'Grade 10'),
        ('Grade 11', 'Grade 11'),
        ('Grade 12', 'Grade 12'),
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


EMPSTATUS_CHOICES = [
        ('Full time', 'Full time'),
        ('Part time', 'Part time'),
        ('Self employed', 'Self employed'),
        ('Unemployed due to ECQ', 'Unemployed due to ECQ'),
        ('Not working', 'Not working'),
    ]


YEARS= [x for x in range(1990,2020)]


class StudentRegisterForm(forms.ModelForm):
    school_year1 = forms.CharField(label='A1. School Year')
    school_year2 = forms.CharField(label='-----------')
    wlrn = forms.ChoiceField(label='A2. Has LRN', choices=YN_CHOICES)
    returning = forms.ChoiceField(label='A3. Returning (Balik eskwela)', choices=YN_CHOICES)
    grade_level_to_enroll = forms.ChoiceField(label='A4. Grade Level to Enroll', choices=GRADE_CHOICES)
    last_grade_level_com = forms.ChoiceField(label='A5. Last grade level completed', choices=LGRADE_CHOICES)
    last_school_year_com = forms.CharField(label='A6. Last school year completed')
    school_id_to_enroll = forms.CharField(label='A12. School ID')
    last_school_attended = forms.CharField(label='A7. Last School Attended')
    school_id = forms.CharField(label='A8. School ID')
    school_address = forms.CharField(label='A9. School Address')
    school_type = forms.ChoiceField(label='A10. School Type', choices=SCHOOLTYPE_CHOICES)
    school_to_enroll_in = forms.CharField(label='A11. School to enroll in')
    school_address_to_enroll = forms.CharField(label='A13. School Address')
    semester = forms.ChoiceField(label='A14. Semester', choices=SEMESTER_CHOICES)
    track = forms.ChoiceField(label='A15. Track', choices=TRACK_CHOICES)
    strand = forms.ChoiceField(label='A16. Strand', choices=STRAND_CHOICES, required=False)

    psa_cer_no = forms.CharField(label='B1. PSA Birth Certificate No. (if available upon enrolment)', required=False)
    lrn = forms.CharField(label='B2. Learners Reference Number (LRN)')
    last_name = forms.CharField(label='B3. Last Name')
    first_name = forms.CharField(label='B4. First Name')
    middle_name = forms.CharField(label='B5. Middle Name', required=False)
    extension_name = forms.CharField(label='B6. Extension Name', required=False)
    birthdate = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    age = forms.CharField(label='B8. Age')
    sex = forms.ChoiceField(label='B9. Sex', choices=SEX_CHOICES)
    ip = forms.ChoiceField(label='B10. Belonging to Indigenous People (IP)', choices=YN_CHOICES, required=False)
    ip_specify = forms.CharField(label='B11. If yes, please specify:', required=False)
    mother_tongue = forms.CharField(label='B12. Mother tongue', required=False)
    religion = forms.CharField(label='B13. Religion', required=False)
    special_ed_needs = forms.ChoiceField(label='B14. Does the learner have special education needs?', choices=YN_CHOICES, required=False)
    speed_needs_specify = forms.CharField(label='B15. If yes, please specify:', required=False)
    technology_devices = forms.ChoiceField(label='B16. Do you have any assistive technology devices available at home?', choices=YN_CHOICES, required=False)
    technology_devices_specify = forms.CharField(label='B17. If yes, please specify:', required=False)
    house_number_and_street = forms.CharField(label='B18. House number and street', required=False)
    barangay = forms.CharField(label='B19. Barangay')
    city_municipality = forms.CharField(label='B20. City/Municipality')
    province = forms.CharField(label='B21. Province')
    region = forms.CharField(label='B22. Region')
    
    father_full_name = forms.CharField(label='C1. Father Full name (surname, name, middle name)', required=False)
    father_educ_attainment = forms.ChoiceField(label='C2. Father Educational Attainment', choices=EDUCATTAIN_CHOICES, required=False)
    father_working_from_home_due_to_ecq = forms.ChoiceField(label='C4. Working from home due to_ECQ', choices=YN_CHOICES)
    mother_full_name = forms.CharField(label='C7. Mother Full name (surname, name, middle name)', required=False)
    mother_educ_attainment = forms.ChoiceField(label='C8. Mother Educational Attainment', choices=EDUCATTAIN_CHOICES, required=False)
    mother_working_from_home_due_to_ecq = forms.ChoiceField(label='C10. Working from home due to_ECQ', choices=YN_CHOICES)
    guardian_full_name = forms.CharField(label='C13. Guardian Full name (surname, name, middle name)', required=False)
    guardian_educ_attainment = forms.ChoiceField(label='C14. Guardian Educational Attainment', choices=EDUCATTAIN_CHOICES, required=False)
    guardian_working_from_home_due_to_ecq = forms.ChoiceField(label='C16. Working from home due to_ECQ', choices=YN_CHOICES)

    d1_walking = forms.BooleanField(label='Walking', required=False)
    d1_public_commute_landwater = forms.BooleanField(label='Public Commute (Land/water)', required=False)
    d1_family_owned_vehicle = forms.BooleanField(label='Family-owned vehicle', required=False)
    d1_school_service = forms.BooleanField(label='School service', required=False)

    kinder = forms.CharField(label='Kinder', required=False)
    grade_1 = forms.CharField(label='Grade 1', required=False)
    grade_2 = forms.CharField(label='Grade 2', required=False)
    grade_3 = forms.CharField(label='Grade 3', required=False)
    grade_4 = forms.CharField(label='Grade 4', required=False)
    grade_5 = forms.CharField(label='Grade 5', required=False)
    grade_6 = forms.CharField(label='Grade 6', required=False)
    grade_7 = forms.CharField(label='Grade 7', required=False)
    grade_8 = forms.CharField(label='Grade 8', required=False)
    grade_9 = forms.CharField(label='Grade 9', required=False)
    grade_10 = forms.CharField(label='Grade 10', required=False)
    grade_11 = forms.CharField(label='Grade 11', required=False)
    grade_12 = forms.CharField(label='Grade 12', required=False)
    others = forms.CharField(label='Others (ie college, vocational, etc)', required=False)

    d3_parents_or_guardians = forms.BooleanField(label='parents/ guardians', required=False)
    d3_elder_siblings = forms.BooleanField(label='elder siblings', required=False)
    d3_grandparents = forms.BooleanField(label='grandparents', required=False)
    d3_extended_members = forms.BooleanField(label='extended members of the family', required=False)
    d3_others = forms.BooleanField(label='others (tutor, house helper)', required=False)
    d3_none = forms.BooleanField(label='none', required=False)
    d3_independent = forms.BooleanField(label='able to do independent learning', required=False)
    
    d4_cable_tv = forms.BooleanField(label='cable TV', required=False)
    d4_noncable_tv = forms.BooleanField(label='non-cable TV', required=False)
    d4_basic_cp = forms.BooleanField(label='basic cellphone', required=False)
    d4_smartphone = forms.BooleanField(label='smartphone', required=False)
    d4_tablet = forms.BooleanField(label='tablet', required=False)
    d4_radio = forms.BooleanField(label='radio', required=False)
    d4_desktop = forms.BooleanField(label='desktop computer', required=False)
    d4_laptop = forms.BooleanField(label='laptop', required=False)
    d4_none = forms.BooleanField(label='none', required=False)
    d4_others = forms.CharField(label='others:', required=False)
    
    have_internet = forms.ChoiceField(label='D5. Do you have a way to connect to the internet?:', required=False, choices=MYN_CHOICES)
    
    d6_own_mobile_data = forms.BooleanField(label='own mobile data', required=False)
    d6_own_broadband_internet = forms.BooleanField(label='own broadband internet (DSL, wireless fiber, satellite)', required=False)
    d6_computer_shop = forms.BooleanField(label='computer shop', required=False)
    d6_other_places = forms.BooleanField(label='other places outside the home with internet connection (library, barangay/ municipal hall, neighbor, relatives)', required=False)
    d6_none = forms.BooleanField(label='none', required=False)
    
    d7_ol_learning = forms.BooleanField(label='online learning', required=False)
    d7_tv = forms.BooleanField(label='television', required=False)
    d7_radio = forms.BooleanField(label='radio', required=False)
    d7_modular = forms.BooleanField(label='modular learning', required=False)
    d7_f2f_w_modalities = forms.BooleanField(label='combination of face to face with other modalities', required=False)
    d7_others = forms.CharField(label='others:', required=False)

    d8_lack_gadgets = forms.BooleanField(label='lack of available gadgets/ equipment', required=False)
    d8_insufficient_load = forms.BooleanField(label='insufficient load/ data allowance', required=False)
    d8_unstable_internet = forms.BooleanField(label='unstable mobile/ internet connection', required=False)
    d8_health_conditions = forms.BooleanField(label=' existing health condition/s', required=False)
    d8_difficulty_independent_learning = forms.BooleanField(label='difficulty in independent learning', required=False)
    d8_con_other_activities = forms.BooleanField(label='conflict with other activities (i.e., house chores)', required=False)
    d8_hi_elec_consump = forms.BooleanField(label='high electrical consumption', required=False)
    d8_distractions = forms.BooleanField(label='distractions (i.e., social media, noise from community/ neighbor', required=False)
    d8_others = forms.CharField(label='others:', required=False)

    certify = forms.BooleanField(label='I hereby certify that the above information given are true and correct to the best of my knowledge and I allow the Department of Education to use my child’s details to create and/or update his/her learner profile in the Learner Information System. The information herein shall be treated as confidential in compliance with the Data Privacy Act of 2012.')

    image = forms.FileField(label='ID Picture', required=False)
    birth_certificate = forms.FileField(label='Birth Certificate', required=False)
    form_137 = forms.FileField(label='School Card')

    class Meta:
        model = STUDENT_INFO
        fields = [
            'school_year1',
            'school_year2',
            'wlrn',
            'returning',
            'grade_level_to_enroll',
            'last_grade_level_com',
            'last_school_year_com',
            'last_school_attended',
            'school_id',
            'school_address',
            'school_type',
            'school_to_enroll_in',
            'school_id_to_enroll',
            'school_address_to_enroll',
            'semester',
            'track',
            'strand',

            'psa_cer_no',
            'lrn',
            'last_name',
            'first_name',
            'middle_name',
            'extension_name',
            'birthdate',
            'age',
            'sex',
            'ip',
            'ip_specify',
            'mother_tongue',
            'religion',
            'special_ed_needs',
            'speed_needs_specify',
            'technology_devices',
            'technology_devices_specify',
            'house_number_and_street',
            'barangay',
            'city_municipality',
            'province',
            'region',
            
            'father_full_name',
            'father_educ_attainment',
            'father_employment_status',
            'father_working_from_home_due_to_ecq',
            'father_contact',
            'mother_full_name',
            'mother_educ_attainment',
            'mother_employment_status',
            'mother_working_from_home_due_to_ecq',
            'mother_contact',
            'guardian_full_name',
            'guardian_educ_attainment',
            'guardian_employment_status',
            'guardian_working_from_home_due_to_ecq',
            'guardian_contact',

            'd1_walking',
            'd1_public_commute_landwater',
            'd1_family_owned_vehicle',
            'd1_school_service',

            'kinder',
            'grade_1',
            'grade_2',
            'grade_3',
            'grade_4',
            'grade_5',
            'grade_6',
            'grade_7',
            'grade_8',
            'grade_9',
            'grade_10',
            'grade_11',
            'grade_12',
            'others',

            'd3_parents_or_guardians',
            'd3_elder_siblings',
            'd3_grandparents',
            'd3_extended_members',
            'd3_others',
            'd3_none',
            'd3_independent',

            'd4_cable_tv',
            'd4_noncable_tv',
            'd4_basic_cp',
            'd4_smartphone',
            'd4_tablet',
            'd4_radio',
            'd4_desktop',
            'd4_laptop',
            'd4_none',
            'd4_others',

            'have_internet',

            'd6_own_mobile_data',
            'd6_own_broadband_internet',
            'd6_computer_shop',
            'd6_other_places',
            'd6_none',

            'd7_ol_learning',
            'd7_tv',
            'd7_radio',
            'd7_modular',
            'd7_f2f_w_modalities',
            'd7_others',

            'd8_lack_gadgets',
            'd8_insufficient_load',
            'd8_unstable_internet',
            'd8_health_conditions',
            'd8_difficulty_independent_learning',
            'd8_con_other_activities',
            'd8_hi_elec_consump',
            'd8_distractions',
            'd8_others',

            'certify',

            'image',
            'form_137',
            'birth_certificate',
        ]


#update
class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']