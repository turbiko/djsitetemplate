from .models import Product


def shop(request):
    products = Product.objects.live()
    p = Paginator(products, 10)
    #shows number of items in page
    totalProducts = (p.count)
    pageNum = request.GET.get('page', 1)
    page1 = p.page(pageNum)

    return TemplateResponse(request, 'home/shop.html', {
        'products': products,
        'dataSaved':page1
    })

def about(request):
    return TemplateResponse(request, 'home/about.html', {
    })

def contact(request):
    return TemplateResponse(request, 'home/contact.html', {
    })