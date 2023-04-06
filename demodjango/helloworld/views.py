from django.shortcuts import render, redirect
from .models import product,bill
from django.views import generic
from .forms import billform


# Create your views here
def home(request):
    return render(request,'home.html')

class product_lists(generic.ListView):
    model=product

class product_detail(generic.DetailView):
    model = product

class product_add(generic.CreateView):
    model = product
    fields = '__all__'

def billgeneration(request):
    bill_obj = billform(request.POST)
    if bill_obj.is_valid():
        bills = bill_obj.save()
        return redirect('calc-sum',pk=bills.bill_num)
    return render(request, 'helloworld/billadd_form.html', {'form':billform})


def calsum(request,pk):
    bill_obj = bill.objects.get(bill_num=pk)
    products_set=bill_obj.products.all()
    total=bill_obj.total_sum
    for product in products_set:
        total = total+product.product_price
    bill_obj.total_sum= total
    bill_obj.save()
    return redirect('bill-detail',pk=bill_obj.bill_num)


class bill_detail(generic.DetailView):
    model = bill