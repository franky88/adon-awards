from django.contrib import admin
from .models import Awardee, AwardTitle, CertBG, AdonLogo
# Register your models here.
admin.site.site_header = "ADONGROUP PAGES"
admin.site.register(Awardee)
admin.site.register(AwardTitle)
admin.site.register(CertBG)
admin.site.register(AdonLogo)
