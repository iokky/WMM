from django import forms

from .models import Category, Order, Product


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            'name',
            'image'
        )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'category',
            'name',
            'description',
            'image'
        )


class OrderForm(forms.ModelForm):
    # def __init__(self, product_pk, *args, **kwargs):
    #     super(OrderForm, self).__init__(*args, **kwargs)
    #     self.fields['product'].initial = Product.objects.get(pk=product_pk)
    #     print(args, kwargs)

    # def __init__(self, *args, **kwargs):
        # super(OrderForm, self).__init__(*args, **kwargs)
        # self.fields['product'].initial = Product.objects.get(pk=1)
        # for fields in self:
        #     fields.label = ''

    class Meta:
        model = Order
        fields = (
            'category',
            'product',
            'price',
        )


class DateFilterForm(forms.ModelForm):
    start_date = forms.DateField()
    end_date = forms.DateField()
