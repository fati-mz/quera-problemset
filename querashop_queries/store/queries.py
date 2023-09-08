from datetime import timezone
from django.db.models import Avg, Sum, Count
from .models import Employee, Product, Company, Order, Customer

def young_employees(job: str):
    return Employee.objects.filter(age<=30).exclude(job=None)

def cheap_products():
    return Product.objects.filter(price__lt=Avg('price')).order_by('price').values_list('name', flat=True)

def products_sold_by_companies():
    return Company.objects.annotate(sold=Sum('product__sold')).values_list('name', 'sold')

def sum_of_income(start_date: str, end_date: str):
    return Order.objects.filter(time__range=[start_date, end_date]).aggregate(total_revenue=Sum('price'))

def good_customers():
    one_month_ago = timezone.now() - timezone.timedelta(days=30)
    return Customer.objects.filter(level='G', order__time__gte=one_month_ago).annotate(num_orders=Count('order')).filter(num_orders__gt=10).values_list('name', 'phone')

def nonprofitable_companies():
    return Company.objects.annotate(num_products=Count('product')).filter(product__sold__lt=100).filter(num_products__gte=4).values_list('name', flat=True)
