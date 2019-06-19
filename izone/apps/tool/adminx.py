import xadmin 
from .models import ToolCategory, ToolLink
from django.conf import settings


# Register your models here.
if settings.TOOL_FLAG:
    # @admin.register(ToolLink)
    class ToolLinkAdmin(object):
        list_display = ('name', 'description', 'link', 'order_num','category')


    # @admin.register(ToolCategory)
    class ToolCategoryAdmin(object):
        list_display = ('name', 'order_num')
        search_fields = ['order_num', ] 
        list_editable = ['order_num'] 
        list_filter = ['order_num']
        
xadmin.site.register(ToolLink,ToolLinkAdmin)
xadmin.site.register(ToolCategory,ToolCategoryAdmin)