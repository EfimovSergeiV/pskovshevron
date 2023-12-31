from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor.widgets import CKEditorWidget

from shop.models import (
    CategoryModel,
    ProductModel, 
    ImageProductModel, 
    ProductPropertyModel, 
    OrderModel,
    OrderProductModel,
)



class ProductAdminForm(forms.ModelForm):
    """ Добавляем полю описания, виджет CKEditor """

    description = forms.CharField(widget=CKEditorWidget(), label="Описание")
    
    class Meta:
        model = ProductModel
        fields = '__all__'


class ProductImageInline(admin.TabularInline):
    """ Вложенные изображения товара """

    model = ImageProductModel
    readonly_fields = ('preview', )

    def preview(self, obj):
        return mark_safe('<img style="margin-right: -20vh" src="/files/%s" alt="Нет изображения" width="auto" height="80" />' % (obj.image))

    preview.short_description = 'Изображение'
    fieldsets = (
        (None, {'fields': ('preview', 'image')}),
        )
    extra = 0


class ProductPropertyInline(admin.TabularInline):
    """ Вложенные свойства товара """

    model = ProductPropertyModel
    extra = 0


class CategoryAdmin(admin.ModelAdmin):

    list_display = ( 'id', 'title', 'ordering', )
    list_display_links = ( 'id', 'title', )
    list_editable = ('ordering', )


class ProductAdmin(admin.ModelAdmin):
    """ Страница редактирования товара """

    form = ProductAdminForm
    list_display = ('id', 'title', 'price', 'activated', 'last_update',)
    list_display_links = ('id', 'title',)
    list_editable = ('activated', 'price',)
    search_fields = ('id', 'name',)
    readonly_fields = ('last_update',)
    inlines = (ProductImageInline, ProductPropertyInline)
    fieldsets = (
        (None, {'fields': (('title','activated'),('wildberries', 'price',), ('category',),('description', ),('last_update', ),)}),
    )




class OrderProductInline(admin.TabularInline):
    """ Вложенные свойства товара """

    model = OrderProductModel
    def preview(self, obj):
        return mark_safe('<img style="" src="%s" alt="Нет изображения" width="auto" height="80" />' % (obj.image))


    fields =  ('prod_id', 'preview', 'title', 'price','quantity')
    readonly_fields = ('prod_id', 'preview', 'title', 'price','quantity')
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    """ Отображение заказов в админке """
    def preview(self, obj):
        if obj.image_for_custom:
            return mark_safe('<img style="" src="/files/%s" alt="Нет изображения" width="auto" height="120" />' % (obj.image_for_custom))
        else:
            return mark_safe('<p>-</p>')
    preview.short_description = 'Изображение'

    readonly_fields = ('client_name','contact_data', 'preview', 'image_for_custom')
    list_display = ('id', 'client_name', 'contact_data', 'created_data')
    list_display_links = ('id', 'client_name',)
    inlines = ( OrderProductInline, )
    fieldsets = (
        ('Данные клиента', {'fields': (('client_name','contact_data'),)}),
        ('Дизайн клиента', {'fields': (('preview', 'image_for_custom',),)})
    )


# Регистрация моделей в админке
admin.site.register(CategoryModel, CategoryAdmin)
admin.site.register(ProductModel, ProductAdmin)
admin.site.register(OrderModel, OrderAdmin)