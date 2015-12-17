from django.contrib import admin
from market.funcs import get_editable_fields, expand_list_unique, \
    get_existent_fields, get_readonly_fields
from .models import *

#Start common inline model
class CIM(admin.StackedInline):
    extra = 0
    show_change_link = True
    view_on_site = False
#End common inline model
#todo improve general perception and linkage of the admin pages
#TODO make [Save] button on top of the model list page
#Start inlines
# class OperatorPackageInline(CIM):
#     form = SmallLinkForm
#     model = Package
#     fieldsets = [(None, {'fields': [('name', 'package_type', 'link'), ('po_term', 'price')]}), ]
#End inlines

#Start common admin model
class CAM(admin.ModelAdmin):
    view_on_site = False
    save_on_top = True
    save_as = True
    list_per_page = 20
    def gim(in_model, in_list_display, in_fieldsets):#TODO re-write admin.register to include this logic
        list_display = expand_list_unique(['get_pk',], in_list_display, ['is_actual', 'remove', ])
        list_editable = [f.name for f in get_editable_fields(in_model, list_display)]
        search_fields = [f.name for f in get_existent_fields(in_model, ['name', ])]
        list_display_links = ['get_pk', ]
        fieldsets = in_fieldsets+[('Actuality', {'fields': ['is_actual', ('created_when', 'updated_when')]}), ('Extra', {'fields': ['description'], 'classes':['collapse']}),]
        readonly_fields = ['created_when', 'updated_when']
        return list_display, list_editable, search_fields, list_display_links, fieldsets, readonly_fields
    def get_actions(self, request):
        actions = super(CAM, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
#End common admin model

#Start admin models
class PersonAdmin(CAM):
    in_fieldsets = [
        (None,                {'fields': [('name', 'user')]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets, readonly_fields =  CAM.gim(Person, ['name', 'user'], in_fieldsets)


class ContactDetailsAdmin(CAM):
    # list_filter = ['operator', 'package_type', 'po_term__is_active']
    in_fieldsets = [
        (None,                {'fields': [('person', 'email', 'phone')]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets, readonly_fields =  CAM.gim(ContactDetails, ['person', 'email', 'phone'], in_fieldsets)

class BrandAdmin(CAM):
    # list_filter = ['operator', 'package_type', 'po_term__is_active']
    in_fieldsets = [
        (None,                {'fields': [('name', 'owner'), ('contract', 'site_address')]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets, readonly_fields =  CAM.gim(Brand, ['name', 'owner', 'site_address', 'contract'], in_fieldsets)

class ShopAdmin(CAM):
    # list_filter = ['operator', 'package_type', 'po_term__is_active']
    in_fieldsets = [
        (None,                {'fields': [('name', 'brand'), ('owner', 'address'), ('working_days', 'working_hours')]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets, readonly_fields =  CAM.gim(Shop, ['name', 'brand', 'owner', 'address', 'working_days', 'working_hours'], in_fieldsets)

class ItemTypeAdmin(CAM):
    # list_filter = ['operator', 'package_type', 'po_term__is_active']
    in_fieldsets = [
        (None,                {'fields': [('name', 'category', 'photo')]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets, readonly_fields =  CAM.gim(ItemType, ['name', 'category_m2m'], in_fieldsets)

class CategoryAdmin(CAM):
    # list_filter = ['operator', 'package_type', 'po_term__is_active']
    in_fieldsets = [
        (None,                {'fields': [('name', 'parent')]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets, readonly_fields =  CAM.gim(Category, ['name', 'parent'], in_fieldsets)

class ItemAdmin(CAM):
    in_fieldsets = [
        (None,                {'fields': [('type', 'shop'), ('quantity', 'price', 'photo')]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets, readonly_fields =  CAM.gim(Item, ['type', 'shop', 'quantity', 'price'], in_fieldsets)

class CharacteristicAdmin(CAM):
    in_fieldsets = [
        (None,                {'fields': [('name', 'item_type', 'measurement')]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets, readonly_fields =  CAM.gim(Characteristic, ['name', 'item_type_m2m', 'measurement'], in_fieldsets)

class MeasurementAdmin(CAM):
    in_fieldsets = [
        (None,                {'fields': [('name', 'compared_to', 'multiplier')]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets, readonly_fields =  CAM.gim(Measurement, ['name', 'compared_to', 'multiplier'], in_fieldsets)

class OrderAdmin(CAM):
    in_fieldsets = [
        (None,                {'fields': [('customer', 'delivery', 'payment')]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets, readonly_fields =  CAM.gim(Order, ['customer', 'delivery', 'payment'], in_fieldsets)

class OrderItemAdmin(CAM):
    in_fieldsets = [
        (None,                {'fields': [('item', 'quantity'), ('price', 'order')]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets, readonly_fields =  CAM.gim(OrderItem, ['item', 'quantity', 'price', 'order'], in_fieldsets)

class DeliveryAdmin(CAM):
    in_fieldsets = [
        (None,                {'fields': [('price', 'details')]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets, readonly_fields =  CAM.gim(Delivery, ['price', 'details'], in_fieldsets)

class DeliveryDetailsAdmin(CAM):
    in_fieldsets = [
        (None,                {'fields': [('address', 'phone'), 'delivery_when']}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets, readonly_fields =  CAM.gim(DeliveryDetails, ['address', 'phone', 'delivery_when'], in_fieldsets)

class PaymentAdmin(CAM):
    in_fieldsets = [
        (None,                {'fields': [('type', 'amount')]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets, readonly_fields =  CAM.gim(Delivery, ['type', 'amount'], in_fieldsets)

class PaymentTypeAdmin(CAM):
    in_fieldsets = [
        (None,                {'fields': [('name',)]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets, readonly_fields =  CAM.gim(DeliveryDetails, ['name'], in_fieldsets)

class DirectoryAdmin(CAM):
    list_filter = ('updated_when', )
    in_fieldsets = [
        (None,                {'fields': [('key', 'value')]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets, readonly_fields =  CAM.gim(Directory, ['key', 'value'], in_fieldsets)

admin.site.register(Person, PersonAdmin)
admin.site.register(ContactDetails, ContactDetailsAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(ItemType, ItemTypeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Characteristic, CharacteristicAdmin)
admin.site.register(Measurement, MeasurementAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Delivery, DeliveryAdmin)
admin.site.register(DeliveryDetails, DeliveryDetailsAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(PaymentType, PaymentTypeAdmin)
admin.site.register(Directory, DirectoryAdmin)

