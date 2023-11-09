from django.contrib import admin

class AdminSite(admin.AdminSite):
    site_title = 'Agropost'
    site_header = 'Agropost from Leaf Solutions'
    index_title = 'Agropost - Overview'

admin_site = AdminSite(name='AgropostAdmin')
admin.site = admin_site