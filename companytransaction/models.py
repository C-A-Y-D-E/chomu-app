# this is models.py file for companytransactions which consists of transaction tables
from django.db import models
from companymaster.models import Filing, Company, Exchange, Fundparty, Country, Industry, CompanyOfferings, Currency, OfferStatus, IPOStatus, ListingStatus, ListingType
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone

class Offering(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    offering = models.ForeignKey(CompanyOfferings, on_delete=models.PROTECT)
    is_reviewed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.company}'

    class Meta:
        verbose_name = "Offering"
        verbose_name_plural = "Offerings"


class CompanyExchange(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    exchange = models.ForeignKey(Exchange, on_delete=models.PROTECT)
    exchange_country = models.ForeignKey(Country, on_delete=models.PROTECT,null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.exchange}'

    class Meta:
        verbose_name = "CompanyExchange"
        verbose_name_plural = "CompanyExchanges"


class CompanyCountry(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.company}'

    class Meta:
        verbose_name = "CompanyCountry"
        verbose_name_plural = "CompanyCountries"


class IndustryCompany(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    industry = models.ForeignKey(Industry, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.company}'

    class Meta:
        verbose_name = "IndustryCompany"
        verbose_name_plural = "IndustryCompanies"


class CompanyOfferingShares(models.Model):
    company_offering = models.ForeignKey(Offering, on_delete=models.PROTECT, null=True)    
    shares_offered_min = models.DecimalField(
        max_digits=30, decimal_places=8, null=True, blank=True)
    shares_offered_max = models.DecimalField(
        max_digits=30, decimal_places=8, null=True, blank=True)
    shares_offered_flag = models.BooleanField(null=True)
    strategic_shares_offered = models.DecimalField(
        max_digits=30, decimal_places=8, null=True, blank=True)
    additional_shares_offered_aboveIPO = models.DecimalField(
        max_digits=30, decimal_places=8, null=True, blank=True)
    offer_amount_min = models.DecimalField(
        max_digits=30, decimal_places=8, null=True, blank=True)
    offer_amount_max = models.DecimalField(
        max_digits=30, decimal_places=8, null=True, blank=True)
    offer_amount_flag = models.BooleanField(null=True)
    price_range_min = models.DecimalField(
        max_digits=30, decimal_places=8, null=True, blank=True)
    price_range_max = models.DecimalField(
        max_digits=30, decimal_places=8, null=True, blank=True)
    underwriting_discount = models.CharField(max_length=255, null=True)
    proceeds_after_expense = models.CharField(max_length=255, null=True)
    shares_outstanding = models.DecimalField(
        max_digits=30, decimal_places=8, null=True, blank=True)
    shareholder_shares_offered = models.DecimalField(
        max_digits=30, decimal_places=8, null=True, blank=True)
    lockup_period = models.DecimalField(
        max_digits=30, decimal_places=8, null=True, blank=True)
    lockup_expiration_date = models.DateField(null=True, blank=True)
    quiet_period_expiration_date = models.DateField(null=True, blank=True)
    number_of_shares_issued = models.DecimalField(
        max_digits=30, decimal_places=8, null=True, blank=True)
    strategic_sale_offer_that_were_issued = models.DecimalField(
        max_digits=30, decimal_places=8, null=True, blank=True)
    greenshoe_option_exercise_date = models.DateField(null=True, blank=True)
    number_of_greenshoe_shares_issued = models.DecimalField(
        max_digits=30, decimal_places=8, null=True, blank=True)
    shares_overalloted = models.DecimalField(
        max_digits=30, decimal_places=8, null=True, blank=True)
    snapshot_date = models.DateField(null=True, blank=True)
    prospectus_link = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.offering}'

    class Meta:
        verbose_name = "CompanyOfferingShare"
        verbose_name_plural = "CompanyOfferingShares"


class CompanyOfferingStatus(models.Model):
    company_offering = models.ForeignKey(Offering, on_delete=models.PROTECT, null=True)    
    listing_status = models.ForeignKey(ListingStatus, on_delete=models.PROTECT,null=True, blank=True)
    snapshot_date = models.DateField(null=True, blank=True)
    IPO_status = models.ForeignKey(IPOStatus, on_delete=models.PROTECT,null=True, blank=True)
    offer_status = models.ForeignKey(OfferStatus, on_delete=models.PROTECT,null=True, blank=True)
    type_of_listing = models.ForeignKey(ListingType, on_delete=models.PROTECT,null=True, blank=True)
    offering_announcement_date = models.DateField(null=True, blank=True)
    offering_price_announcement_date = models.DateField(null=True, blank=True)
    offering_start_date = models.DateField(null=True, blank=True)
    offering_end_date = models.DateField(null=True, blank=True)
    snapshot_date = models.DateField(null=True, blank=True)
    share_issue_date = models.DateField(null=True, blank=True)
    date_of_listing = models.DateField(null=True, blank=True)
    withdrawn_date = models.DateField(null=True, blank=True)
    postpone_date = models.DateField(null=True, blank=True)
    use_of_proceeds = models.CharField(max_length=1000, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.offering}'

    class Meta:
        verbose_name = "CompanyOfferingStatus"
        verbose_name_plural = "CompanyOfferingStatus"


class CompanyFinancial(models.Model):
    company_offering = models.ForeignKey(Offering, on_delete=models.PROTECT, null=True) 
    snapshot_date = models.DateField(null=True, blank=True)
    revenue = models.DecimalField(
        max_digits=30, decimal_places=8, null=True, blank=True)
    net_income = models.DecimalField(
        max_digits=30, decimal_places=8, null=True, blank=True)
    ebit = models.DecimalField(
        max_digits=30, decimal_places=8, null=True, blank=True)
    ebitda = models.DecimalField(
        max_digits=30, decimal_places=8, null=True, blank=True)
    y_o_y_growth = models.DecimalField(
        max_digits=30, decimal_places=8, null=True, blank=True)
    last_12_months_sales = models.DecimalField(
        max_digits=30, decimal_places=8, null=True, blank=True)
    last_24_months_sales = models.DecimalField(
        max_digits=30, decimal_places=8, null=True, blank=True)
    total_liabilities = models.DecimalField(
        max_digits=30, decimal_places=8, null=True, blank=True)
    cash = models.DecimalField(
        max_digits=30, decimal_places=8, null=True, blank=True)
    debt = models.DecimalField(
        max_digits=30, decimal_places=8, null=True, blank=True)
    equity = models.DecimalField(
        max_digits=30, decimal_places=8, null=True, blank=True)
    total_assets = models.DecimalField(
        max_digits=30, decimal_places=8, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.offering}'

    class Meta:
        verbose_name = "CompanyFinancial"
        verbose_name_plural = "CompanyFinancials"


class CompanyOfferingFeesExpense(models.Model):
    company_offering = models.ForeignKey(Offering, on_delete=models.PROTECT, null=True)    
    snapshot_date = models.DateField(null=True, blank=True)
    registeration_fee = models.DecimalField(max_digits=30, decimal_places=8, null=True, blank=True)
    type_of_equity_instrument = models.CharField(max_length=255, null=True, blank=True)
    security_description = models.CharField(max_length=500, null=True, blank=True)
    warants_issued = models.DecimalField(max_digits=30, decimal_places=8, null=True, blank=True)
    ex_price_of_warants = models.DecimalField(max_digits=30, decimal_places=8, null=True, blank=True)
    total_offering_expense = models.DecimalField(max_digits=30, decimal_places=8, null=True, blank=True)
    legal_fees_expenses = models.DecimalField(max_digits=30, decimal_places=8, null=True, blank=True)
    security_parvalue = models.DecimalField(max_digits=30, decimal_places=8, null=True, blank=True)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT, null=True, blank=True)
    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    created_date = models.DateTimeField(editable=False, null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True, editable=True)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.offering}'

    class Meta:
        verbose_name = "CompanyOfferingFeesExpense"
        verbose_name_plural = "CompanyOfferingFeesExpenses"


class CompanyRepresentative(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    representative_name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=True)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Updated By",
                                   blank=True, related_name="company_updated_by", default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.company}'

    class Meta:
        verbose_name = "CompanyRepresentative"
        verbose_name_plural = "CompanyRepresentatives"


class CompanyKeyshareholder(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    keyshareholders_name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.company}'

    class Meta:
        verbose_name = "CompanyKeyshareholder"
        verbose_name_plural = "CompanyKeyshareholders"


class FundpartyLeadUnderwiter(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    fundparty = models.ForeignKey(Fundparty, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=True)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Updated By",
                                   blank=True, related_name="lead_underwiter_updated_by", default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.company}'

    class Meta:
        verbose_name = "FundpartyLeadUnderwiter"
        verbose_name_plural = "FundpartyLeadUnderwiters"


class FundPartyUnderwriter(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    fundparty = models.ForeignKey(Fundparty, on_delete=models.PROTECT)
    offering = models.ForeignKey(
        CompanyOfferings, on_delete=models.PROTECT, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.company}'

    class Meta:
        verbose_name = "Underwriter"
        verbose_name_plural = "Underwriters"


class FundpartyUnderwiterCouncel(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    fundparty = models.ForeignKey(Fundparty, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.company}'

    class Meta:
        verbose_name = "FundpartyUnderwiterCouncel"
        verbose_name_plural = "FundpartyUnderwiterCouncels"


class FundpartyAuditor(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    fundparty = models.ForeignKey(Fundparty, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.company}'

    class Meta:
        verbose_name = "FundpartyAuditor"
        verbose_name_plural = "FundpartyAuditors"


class FundpartyTransferAgent(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    fundparty = models.ForeignKey(Fundparty, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.company}'

    class Meta:
        verbose_name = "FundpartyTransferAgent"
        verbose_name_plural = "FundpartyTransferAgents"


class FundpartyCompanyCouncel(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    fundparty = models.ForeignKey(Fundparty, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.company}'

    class Meta:
        verbose_name = "FundpartyCompanyCouncel"
        verbose_name_plural = "FundpartyCompanyCouncels"


class CompanyFiling(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    filing = models.ForeignKey(Filing, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.company}'

    class Meta:
        verbose_name = "CompanyFiling"
        verbose_name_plural = "CompanyFilings"


class CompanyContact(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    website = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.company}'

    class Meta:
        verbose_name = "CompanyContact"
        verbose_name_plural = "CompanyContacts"


class CompanyCurrency(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.company}'

    class Meta:
        verbose_name = "CompanyCurrency"
        verbose_name_plural = "CompanyCurrencies"


class CompanyIndustry(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    industry = models.ForeignKey(Industry, on_delete=models.PROTECT)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(editable=False)
    updated_date = models.DateTimeField(null=True, blank=True, editable=True)
    updated_by = models.ForeignKey(
        User, on_delete=models.PROTECT, verbose_name="Updated By", blank=True, default=1)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.company}'

    class Meta:
        verbose_name = "CompanyIndustry"
        verbose_name_plural = "CompanyIndustries"