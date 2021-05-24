#this is admin.py for company (master tables)
from django.contrib import admin
from companytransaction.models import CompanyExchange,CompanyCountry,Offering,IndustryCompany,CompanyOfferingShares,CompanyOfferingStatus,CompanyKeyshareholder,FundpartyUnderwiterCouncel,CompanyRepresentative,FundpartyLeadUnderwiter,CompanyFinancial,CompanyOfferingFeesExpense,FundpartyAuditor,FundpartyTransferAgent,FundpartyCompanyCouncel,CompanyFiling,CompanyContact,CompanyCurrency,FundPartyUnderwriter,CompanyIndustry

from import_export.admin import ImportExportModelAdmin

class ImportExport(ImportExportModelAdmin,admin.ModelAdmin):
    pass

admin.site.register(CompanyExchange, ImportExport)
admin.site.register(CompanyCountry, ImportExport)
admin.site.register(IndustryCompany, ImportExport)
admin.site.register(CompanyOfferingShares, ImportExport)
admin.site.register(CompanyOfferingStatus, ImportExport)
admin.site.register(CompanyFinancial, ImportExport)
admin.site.register(CompanyOfferingFeesExpense, ImportExport)
admin.site.register(Offering, ImportExport)
admin.site.register(CompanyRepresentative, ImportExport)
admin.site.register(CompanyKeyshareholder, ImportExport)
admin.site.register(FundpartyLeadUnderwiter, ImportExport)
admin.site.register(FundpartyUnderwiterCouncel, ImportExport)
admin.site.register(FundpartyAuditor, ImportExport)
admin.site.register(FundpartyTransferAgent, ImportExport)
admin.site.register(FundpartyCompanyCouncel,ImportExport)
admin.site.register(CompanyFiling,ImportExport)
admin.site.register(CompanyContact,ImportExport)
admin.site.register(CompanyCurrency,ImportExport)
admin.site.register(CompanyIndustry,ImportExport)
admin.site.register(FundPartyUnderwriter,ImportExport)