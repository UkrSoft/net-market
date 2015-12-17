import datetime
from django.contrib.auth.models import User
from django.core.urlresolvers import NoReverseMatch, reverse
from django.db import models
from django.db.models import Count, Q
from django.utils.translation import gettext as _

class DescriptionModel(models.Model):
    description = models.TextField(blank = True, verbose_name=_("Description"), help_text=_("Any information which may be helpful to operate the current object."))
    created_when = models.DateTimeField(auto_now_add = True, verbose_name=_("Created When"), help_text=_("When current object was created."))
    updated_when = models.DateTimeField(auto_now = True, verbose_name=_("Updated When"), help_text=_("When current object was modified last time."))
    is_actual = models.BooleanField(default=True, verbose_name=_("Is Actual"), help_text=_("Designates whether this item should be taken into the account or not."))
    def get_admin_url(self):
        """
        Returns the admin URL to edit the object represented by this log entry.
        """
        if self._meta.app_label and self._meta.model_name:
            info = (self._meta.app_label, self._meta.model_name)
            try:
                return reverse('admin:%s_%s_change' % info, args=(self.pk,))
            except NoReverseMatch:
                pass
        return None
    def get_absolute_url(self):
        return self.get_admin_url()#'http://' + get_absolute_url() + self.get_admin_url()
    def get_absolute_url_link(self):
        return '<a href="%(link)s">%(text)s</a>' % {'link' : self.get_absolute_url(), 'text' : self.__str__()}
    get_absolute_url_link.description = 'URL'
    get_absolute_url_link.allow_tags = True
    def gab(self):#shortcut for self.get_absolute_url_link()
        return self.get_absolute_url_link()
    gab.short_description = _('Object')
    gab.allow_tags = True
    def get_pk(self):
        return self.pk
    get_pk.short_description = _('ID')
    def remove(self):
        return '<a class="inline-deletelink" title="delete" href="%s/delete/"></a>' % (self.pk)
    remove.short_description = ''
    remove.allow_tags = True
    class Meta:
        abstract = True

class Person(DescriptionModel):
    name = models.CharField(max_length=255, unique=True, verbose_name=_("Name"), help_text=_("Shop's owner name."))
    user = models.OneToOneField(User, verbose_name=_("User"), help_text = _('Login name.'))
    def __str__(self):
        return self.name
    def get_person_by_request(request):
        user = request.user
        person, created = Person.get_person_by_user(user)
        return user, person, created
    def get_person_by_user(user):
        return Person.objects.get_or_create(name = user.username, defaults={'user':user})
    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("People")
        ordering = ("name", )

class ContactDetails(DescriptionModel):
    email = models.EmailField(max_length=300, verbose_name=_("Email"), help_text=_("Email address."))
    phone = models.CharField(max_length=300, verbose_name=_("Phone"), help_text=_("Phone numbers."))
    person = models.ForeignKey('Person', verbose_name=_("Person"), help_text = _('Related person.'))
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _("Contact Detail")
        verbose_name_plural = _("Contact Details")
        ordering = ("person__name", )

class Brand(DescriptionModel):
    name = models.CharField(max_length=255, unique=True, verbose_name=_("Name"), help_text=_("Brand name."))
    site_address = models.CharField(max_length=300, blank=True, null=True, verbose_name=_("Site Address"), help_text=_("Link to the company's site (if any)."))
    contract = models.FileField(max_length=200, upload_to='static/contracts/', help_text=_("Contract with the current brand."))
    owner = models.ForeignKey('Person', verbose_name=_("Owner"), blank=True, null=True,
                                 help_text=_("Brand owner."))
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")
        unique_together = (("name", "owner"),)
        ordering = ('name', )

class Shop(DescriptionModel):
    name = models.CharField(max_length=500, verbose_name=_("Name"), help_text = _("Shop's name."))
    address = models.CharField(max_length=300, null=True, blank=True, verbose_name=_("Address"), help_text = _("Physical address of the shop."))
    working_days = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("Working days"), help_text = _("Days when the shop is open."))
    working_hours = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("Working hours"), help_text = _("Hours when the shop is open."))
    owner = models.ForeignKey('Person', verbose_name=_('Owner'),
                                     help_text=_("Owner of this shop."))
    brand = models.ForeignKey('Brand', verbose_name=_('Brand'), null = True, blank=True,
                                help_text=_("Brand this shop belongs to."))
    def __str__(self):
        return "%s - %s" % (self.name, self.address)
    class Meta:
        verbose_name = _("Shop")
        verbose_name_plural = _("Shops")
        unique_together = (("name", "address"),)
        ordering = ('owner__name', 'name', 'address', )

class ItemType(DescriptionModel):
    name = models.CharField(max_length=255, unique=True, verbose_name=_("Name"), help_text = _("Item's type name."))
    category = models.ManyToManyField('Category', verbose_name=_("Category"), help_text = _("Category for the current item type."))
    photo = models.FileField(max_length=200, null=True, blank=True, upload_to='static/photos/', help_text=_("Photo for the current item type."))
    def category_m2m(self):
        return ', '.join(c.__str__() for c in self.category.all())
    category_m2m.short_description = 'Category inline'
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _("Item Type")
        verbose_name_plural = _("Item Types")
        ordering = ('name', )

class Category(DescriptionModel):
    name = models.CharField(max_length=500, verbose_name=_("Name"), help_text = _("Category's name."))
    parent = models.ForeignKey('Category', blank=True, null=True, verbose_name=_("Parent category"), help_text = _("Parent category in the hierarchy."))
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ('parent__name', 'name', )
        unique_together = (('name', 'parent'), )

class Item(DescriptionModel):
    type = models.ForeignKey('ItemType', verbose_name=_("Item Type"), help_text=_("Type of the current item."))
    shop = models.ForeignKey('Shop', verbose_name=_("Shop"), help_text=_("Shop which is selling this item."))
    quantity = models.IntegerField(verbose_name=_("Quantity"), help_text=_("Amount of items available."))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"), help_text=_("Price for the item."))
    photo = models.FileField(max_length=200, null=True, blank=True, upload_to='static/photos/', help_text=_("Photo of the current item."))
    def __str__(self):
        return _("%(type)s from %(shop)s (%(quantity)s)") % {
            'type':self.type, 'shop':self.shop, 'quantity':self.quantity}
    class Meta:
        verbose_name = _("Item")
        verbose_name_plural = _("Items")
        ordering = ('type__name', 'quantity', )
        unique_together = (('type', 'shop', ),)

class Characteristic(DescriptionModel):
    name = models.CharField(max_length=300, verbose_name=_("Name"), help_text=_("Characteristic's name."))
    item_type = models.ManyToManyField('ItemType', verbose_name=_("Item Type"), help_text=_("Item type which should have this characteristic available."))
    measurement = models.ForeignKey('Measurement', verbose_name=_("Measurement units"), help_text=_("Units to measure characteristic's values."))
    def item_type_m2m(self):
        return ', '.join(i for i in self.item_type)
    def __str__(self):
        return _("%(name)s for the %(type)s") % {'name' : self.name, 'type' : self.item_type}
    class Meta:
        verbose_name = _("Characteristic")
        verbose_name_plural = _("Characteristics")
        ordering = ('name', )

class CValue(DescriptionModel):
    characteristic = models.ForeignKey('Characteristic', verbose_name=_("Characteristic"), help_text=_("Select characteristic."))
    value = models.CharField(max_length=300, verbose_name=_("Value"), help_text=_("Characteristic's value."))
    item = models.ForeignKey('Item', verbose_name=_("Item"), help_text=_("Linked item."))
    def __str__(self):
        return _("%(char)s = %(value)s for the %(item)s") % {'char' : self.characteristic, 'value' : self.value, 'item' : self.item}
    class Meta:
        verbose_name = _("Characteristic Value")
        verbose_name_plural = _("Characteristic Values")
        ordering = ('characteristic__name', 'item__name')

class Measurement(DescriptionModel):
    name = models.CharField(max_length=300, verbose_name="Name", help_text="Unit used for measurement")
    compared_to = models.ForeignKey('self', related_name="linked_unit", null=True, blank=True, verbose_name=_("Compared to unit"), help_text=_("If need to compare this unit to another one"))
    multiplier = models.FloatField(default=1, verbose_name=_("Multiply 'compared to unit'"), help_text=_("Multiplier used to compare to values (formula is : compared_to * multiplier = unit)"))
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _("Measurement Unit")
        verbose_name_plural = _("Measurement Units")
        ordering = ('name', )

class Order(DescriptionModel):
    customer = models.ForeignKey('Person', verbose_name=_("Customer"), help_text=_("Customer who made this order."))
    delivery = models.ForeignKey('Delivery', null=True, blank=True, verbose_name=_("Delivery"), help_text=_("Delivery details (if any)."))
    payment = models.ForeignKey('Payment', null=True, blank=True, verbose_name=_("Payment"), help_text=_("Payment details."))
    def __str__(self):
        return '%(customer)s - %(delivery)s' % {'customer':self.customer, 'delivery':self.delivery}
    def get_oi(self):
        self.optimize_items()
        return self.get_oi_no_optim()
    def get_oi_no_optim(self):
        return OrderItem.objects.filter(order = self, is_actual = True)
    def optimize_items(self):
        ois = self.get_oi_no_optim()
        for ois_item_v in ois.values('item').distinct():
            ois_item = ois.get(item__id = ois_item_v['item'])
            for ois_duplicate in ois.filter(~Q(id=ois_item.id), item = ois_item.item):
                ois_item.quantity += ois_duplicate.quantity
                ois_duplicate.delete()
            ois_item.save()
    def get_order_by_person(person):
        order, order_created = Order.objects.get_or_create(customer = person, is_actual = True)
        if (order.payment is not None and order.payment.is_actual):
            payment = order.payment
        else:
            payment = Payment.objects.create()
            order.payment = payment
            order.save()
        payment.recalculate()
        return order, order_created, payment
    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        ordering = ('customer__name', 'created_when', )

class OrderItem(DescriptionModel):
    item = models.ForeignKey('Item', verbose_name=_("Item"), help_text=_("Related order item."))
    quantity = models.IntegerField(default=1, verbose_name=_("Quantity"), help_text=_("Quantity of items in the basket."))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"), help_text=_("Price for each item."))
    order = models.ForeignKey('Order', verbose_name=_("Order"), help_text=_("Linked order."))
    def __str__(self):
        return _("%(order)s - %(item)s (%(quantity)s for %(price)s)") % {
            'order':self.order, 'item':self.item, 'price':self.price, 'quantity':self.quantity}
    def new_order_item(item, order, quantity):
        ois = order.get_oi().filter(item = item)
        if ois.count() > 0:
            oi = ois.first()
            oi.quantity += quantity
            oi.save()
            created = False
        else:
            oi = OrderItem.objects.create(item = item, price = item.price, order = order, quantity = quantity)
            created = True
        return oi, created
    def remove_order_item(item, order, quantity):
        ois = order.get_oi().get(item = item)
        ois_str = ois.__str__()
        if (ois.quantity > quantity):
            ois.quantity -= quantity
            removed = False
        else:
            ois.delete()
            removed = True
        return ois_str, removed
    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")
        ordering = ('created_when', )

class Delivery(DescriptionModel):
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"), help_text=_("Delivery price."))
    details = models.ForeignKey('DeliveryDetails', verbose_name=_("Details"), help_text=_("Current delivery details."))
    def __str__(self):
        return self.price
    class Meta:
        verbose_name = _("Delivery")
        verbose_name_plural = _("Deliveries")

class DeliveryDetails(DescriptionModel):
    address = models.CharField(max_length=300, verbose_name=_("Address"), help_text=_("Delivery address."))
    phone = models.CharField(max_length=300, verbose_name=_("Phone"), help_text=_("Phone numbers."))
    delivery_when = models.DateTimeField(verbose_name=_("Delivery when"), help_text=_("Expected date and time of delivery."))
    def __str__(self):
        return self.price
    class Meta:
        verbose_name = _("Delivery Detail")
        verbose_name_plural = _("Delivery Details")

class Payment(DescriptionModel):
    type = models.ForeignKey('PaymentType', default=1, verbose_name=_("Payment Type"), help_text=_("Type of payment."))
    amount = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name=_("Amount"), help_text=_("Price to pay fo the order."))
    def __str__(self):
        return _("%(type)s for %(amount)s") % {'type':self.type, 'amount':self.amount}
    def recalculate(self):
        order = Order.objects.get(payment = self, is_actual = True)
        self.amount = sum(oi.price*oi.quantity for oi in order.get_oi())
        self.save()
    class Meta:
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")
        ordering = ('type', )

class PaymentType(DescriptionModel):
    name = models.CharField(max_length=300, verbose_name=_("Payment Type"),
                                    help_text=_("Type of payment."))
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = _("Payment Type")
        verbose_name_plural = _("Payment Types")

class Directory(DescriptionModel):
    key = models.CharField(max_length=200, verbose_name=_("Key"), help_text=_("Name of the key"))
    value = models.TextField(verbose_name=_("Value"), help_text=_("Value of current key"))
    def get_name(self):
        return "%(key)s" % {'key' : self.key}
    class Meta:
        verbose_name = _("Directory")
        verbose_name_plural = _("Directory")
        ordering = ('key', 'updated_when', )

LOGGING_CHOICES = (
    (u'Success', _(u'Success')),
    (u'Info', _(u'Info')),
    (u'Warning', _(u'Warning')),
    (u'Danger', _(u'Danger')),
)

class Logging(DescriptionModel):
    level = models.CharField(max_length=30, default='Info', choices = LOGGING_CHOICES)
    message = models.CharField(max_length=500, verbose_name=_("Logging message"),
                                    help_text=_("Message to be outputted by logging engine."))
    user = models.ForeignKey(User, verbose_name=_("User"), help_text = _('Related user.'))
    times = models.IntegerField(default=1, verbose_name=_("Output times"), help_text = _('Amount of times to show message to user.'))
    till = models.DateTimeField(null=True, blank=True, verbose_name=_("Output till"), help_text = _('Show message till date and time.'))
    def add_entry(user, message, level='Warning', times=1, till=None):
        log = Logging.objects.create(user = user, level = level, message = message, times = times)
        if till is not None:
            log.till = till
        log.save()
        return log
    def get_entries(user):
        return Logging.objects.filter(user = user, is_actual = True)
    def output(self):
        if not self.is_actual():
            return
        if (self.times > 0):
            self.times -= 1
            return {'level':self.level, 'message':self.message}
    def is_actual(self):
        return self.times > 0 or (self.till is not None and self.till - datetime.now() > 0)
    class Meta:
        verbose_name = _("Logging entry")
        verbose_name_plural = _("Logging entries")