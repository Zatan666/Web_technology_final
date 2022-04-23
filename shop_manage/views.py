from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.db.models import Q 
from shop_manage.models import Pens , Erasers ,Arts, Diys
from django.core.paginator import Paginator, EmptyPage, InvalidPage



# Create your views here.
def home(request):
    cate = 'Stationery'
    quote = ' "Without black, no color has any depth" -Amy Grant" '
    type1 = 'Writing'
    type2 = 'Eraser'
    type3 = 'Art'
    type4 = 'Diy'

    type1_details = 'pen & pencil'
    type2_details = 'eraser & liquid paper'
    type3_details = 'all type color, brush,tool '
    type4_details = 'sticker, tape'

    template = loader.get_template('index.html')

    context  = {
        'category': cate,
        'quote' : quote,
        'type1': type1,
        'type2': type2,
        'type3': type3,
        'type4': type4,
        'type1_details': type1_details,
        'type2_details': type2_details,
        'type3_details': type3_details,
        'type4_details': type4_details,

    }
    return HttpResponse(template.render(context,request))

def project(request):
    cate = 'Project'
    template = loader.get_template('project.html')
    context  = {
        'category': cate,
        }
    return HttpResponse(template.render(context,request))

def product_pen(request):

    cate = 'Writing'

    products_list = Pens.objects.all()

    search_post = request.GET.get('search')
    
    sub = request.GET.get('subcat')

    if search_post :
        products_list = Pens.objects.filter(Q(name__icontains=search_post) | Q(price__icontains=search_post)).order_by('id')
    
    if sub:
        if sub == 'cat1' :
            products_list = products_list.filter(sub='pen').order_by('id')
        elif sub == 'cat2' :
            products_list = products_list.filter(sub='pencil').order_by('id')


    count = products_list

    #per page
    p = Paginator(products_list, 19)
    page = request.GET.get('page', '1')
    
    try:
        products_list = p.page(page)
    except(EmptyPage, InvalidPage):
        products_list = p.page(p.num_pages)


    index = products_list.number -1  
 
    max_index = len(p.page_range)

    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index

    page_range = list(p.page_range)[start_index:end_index]


    template = loader.get_template('product_pen.html')

    context  = {
        'category': cate,
        'products_list': products_list,
        'page_range':page_range,
        'search_post' : search_post,
        'count':count,
        'sub':sub,

    }

    return HttpResponse(template.render(context,request))

def product_eraser(request):

    cate = 'Eraser'

    products_list = Erasers.objects.all()

    search_post = request.GET.get('search')
    
    sub = request.GET.get('subcat')

    if search_post :
        products_list = Erasers.objects.filter(Q(name__icontains=search_post) | Q(price__icontains=search_post)).order_by('id')
    
    if sub:
        if sub == 'cat1' :
            products_list = products_list.filter(sub='eraser').order_by('-id')
        elif sub == 'cat2' :
            products_list = products_list.filter(sub='correction').order_by('id')

    count = products_list

    #per page
    p = Paginator(products_list, 19)
    page = request.GET.get('page', '1')
    
    try:
        products_list = p.page(page)
    except(EmptyPage, InvalidPage):
        products_list = p.page(p.num_pages)


    index = products_list.number -1  
 
    max_index = len(p.page_range)

    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index

    page_range = list(p.page_range)[start_index:end_index]


    template = loader.get_template('product_eraser.html')

    context  = {
        'category': cate,
        'products_list': products_list,
        'page_range':page_range,
        'search_post' : search_post,
        'count':count,
        'sub':sub,

    }

    return HttpResponse(template.render(context,request))

def product_art(request):

    cate = 'Art'

    products_list = Arts.objects.all()

    search_post = request.GET.get('search')
    
    sub = request.GET.get('subcat')

    if search_post :
        products_list = Arts.objects.filter(Q(name__icontains=search_post) | Q(price__icontains=search_post)).order_by('id')
    
    if sub:
        if sub == 'cat1' :
            products_list = products_list.filter(sub='color').order_by('id')
        elif sub == 'cat2' :
            products_list = products_list.filter(sub='brush').order_by('id')
        elif sub == 'cat3' :
            products_list = products_list.filter(sub='paper').order_by('id')        


    count = products_list

    #per page
    p = Paginator(products_list, 19)
    page = request.GET.get('page', '1')
    

    try:
        products_list = p.page(page)
    except(EmptyPage, InvalidPage):
        products_list = p.page(p.num_pages)


    index = products_list.number - 1  
 
    max_index = len(p.page_range)

    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index

    page_range = list(p.page_range)[start_index:end_index]


    template = loader.get_template('product_art.html')

    context  = {
        'category': cate,
        'products_list': products_list,
        'page_range':page_range,
        'search_post' : search_post,
        'count':count,
        'sub':sub,

    }

    return HttpResponse(template.render(context,request))

def product_diy(request):

    cate = 'DIY'

    products_list = Diys.objects.all()

    search_post = request.GET.get('search')
    
    sub = request.GET.get('subcat')

    if search_post :
        products_list = Diys.objects.filter(Q(name__icontains=search_post) | Q(price__icontains=search_post)).order_by('id')
    
    if sub:
        if sub == 'cat1' :
            products_list = products_list.filter(sub='sticker').order_by('id')
        elif sub == 'cat2' :
            products_list = products_list.filter(sub='tape').order_by('id')

    count = products_list

    #per page
    p = Paginator(products_list, 19)
    page = request.GET.get('page', '1')
    

    try:
        products_list = p.page(page)
    except(EmptyPage, InvalidPage):
        products_list = p.page(p.num_pages)


    index = products_list.number - 1  
 
    max_index = len(p.page_range)

    start_index = index - 3 if index >= 3 else 0
    end_index = index + 3 if index <= max_index - 3 else max_index

    page_range = list(p.page_range)[start_index:end_index]


    template = loader.get_template('product_diy.html')

    context  = {
        'category': cate,
        'products_list': products_list,
        'page_range':page_range,
        'search_post' : search_post,
        'count':count,
        'sub':sub,

    }

    return HttpResponse(template.render(context,request))

def about(request):

    return render(request, "about.html")
