# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.TextField(blank=True, help_text='Any information which may be helpful to operate the current object.', verbose_name='Description')),
                ('created_when', models.DateTimeField(auto_now_add=True, help_text='When current object was created.', verbose_name='Created When')),
                ('updated_when', models.DateTimeField(auto_now=True, help_text='When current object was updated last time.', verbose_name='Updated When')),
                ('is_actual', models.BooleanField(default=True, help_text='Designates whether this item should be taken into account or not.', verbose_name='Is Actual')),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Name', help_text='Brand name.')),
                ('site_address', models.CharField(blank=True, null=True, max_length=300, verbose_name='Site Address', help_text="Link to the company's site (if any).")),
                ('contract', models.FileField(max_length=200, help_text='Contract with the current brand.', upload_to='static/contracts/')),
            ],
            options={
                'verbose_name_plural': 'Brands',
                'ordering': ('name',),
                'verbose_name': 'Brand',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.TextField(blank=True, help_text='Any information which may be helpful to operate the current object.', verbose_name='Description')),
                ('created_when', models.DateTimeField(auto_now_add=True, help_text='When current object was created.', verbose_name='Created When')),
                ('updated_when', models.DateTimeField(auto_now=True, help_text='When current object was updated last time.', verbose_name='Updated When')),
                ('is_actual', models.BooleanField(default=True, help_text='Designates whether this item should be taken into account or not.', verbose_name='Is Actual')),
                ('name', models.CharField(max_length=500, verbose_name='Name', help_text="Category's name.")),
                ('parent', models.ForeignKey(verbose_name='Parent category', help_text='Parent category in the hierarchy.', to='market.Category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ('parent__name', 'name'),
                'verbose_name': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Characteristic',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.TextField(blank=True, help_text='Any information which may be helpful to operate the current object.', verbose_name='Description')),
                ('created_when', models.DateTimeField(auto_now_add=True, help_text='When current object was created.', verbose_name='Created When')),
                ('updated_when', models.DateTimeField(auto_now=True, help_text='When current object was updated last time.', verbose_name='Updated When')),
                ('is_actual', models.BooleanField(default=True, help_text='Designates whether this item should be taken into account or not.', verbose_name='Is Actual')),
                ('name', models.CharField(max_length=300, verbose_name='Name', help_text="Characteristic's name.")),
            ],
            options={
                'verbose_name_plural': 'Characteristics',
                'ordering': ('name',),
                'verbose_name': 'Characteristic',
            },
        ),
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.TextField(blank=True, help_text='Any information which may be helpful to operate the current object.', verbose_name='Description')),
                ('created_when', models.DateTimeField(auto_now_add=True, help_text='When current object was created.', verbose_name='Created When')),
                ('updated_when', models.DateTimeField(auto_now=True, help_text='When current object was updated last time.', verbose_name='Updated When')),
                ('is_actual', models.BooleanField(default=True, help_text='Designates whether this item should be taken into account or not.', verbose_name='Is Actual')),
                ('email', models.EmailField(max_length=300, verbose_name='Email', help_text='Email address.')),
                ('phone', models.CharField(max_length=300, verbose_name='Phone', help_text='Phone numbers.')),
            ],
            options={
                'verbose_name_plural': 'Contact Details',
                'ordering': ('person__name',),
                'verbose_name': 'Contact Detail',
            },
        ),
        migrations.CreateModel(
            name='CValue',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.TextField(blank=True, help_text='Any information which may be helpful to operate the current object.', verbose_name='Description')),
                ('created_when', models.DateTimeField(auto_now_add=True, help_text='When current object was created.', verbose_name='Created When')),
                ('updated_when', models.DateTimeField(auto_now=True, help_text='When current object was updated last time.', verbose_name='Updated When')),
                ('is_actual', models.BooleanField(default=True, help_text='Designates whether this item should be taken into account or not.', verbose_name='Is Actual')),
                ('value', models.CharField(max_length=300, verbose_name='Value', help_text="Characteristic's value.")),
                ('characteristic', models.ForeignKey(verbose_name='Characteristic', help_text='Select characteristic.', to='market.Characteristic')),
            ],
            options={
                'verbose_name_plural': 'Characteristic Values',
                'ordering': ('characteristic__name', 'item__name'),
                'verbose_name': 'Characteristic Value',
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.TextField(blank=True, help_text='Any information which may be helpful to operate the current object.', verbose_name='Description')),
                ('created_when', models.DateTimeField(auto_now_add=True, help_text='When current object was created.', verbose_name='Created When')),
                ('updated_when', models.DateTimeField(auto_now=True, help_text='When current object was updated last time.', verbose_name='Updated When')),
                ('is_actual', models.BooleanField(default=True, help_text='Designates whether this item should be taken into account or not.', verbose_name='Is Actual')),
                ('price', models.DecimalField(decimal_places=2, help_text='Delivery price.', verbose_name='Price', max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'Deliveries',
                'verbose_name': 'Delivery',
            },
        ),
        migrations.CreateModel(
            name='DeliveryDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.TextField(blank=True, help_text='Any information which may be helpful to operate the current object.', verbose_name='Description')),
                ('created_when', models.DateTimeField(auto_now_add=True, help_text='When current object was created.', verbose_name='Created When')),
                ('updated_when', models.DateTimeField(auto_now=True, help_text='When current object was updated last time.', verbose_name='Updated When')),
                ('is_actual', models.BooleanField(default=True, help_text='Designates whether this item should be taken into account or not.', verbose_name='Is Actual')),
                ('address', models.CharField(max_length=300, verbose_name='Address', help_text='Delivery address.')),
                ('phone', models.CharField(max_length=300, verbose_name='Phone', help_text='Phone numbers.')),
                ('delivery_when', models.DateTimeField(help_text='Expected date and time of delivery.', verbose_name='Delivery when')),
            ],
            options={
                'verbose_name_plural': 'Delivery Details',
                'verbose_name': 'Delivery Detail',
            },
        ),
        migrations.CreateModel(
            name='Directory',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.TextField(blank=True, help_text='Any information which may be helpful to operate the current object.', verbose_name='Description')),
                ('created_when', models.DateTimeField(auto_now_add=True, help_text='When current object was created.', verbose_name='Created When')),
                ('updated_when', models.DateTimeField(auto_now=True, help_text='When current object was updated last time.', verbose_name='Updated When')),
                ('is_actual', models.BooleanField(default=True, help_text='Designates whether this item should be taken into account or not.', verbose_name='Is Actual')),
                ('key', models.CharField(max_length=200, verbose_name='Key', help_text='Name of the key')),
                ('value', models.TextField(help_text='Value of current key', verbose_name='Value')),
            ],
            options={
                'verbose_name_plural': 'Directory',
                'ordering': ('key', 'updated_when'),
                'verbose_name': 'Directory',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.TextField(blank=True, help_text='Any information which may be helpful to operate the current object.', verbose_name='Description')),
                ('created_when', models.DateTimeField(auto_now_add=True, help_text='When current object was created.', verbose_name='Created When')),
                ('updated_when', models.DateTimeField(auto_now=True, help_text='When current object was updated last time.', verbose_name='Updated When')),
                ('is_actual', models.BooleanField(default=True, help_text='Designates whether this item should be taken into account or not.', verbose_name='Is Actual')),
                ('quantity', models.IntegerField(help_text='Amount of items available.', verbose_name='Quantity')),
                ('price', models.DecimalField(decimal_places=2, help_text='Price for the item.', verbose_name='Price', max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'Items',
                'ordering': ('type__name', 'quantity'),
                'verbose_name': 'Item',
            },
        ),
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.TextField(blank=True, help_text='Any information which may be helpful to operate the current object.', verbose_name='Description')),
                ('created_when', models.DateTimeField(auto_now_add=True, help_text='When current object was created.', verbose_name='Created When')),
                ('updated_when', models.DateTimeField(auto_now=True, help_text='When current object was updated last time.', verbose_name='Updated When')),
                ('is_actual', models.BooleanField(default=True, help_text='Designates whether this item should be taken into account or not.', verbose_name='Is Actual')),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Name', help_text="Item's type name.")),
                ('category', models.ManyToManyField(help_text='Category for the current item type.', verbose_name='Category', to='market.Category')),
            ],
            options={
                'verbose_name_plural': 'Item Types',
                'ordering': ('name',),
                'verbose_name': 'Item Type',
            },
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.TextField(blank=True, help_text='Any information which may be helpful to operate the current object.', verbose_name='Description')),
                ('created_when', models.DateTimeField(auto_now_add=True, help_text='When current object was created.', verbose_name='Created When')),
                ('updated_when', models.DateTimeField(auto_now=True, help_text='When current object was updated last time.', verbose_name='Updated When')),
                ('is_actual', models.BooleanField(default=True, help_text='Designates whether this item should be taken into account or not.', verbose_name='Is Actual')),
                ('name', models.CharField(max_length=300, verbose_name='Name', help_text='Unit used for measurement')),
                ('multiplier', models.FloatField(default=1, help_text='Multiplier used to compare to values (formula is : compared_to * multiplier = unit)', verbose_name="Multiply 'compared to unit'")),
                ('compared_to', models.ForeignKey(related_name='linked_unit', verbose_name='Compared to unit', help_text='If need to compare this unit to another one', blank=True, null=True, to='market.Measurement')),
            ],
            options={
                'verbose_name_plural': 'Measurement Units',
                'ordering': ('name',),
                'verbose_name': 'Measurement Unit',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.TextField(blank=True, help_text='Any information which may be helpful to operate the current object.', verbose_name='Description')),
                ('created_when', models.DateTimeField(auto_now_add=True, help_text='When current object was created.', verbose_name='Created When')),
                ('updated_when', models.DateTimeField(auto_now=True, help_text='When current object was updated last time.', verbose_name='Updated When')),
                ('is_actual', models.BooleanField(default=True, help_text='Designates whether this item should be taken into account or not.', verbose_name='Is Actual')),
            ],
            options={
                'verbose_name_plural': 'Orders',
                'ordering': ('customer__name', 'created_when'),
                'verbose_name': 'Order',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.TextField(blank=True, help_text='Any information which may be helpful to operate the current object.', verbose_name='Description')),
                ('created_when', models.DateTimeField(auto_now_add=True, help_text='When current object was created.', verbose_name='Created When')),
                ('updated_when', models.DateTimeField(auto_now=True, help_text='When current object was updated last time.', verbose_name='Updated When')),
                ('is_actual', models.BooleanField(default=True, help_text='Designates whether this item should be taken into account or not.', verbose_name='Is Actual')),
                ('quantity', models.IntegerField(help_text='Quantity of items in the basket.', verbose_name='Quantity')),
                ('price', models.DecimalField(decimal_places=2, help_text='Price for each item.', verbose_name='Price', max_digits=10)),
                ('item', models.ForeignKey(verbose_name='Item', help_text='Related order item.', to='market.Item')),
                ('order', models.ForeignKey(verbose_name='Order', help_text='Linked order.', to='market.Order')),
            ],
            options={
                'verbose_name_plural': 'Order Items',
                'ordering': ('created_when',),
                'verbose_name': 'Order Item',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.TextField(blank=True, help_text='Any information which may be helpful to operate the current object.', verbose_name='Description')),
                ('created_when', models.DateTimeField(auto_now_add=True, help_text='When current object was created.', verbose_name='Created When')),
                ('updated_when', models.DateTimeField(auto_now=True, help_text='When current object was updated last time.', verbose_name='Updated When')),
                ('is_actual', models.BooleanField(default=True, help_text='Designates whether this item should be taken into account or not.', verbose_name='Is Actual')),
                ('amount', models.DecimalField(decimal_places=2, help_text='Price to pay fo the order.', verbose_name='Amount', max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'Payments',
                'ordering': ('type',),
                'verbose_name': 'Payment',
            },
        ),
        migrations.CreateModel(
            name='PaymentType',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.TextField(blank=True, help_text='Any information which may be helpful to operate the current object.', verbose_name='Description')),
                ('created_when', models.DateTimeField(auto_now_add=True, help_text='When current object was created.', verbose_name='Created When')),
                ('updated_when', models.DateTimeField(auto_now=True, help_text='When current object was updated last time.', verbose_name='Updated When')),
                ('is_actual', models.BooleanField(default=True, help_text='Designates whether this item should be taken into account or not.', verbose_name='Is Actual')),
                ('name', models.CharField(max_length=300, verbose_name='Payment Type', help_text='Type of payment.')),
            ],
            options={
                'verbose_name_plural': 'Payment Types',
                'verbose_name': 'Payment Type',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.TextField(blank=True, help_text='Any information which may be helpful to operate the current object.', verbose_name='Description')),
                ('created_when', models.DateTimeField(auto_now_add=True, help_text='When current object was created.', verbose_name='Created When')),
                ('updated_when', models.DateTimeField(auto_now=True, help_text='When current object was updated last time.', verbose_name='Updated When')),
                ('is_actual', models.BooleanField(default=True, help_text='Designates whether this item should be taken into account or not.', verbose_name='Is Actual')),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Name', help_text="Shop's owner name.")),
                ('user', models.OneToOneField(verbose_name='User', help_text='Login name.', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'People',
                'ordering': ('name',),
                'verbose_name': 'Person',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.TextField(blank=True, help_text='Any information which may be helpful to operate the current object.', verbose_name='Description')),
                ('created_when', models.DateTimeField(auto_now_add=True, help_text='When current object was created.', verbose_name='Created When')),
                ('updated_when', models.DateTimeField(auto_now=True, help_text='When current object was updated last time.', verbose_name='Updated When')),
                ('is_actual', models.BooleanField(default=True, help_text='Designates whether this item should be taken into account or not.', verbose_name='Is Actual')),
                ('name', models.CharField(max_length=500, verbose_name='Name', help_text="Shop's name.")),
                ('address', models.CharField(blank=True, null=True, max_length=300, verbose_name='Address', help_text='Physical address of the shop.')),
                ('working_days', models.CharField(blank=True, null=True, max_length=100, verbose_name='Working days', help_text='Days when the shop is open.')),
                ('working_hours', models.CharField(blank=True, null=True, max_length=100, verbose_name='Working hours', help_text='Hours when the shop is open.')),
                ('brand', models.ForeignKey(verbose_name='Brand', help_text='Brand this shop belongs to.', blank=True, null=True, to='market.Brand')),
                ('owner', models.ForeignKey(verbose_name='Owner', help_text='Owner of this shop.', to='market.Person')),
            ],
            options={
                'verbose_name_plural': 'Shops',
                'ordering': ('owner__name', 'name', 'address'),
                'verbose_name': 'Shop',
            },
        ),
        migrations.AddField(
            model_name='payment',
            name='type',
            field=models.ForeignKey(verbose_name='Payment Type', help_text='Type of payment.', to='market.PaymentType'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(verbose_name='Customer', help_text='Customer who made this order.', to='market.Person'),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery',
            field=models.ForeignKey(verbose_name='Delivery', help_text='Delivery details (if any).', blank=True, null=True, to='market.Delivery'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(verbose_name='Payment', help_text='Payment details.', to='market.Payment'),
        ),
        migrations.AddField(
            model_name='item',
            name='shop',
            field=models.ForeignKey(verbose_name='Shop', help_text='Shop which is selling this item.', to='market.Shop'),
        ),
        migrations.AddField(
            model_name='item',
            name='type',
            field=models.ForeignKey(verbose_name='Item Type', help_text='Type of the current item.', to='market.ItemType'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='details',
            field=models.ForeignKey(verbose_name='Details', help_text='Current delivery details.', to='market.DeliveryDetails'),
        ),
        migrations.AddField(
            model_name='cvalue',
            name='item',
            field=models.ForeignKey(verbose_name='Item', help_text='Linked item.', to='market.Item'),
        ),
        migrations.AddField(
            model_name='contactdetails',
            name='person',
            field=models.ForeignKey(verbose_name='Person', help_text='Related person.', to='market.Person'),
        ),
        migrations.AddField(
            model_name='characteristic',
            name='item_type',
            field=models.ManyToManyField(help_text='Item type which should have this characteristic available.', verbose_name='Item Type', to='market.ItemType'),
        ),
        migrations.AddField(
            model_name='characteristic',
            name='measurement',
            field=models.ForeignKey(verbose_name='Measurement units', help_text="Units to measure characteristic's values.", to='market.Measurement'),
        ),
        migrations.AddField(
            model_name='brand',
            name='owner',
            field=models.ForeignKey(verbose_name='Owner', help_text='Brand owner.', blank=True, null=True, to='market.Person'),
        ),
        migrations.AlterUniqueTogether(
            name='shop',
            unique_together=set([('name', 'address')]),
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together=set([('type', 'shop')]),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set([('name', 'parent')]),
        ),
        migrations.AlterUniqueTogether(
            name='brand',
            unique_together=set([('name', 'owner')]),
        ),
    ]
