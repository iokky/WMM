from django.contrib import messages
from django.core.files.uploadhandler import FileUploadHandler
from django.db.models.aggregates import Count, Sum, Max
from django.db.models.functions import TruncMonth, TruncDate

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from django.views.generic import CreateView, DetailView, ListView, View, UpdateView

from django.utils.decorators import method_decorator


from .models import Category, Order, Product
from .forms import DateFilterForm, CategoryForm, OrderForm, ProductForm


# CATEGORY

class CategoryView(ListView):
    queryset = Category.objects.all()
    template_name = 'order/category.html'

    # def form_valid(self, form, **kwargs):
    #     context = self.get_context_data(**kwargs)
    #     context['form'] = form
    #     print(context)
    #     return super().get_context_data(**kwargs)

    def post(self, request):
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                messages.success(request, 'Продукт успешно добавлен')
            return HttpResponseRedirect('/category')


class CategoryDetailView(DetailView):
    queryset = Category.objects.all()
    slug_field = 'id'


class CategoryFormView(CreateView):
    model = Category
    form_class = CategoryForm

    def post(self, request):
        if request.method == 'POST':
            form = CategoryForm(request.POST, request.FILES)
            if form.is_valid():
                FileUploadHandler(request.FILES['image'])
                form.save()
                return HttpResponseRedirect('category')


class CategoryUpdateView(UpdateView):
    model = Category
    fields = [
        'name',
        'image'
    ]


# PRODUCT
class ProductView(ListView):
    queryset = Product.objects.all()


class ProductFormView(CreateView):
    model = Product
    form_class = ProductForm

    def get_form(self):
        form = super(ProductFormView, self).get_form()
        initial_base = self.get_initial()
        form.initial = initial_base
        if 'category' in self.request.GET:
            form.fields['category'].initial = self.request.GET['category']
        return form

    def post(self, request):
        if request.method == 'POST':
            print(request.GET)
            form = ProductForm(request.POST, request.FILES)

            if form.is_valid():
                FileUploadHandler(request.FILES['image'])
                form.save()
                return HttpResponseRedirect('product')


class ProductUpdateView(UpdateView):
    model = Product
    fields = [
        'category',
        'name',
        'description',
        'image'
    ]


class MainView(ListView):
    queryset = Order.objects.values('product__name', 'category__name', 'date')\
        .filter(date__range=('2021-02-20', '2021-02-28'))\
        .annotate(cost=Sum('price'))\
        .order_by('date')

    template_name = 'order/order.html'


class ReportSerialize(View):

    def get(self, request,  *args, **kwargs):
        if 'start_date' and 'end_date' in request.GET:
            start_date = request.GET['start_date']
            end_date = request.GET['end_date']
        else:
            start_date = '2021-02-01'
            end_date = '2021-02-28'

        orders_list = Order.objects.values('category__name') \
            .filter(date__range=(start_date, end_date)) \
            .annotate(cost=Sum('price')) \
            .annotate(count=Count('category__name')) \
            .order_by('-cost')

        products_list = Order.objects.values('category__name', 'product__name') \
            .filter(date__range=(start_date, end_date)) \
            .annotate(product_cost=Sum('price')) \
            .annotate(product_count=Count('product__name')) \
            .order_by('-product_cost')

        data = {'series': [], 'products': [], 'total_cost': 0}

        for order in orders_list:
            data['total_cost'] += order['cost']
            data['series'].append({
                'name': order['category__name'],
                'y': order['cost'],
                'count': order['count']
            })

        # print(data['series'])

        for order in products_list:
            data['products'].append({
                'category': order['category__name'],
                'name': order['product__name'],
                'y': order['product_cost'],
                'count': order['product_count']
            })
        # print(data['products'])

        return JsonResponse(data, safe=False)

