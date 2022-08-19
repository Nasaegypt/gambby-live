from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Service, SubCategory
from django.core.paginator import Paginator
from .forms import ServiceForm
from .filters import ServiceFilter
from cities_light.models import City, Country, Region


# Create your views here.

def service_list(request):
    # service_list = Service.objects.all()
    # filters
    myfilter = ServiceFilter(request.GET, queryset=Service.objects.all())
    service_list = myfilter.qs
    service_count = service_list.count()
    elements = 6  # services per page
    paginator = Paginator(service_list.order_by('-id'), elements)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    elements = str(":-" + str(elements))
    context = {'services': page_obj, 'service_count': service_count, 'myfilter': myfilter,
               'elements': elements}  # template name
    return render(request, 'service/service_list.html', context)


def service_detail(request, slug):
    service_detail = Service.objects.get(slug=slug)
    context = {'service': service_detail}
    return render(request, 'service/service_detail.html', context)


# AJAX
def load_cities(request):
    region_id = request.GET.get('region_id')
    cities = City.objects.filter(region_id=region_id).all()
    return render(request, 'service/city_dropdown_list_options.html', {'cities': cities})


def load_sub_category(request):
    main_category_id = request.GET.get('main_category_id')
    sub_categories = SubCategory.objects.filter(main_category_id=main_category_id).all()
    #print(sub_categories)
    return render(request, 'service/sub_category_list_options.html', {'sub_categories': sub_categories})



@login_required
def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            form = ServiceForm()
            return redirect('services:service_list')

        else:
            pass

    else:
        form = ServiceForm()

    return render(request, 'service/add_service.html', {'form': form})
