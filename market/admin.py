from django.contrib import admin
from market.funcs import get_editable_fields, expand_list_unique, \
    get_existent_fields
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
        return list_display, list_editable, search_fields, list_display_links, fieldsets
    def get_actions(self, request):
        actions = super(CAM, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
#End common admin model

#Start admin models
class PersonAdmin(CAM):
    fieldsets = [
        (None,                {'fields': [('name', 'user'), ]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets = CAM.gim(Person, ['name', 'user'], fieldsets)


class ContactDetailsAdmin(CAM):
    # list_filter = ['operator', 'package_type', 'po_term__is_active']
    fieldsets = [
        (None,                {'fields': [('person', 'email', 'phone', )]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets = CAM.gim(ContactDetails, ['person', 'email', 'phone'], fieldsets)

class BrandAdmin(CAM):
    # list_filter = ['operator', 'package_type', 'po_term__is_active']
    fieldsets = [
        (None,                {'fields': [(('name', 'owner'), ('contract', 'site_address'), )]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets = CAM.gim(Brand, ['name', 'owner', 'site_address', 'contract'], fieldsets)

class ShopAdmin(CAM):
    # list_filter = ['operator', 'package_type', 'po_term__is_active']
    fieldsets = [
        (None,                {'fields': [(('name', 'brand'), ('owner', 'address'), ('working_days', 'working_hours'), )]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets = CAM.gim(Shop, ['name', 'brand', 'owner', 'address', 'working_days', 'working_hours'], fieldsets)

class ItemTypeAdmin(CAM):
    # list_filter = ['operator', 'package_type', 'po_term__is_active']
    fieldsets = [
        (None,                {'fields': [('name', 'category', )]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets = CAM.gim(ItemType, ['name', 'category_m2m'], fieldsets)

class CategoryAdmin(CAM):
    # list_filter = ['operator', 'package_type', 'po_term__is_active']
    fieldsets = [
        (None,                {'fields': [(('name', 'parent'), )]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets = CAM.gim(Category, ['name', 'parent'], fieldsets)

class ItemAdmin(CAM):
    fieldsets = [
        (None,                {'fields': [(('type', 'shop'), ('quantity', 'price'))]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets = CAM.gim(Item, ['type', 'shop', 'quantity', 'price'], fieldsets)

class CharacteristicAdmin(CAM):
    fieldsets = [
        (None,                {'fields': [(('name', 'item_type', 'measurement'),)]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets = CAM.gim(Characteristic, ['name', 'item_type_m2m', 'measurement'], fieldsets)

class MeasurementAdmin(CAM):
    fieldsets = [
        (None,                {'fields': [(('name', 'compared_to', 'multiplier'),)]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets = CAM.gim(Measurement, ['name', 'compared_to', 'multiplier'], fieldsets)

class OrderAdmin(CAM):
    fieldsets = [
        (None,                {'fields': [(('customer', 'delivery', 'payment'),)]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets = CAM.gim(Order, ['customer', 'delivery', 'payment'], fieldsets)

class OrderItemAdmin(CAM):
    fieldsets = [
        (None,                {'fields': [(('item', 'quantity'),('price', 'order'))]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets = CAM.gim(OrderItem, ['item', 'quantity', 'price', 'order'], fieldsets)

class DeliveryAdmin(CAM):
    fieldsets = [
        (None,                {'fields': [(('price', 'details'),)]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets = CAM.gim(Delivery, ['price', 'details'], fieldsets)

class DeliveryDetailsAdmin(CAM):
    fieldsets = [
        (None,                {'fields': [(('address', 'phone'), 'delivery_when')]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets = CAM.gim(DeliveryDetails, ['address', 'phone', 'delivery_when'], fieldsets)

class PaymentAdmin(CAM):
    fieldsets = [
        (None,                {'fields': [(('type', 'amount'),)]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets = CAM.gim(Delivery, ['type', 'amount'], fieldsets)

class PaymentTypeAdmin(CAM):
    fieldsets = [
        (None,                {'fields': [('name')]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets = CAM.gim(DeliveryDetails, ['name'], fieldsets)

class DirectoryAdmin(CAM):
    list_filter = ('updated_when', )
    fieldsets = [
        (None,                {'fields': [('key', 'value', ), ]}),
    ]
    list_display, list_editable, search_fields, list_display_links, fieldsets = CAM.gim(Directory, ['key', 'value', 'updated_when'], fieldsets)

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

