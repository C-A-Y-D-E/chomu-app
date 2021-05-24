#this is admin.py for companymaster (master tables)
from django.contrib import admin
from companymaster.models import Filing,Company,Currency,Exchange,Country,Industry,Fundparty,CompanyOfferings,OfferStatus,IPOStatus,ListingStatus,ListingType
from import_export.admin import ImportExportModelAdmin

class ImportExport(ImportExportModelAdmin, admin.ModelAdmin):
    pass


admin.site.register(Filing, ImportExport)
admin.site.register(Company, ImportExport)
admin.site.register(Currency, ImportExport)
admin.site.register(Exchange, ImportExport)
admin.site.register(Country, ImportExport)
admin.site.register(Industry, ImportExport)
admin.site.register(Fundparty, ImportExport)
admin.site.register(CompanyOfferings, ImportExport)
admin.site.register(OfferStatus, ImportExport)
admin.site.register(IPOStatus, ImportExport)
admin.site.register(ListingStatus, ImportExport)
admin.site.register(ListingType, ImportExport)
