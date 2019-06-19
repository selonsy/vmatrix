import xadmin 
from .models import Password

class PasswordAdmin(object):
    list_display = ('name', 'order_num')
    search_fields = ['order_num', ] 
    list_editable = ['order_num'] 
    list_filter = ['order_num']
        
xadmin.site.register(Password,PasswordAdmin)