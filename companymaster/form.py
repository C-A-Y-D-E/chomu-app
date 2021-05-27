# this is form.py for all forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from django import forms
from bootstrap_datepicker_plus import DatePickerInput
from companymaster.models import PDFModel, Company, Industry, Exchange, Currency, Country, CompanyOfferings, OfferStatus, IPOStatus, ListingStatus, ListingType, Fundparty

from companytransaction.models import CompanyExchange, CompanyCountry, IndustryCompany, CompanyOfferingShares, CompanyFinancial, CompanyOfferingFeesExpense, Offering, CompanyRepresentative, CompanyKeyshareholder, FundPartyUnderwriter, CompanyCurrency, CompanyContact, CompanyFiling, FundpartyCompanyCouncel, FundpartyTransferAgent, FundpartyAuditor, FundpartyUnderwiterCouncel, CompanyRepresentative, FundpartyLeadUnderwiter
import datetime


class CompanyInfoForm(ModelForm):
    issuer_names = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'dtfc form-control'}))
    no_of_employees = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'dtfc form-control'}))
    currency = forms.ModelChoiceField(queryset=Currency.objects.all(
    ), widget=forms.Select(attrs={'class': 'dtfc selectpicker floating-select whe'}))
    establishment = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'dtfc form-control'}))
    country = forms.ModelChoiceField(queryset=Country.objects.all(
    ), widget=forms.Select(attrs={'class': 'dtfc selectpicker floating-select whe'}))
    industry = forms.ModelChoiceField(queryset=Industry.objects.all(
    ), widget=forms.Select(attrs={'class': 'dtfc selectpicker floating-select whe'}))
    business_description = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'dtfc form-control'}))
    address = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'dtfc form-control'}))
    financial = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'dtfc form-control'}))
    website = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'dtfc form-control'}))
    contact_no = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'dtfc form-control'}))
    exchange = forms.ModelChoiceField(queryset=Exchange.objects.all(
    ), widget=forms.Select(attrs={'class': 'dtfc selectpicker floating-select whe'}))
    country_exchange = forms.ModelChoiceField(queryset=Country.objects.all(
    ), widget=forms.Select(attrs={'class': 'dtfc selectpicker floating-select whe'}))
    symbol = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'dtfc form-control'}))
    CIK = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'dtfc form-control'}))
    ISIN = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'dtfc form-control'}))
    CUSIP = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'dtfc form-control'}))
    LEI = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'dtfc form-control'}))
    SEDOL = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'dtfc form-control'}))
    MIC_Code = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'dtfc form-control'}))
    MIC_Seg = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'dtfc form-control'}))
    SIC_Code = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'dtfc form-control'}))
    # pdf = forms.ModelChoiceField(queryset=PDFModel.objects.all().values_list(
    #     'path', 'filename'), widget=forms.Select(attrs={'class': 'dtfc selectpicker floating-select whe'}))
    pdf = forms.ChoiceField(choices=(PDFModel.objects.all().values_list(
        'path', 'filename')), widget=forms.Select(attrs={'class': 'dtfc selectpicker floating-select whe'}))
    page_no = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'dtfc form-control'}))

    class Meta:
        model = Company
        fields = ['company_name', 'no_of_employees', 'currency', 'establishment', 'country', 'industry', 'business_description', 'address', 'website',
                  'contact_no', 'exchange', 'country_exchange', 'SIC_Code', 'MIC_Seg', 'MIC_Code', 'SEDOL', 'LEI', 'CUSIP', 'ISIN', 'CIK', 'symbol']


class test(ModelForm):
    fund_long_name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Fund Long Name'}))

# This is fundparty_management form page 2


class FundPartyForm(ModelForm):

    company = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label=None, widget=forms.Select(
        attrs={'class': 'dtfc selectpicker floating-select whe', 'multiple data-live-search': 'true', 'data-max-options': '1'}))
    lead_underwriter = forms.ModelChoiceField(queryset=Fundparty.objects.all(), empty_label=None, widget=forms.Select(
        attrs={'class': 'dtfc selectpicker floating-select whe', 'multiple data-live-search': 'true', 'data-live-search-placeholder': 'Search'}))
    underwriter = forms.ModelChoiceField(queryset=Fundparty.objects.all(), empty_label=None, widget=forms.Select(
        attrs={'class': 'dtfc selectpicker floating-select whe', 'multiple data-live-search': 'true', 'data-live-search-placeholder': 'Search'}))
    u_counsel = forms.ModelChoiceField(queryset=Fundparty.objects.all(), empty_label=None, widget=forms.Select(
        attrs={'class': 'dtfc selectpicker floating-select whe', 'multiple data-live-search': 'true', 'data-live-search-placeholder': 'Search'}))
    auditors = forms.ModelChoiceField(queryset=Fundparty.objects.all(), empty_label=None, widget=forms.Select(
        attrs={'class': 'dtfc selectpicker floating-select whe', 'multiple data-live-search': 'true', 'data-live-search-placeholder': 'Search'}))
    director_nominee = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'dtfc form-control'}))
    director_nominee_description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    ceo = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'dtfc form-control'}))
    ceo_description = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 3}))
    cfo = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'dtfc form-control'}))
    cfo_description = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 3}))
    key_share_holder = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'dtfc form-control'}))
    key_share_holder_description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    transfer_agent = forms.ModelChoiceField(queryset=Fundparty.objects.all(), empty_label=None, widget=forms.Select(
        attrs={'class': 'dtfc selectpicker floating-select whe', 'multiple data-live-search': 'true', 'data-live-search-placeholder': 'Search'}))
    comp_counsel = forms.ModelChoiceField(queryset=Fundparty.objects.all(), empty_label=None, widget=forms.Select(
        attrs={'class': 'dtfc selectpicker floating-select whe', 'multiple data-live-search': 'true', 'data-live-search-placeholder': 'Search'}))
    chair_dir = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'dtfc form-control'}))
    chair_dir_description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
    directors = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'dtfc form-control'}))
    directors_description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))

    class Meta:
        model = Company
        fields = ['lead_underwriter', 'underwriter', 'u_counsel', 'auditors', 'director_nominee',
                  'key_share_holder', 'transfer_agent', 'comp_counsel', 'company_name']


# This is OfferingDetail form page 3
class OfferingDetail(ModelForm):
    company = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label=None, widget=forms.Select(
        attrs={'class': 'dtfc selectpicker floating-select whe', 'multiple data-live-search': 'true', 'data-max-options': '1'}))
    choice = forms.ModelChoiceField(queryset=CompanyOfferings.objects.all(
    ), empty_label=None, widget=forms.RadioSelect(attrs={'class': 'choice-field'}))
    snapshot_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d', attrs={
                                    'id': 'snapshot_date', 'placeholder': 'Select Date', 'class': 'dtfc form-control'}))
    use_of_Proceeds = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'dtfc form-control'}))
    listing_status = forms.ModelChoiceField(queryset=ListingStatus.objects.all(
    ), widget=forms.Select(attrs={'class': 'dtfc selectpicker floating-select whe'}))
    ipo_status = forms.ModelChoiceField(queryset=IPOStatus.objects.all(
    ), widget=forms.Select(attrs={'class': 'dtfc selectpicker floating-select whe'}))
    offer_status = forms.ModelChoiceField(queryset=OfferStatus.objects.all(
    ), widget=forms.Select(attrs={'class': 'dtfc selectpicker floating-select whe'}))
    type_of_listing = forms.ModelChoiceField(queryset=ListingType.objects.all(
    ), widget=forms.Select(attrs={'class': 'dtfc selectpicker floating-select whe'}))
    ipo_announcement_dt = forms.DateField(widget=DatePickerInput(
        format='%Y-%m-%d', attrs={'id': 'announcement_dt', 'placeholder': 'Select Date', 'class': 'dtfc form-control'}))
    ipo_pr_announcement_dt = forms.DateField(widget=DatePickerInput(
        format='%Y-%m-%d', attrs={'id': 'pr_announcement_dt', 'placeholder': 'Select Date', 'class': 'dtfc form-control'}))
    ipo_start_dt = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d', attrs={
                                   'id': 'ipo_start_dt', 'placeholder': 'Select Date', 'class': 'dtfc form-control'}))
    ipo_end_dt = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d', attrs={
                                 'id': 'ipo_end_dt', 'placeholder': 'Select Date', 'class': 'dtfc form-control'}))
    share_issue_dt = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d', attrs={
                                     'id': 'share_issue_dt', 'placeholder': 'Select Date', 'class': 'dtfc form-control'}))
    date_of_listing = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d', attrs={
                                      'id': 'date_of_listing', 'placeholder': 'Select Date', 'class': 'dtfc form-control'}))
    withdrawn_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d', attrs={
                                     'id': 'withdrawn_date', 'placeholder': 'Select Date', 'class': 'dtfc form-control'}))
    postpone_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d', attrs={
                                    'id': 'postpone_date', 'placeholder': 'Select Date', 'class': 'dtfc form-control'}))

    class Meta:
        model = Company
        fields = ['date_of_listing', 'share_issue_dt', 'ipo_end_dt', 'ipo_start_dt', 'ipo_pr_announcement_dt',
                  'ipo_announcement_dt', 'use_of_Proceeds', 'listing_status', 'ipo_status', 'offer_status', 'type_of_listing']


# This is OfferingDetail form page 4
class OffershareDetail(forms.Form):
    company = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label=None, widget=forms.Select(
        attrs={'class': 'dtfc selectpicker floating-select whe', 'multiple data-live-search': 'true', 'data-max-options': '1'}))
    offering = forms.ModelChoiceField(queryset=CompanyOfferings.objects.all(
    ), widget=forms.Select(attrs={'class': 'dtfc selectpicker floating-select whe'}))
    shares_offered_min = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'dtfc form-control'}))
    shares_offered_max = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'dtfc form-control'}))
    strategic_shares_off = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'dtfc form-control'}))
    add_sh_off_above_ipo = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'dtfc form-control'}))
    offer_amount_min = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'dtfc form-control'}))
    offer_amount_max = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'dtfc form-control'}))
    price_range_min = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'dtfc form-control'}))
    price_range_max = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'dtfc form-control'}))
    underwriting_discount = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'dtfc form-control'}))
    proceeds_after_expense = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'dtfc form-control'}))
    shares_outstanding = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'dtfc form-control'}))
    sh_shares_offered = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'dtfc form-control'}))
    registration_fee = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'dtfc form-control'}))
    typ_of_eq_instrument = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'dtfc form-control'}))
    security_description = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'dtfc form-control'}))
    warants_issued = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'dtfc form-control'}))
    lockup_period = forms.DateField(
        widget=forms.NumberInput(attrs={'class': 'dtfc form-control'}))
    lockup_expiration = forms.DateField(widget=DatePickerInput(
        format='%Y-%m-%d', attrs={'placeholder': 'Select Date', 'class': 'dtfc form-control'}))
    quiet_period_expiration = forms.DateField(widget=DatePickerInput(
        format='%Y-%m-%d', attrs={'placeholder': 'Select Date', 'class': 'dtfc form-control'}))
    no_of_shares_issued = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'dtfc form-control'}))
    shares_after_str = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'dtfc form-control'}))
    greenshoe_opt_exercise_dt = forms.DateField(widget=DatePickerInput(
        format='%Y-%m-%d', attrs={'placeholder': 'Select Date', 'class': 'dtfc form-control'}))
    no_of_grreenshoe_sh_iss = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'dtfc form-control'}))
    shares_overalloted = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'dtfc form-control'}))
    total_offering_exp = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'dtfc form-control'}))
    legal_fees_exp = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'dtfc form-control'}))
    security_parvalue = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'dtfc form-control'}))
    security_parvalue_curr = forms.ModelChoiceField(queryset=Currency.objects.all(
    ), widget=forms.Select(attrs={'class': 'dtfc selectpicker floating-select whe'}))
    ex_price_of_warants = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'dtfc form-control'}))
    prospectus_link = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'dtfc form-control'}))
    snapshot_date = forms.DateField(widget=DatePickerInput(
        format='%Y-%m-%d', attrs={'placeholder': 'Select Date', 'class': 'dtfc form-control'}))

# This is OfferingDetail form page 5


class FinancialDetail(forms.Form):
    company = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label=None, widget=forms.Select(
        attrs={'class': 'dtfc selectpicker floating-select whe', 'multiple data-live-search': 'true', 'data-max-options': '1'}))
    offering = forms.ModelChoiceField(queryset=CompanyOfferings.objects.all(
    ), widget=forms.Select(attrs={'class': 'dtfc selectpicker floating-select whe'}))
    date = forms.DateField(widget=DatePickerInput(
        format='%Y-%m-%d', attrs={'placeholder': 'Select Date', 'class': 'dtfc form-control'}))
    revenue = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'dtfc form-control'}))
    net_income = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'dtfc form-control'}))
    ebit = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'dtfc form-control'}))
    ebidta = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'dtfc form-control'}))
    y_o_y_growth = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'dtfc form-control'}))
    last_12_month_sales = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'dtfc form-control'}))
    last_24_month_sales = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'dtfc form-control'}))
    total_assets = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'dtfc form-control'}))
    total_liabilities = forms.CharField(
        widget=forms.NumberInput(attrs={'class': 'dtfc form-control'}))
    cash = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'dtfc form-control'}))
    debt = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'dtfc form-control'}))
    equity = forms.CharField(widget=forms.NumberInput(
        attrs={'class': 'dtfc form-control'}))

# class Meta:
#         model = Industry
#         fields = ['prospectus_link','ex_price_of_warants','security_parvalue_curr','security_parvalue','legal_fees_exp','total_offering_exp','shares_overalloted','no_of_grreenshoe_sh_iss','greenshoe_opt_exercise_dt','shares_after_str','no_of_shares_issued','quiet_period_expiration','lockup_expiration','lockup_period','warants_issued','security_description','typ_of_eq_instrument','registration_fee','sh_shares_offered','shares_outstanding','proceeds_after_expense','underwriting_discount','price_range','offer_amount','add_sh_off_above_ipo','strategic_shares_off','shared_offered']


# class UserLoginForm(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super(UserLoginForm, self).__init__(*args, **kwargs)

#     username = forms.CharField(widget=forms.TextInput(
#         attrs={'class': 'un', 'placeholder': 'Username', 'id': 'hello'}))
#     password = forms.CharField(widget=forms.PasswordInput(
#         attrs={
#             'class': 'pass',
#             'placeholder': 'Password',
#             'id': 'hi',
#         }
# ))

# class ipo_search_form(ModelForm):

#     style = {"style":"white-space: nowrap; width: 150px; overflow: hidden;text-overflow: ellipsis; border: 1px solid #000000;"}
#     # to_date = forms.DateField(widget=DatePickerInput(format='%Y-%m-%d', attrs={'id': 'to_date','placeholder': 'To Date'})) #initial=timezone.now().date()- datetime.timedelta(2)
#     company_name = forms.ModelChoiceField(queryset = Company.objects.filter(is_active=1,is_deleted=0, client_id = 1).values_list('fund_family_name',flat=True),  widget=forms.Select(attrs={"data-placeholder":"company_name"}))
#     symbol = forms.ModelChoiceField(queryset = Company.objects.filter(is_active=1,is_deleted=0).values_list('instrument_type_name',flat=True),  widget=forms.Select(attrs={"data-placeholder":"symbol"}))
#     cik = forms.ModelChoiceField(queryset = Company.objects.filter(nav_threshold_percent__gt=0).values_list('asset_class_name',flat=True),  widget=forms.Select(attrs={"data-placeholder":"cik"}))
#     cusip = forms.ModelChoiceField(queryset = Company.objects.filter(is_active=1,is_deleted = 0).values_list('country_name',flat=True),  widget=forms.Select(attrs={"data-placeholder":"cusip"}))
#     isin = forms.ModelChoiceField(queryset = Company.objects.filter(is_active=1,is_deleted = 0).values_list('currency_name',flat=True),  widget=forms.Select(attrs={"data-placeholder":"isin"}))
#     sedol = forms.ModelChoiceField(queryset=Company.objects.filter(is_active=1, is_deleted = 0).values_list('status_name',flat=True), widget=forms.Select(attrs={"data-placeholder":"sedol"}))
#     mic_code = forms.ModelChoiceField(queryset=Company.objects.filter(is_active=1, is_deleted = 0).values_list('status_name',flat=True), widget=forms.Select(attrs={"data-placeholder":"mic_code"}))
#     lei = forms.ModelChoiceField(queryset=Company.objects.filter(is_active=1, is_deleted = 0).values_list('status_name',flat=True), widget=forms.Select(attrs={"data-placeholder":"lei"}))


#     class Meta:
#         model = Company
#         fields = ['company_name','symbol','cik','cusip','isin','sedol','mic_code','lei']


class CompanySearch(forms.Form):
    company = forms.ModelChoiceField(queryset=Company.objects.all(), empty_label=None, widget=forms.Select(
        attrs={'class': 'dtfc selectpicker floating-select whe', 'multiple data-live-search': 'true', 'data-max-options': '1'}))
    symbol = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'dtfc form-control'}))
    country = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'dtfc form-control'}))
    type_of_offer = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'dtfc form-control'}))
    cik = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'dtfc form-control'}))
    cusip = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'dtfc form-control'}))
    isin = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'dtfc form-control'}))
    lei = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'dtfc form-control'}))
    sedol = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'dtfc form-control'}))
    sic_code = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'dtfc form-control'}))
