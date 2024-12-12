from django.shortcuts import render, redirect, get_object_or_404
from .models import PriceProd, Product
from django.http import JsonResponse
from .forms import PriceProdForm


def saveprod(request):
    if request.method == "POST":
        nameprod_ = request.POST.get("nameprod")
        categoryprod_ = request.POST.get("categoryprod")
        descprod_ = request.POST.get("descprod")
        brandprod_ = request.POST.get("brandprod")
        manudateprod_ = request.POST.get("manudateprod")
        weightprod_ = float(request.POST.get("weightprod"))

        Product.objects.create(
            nameprod=nameprod_,
            categoryprod=categoryprod_,
            descprod=descprod_,
            brandprod=brandprod_,
            manudateprod=manudateprod_,
            weightprod=weightprod_,
        )

        return render(request, "cadprod.html")
    return render(request, "cadprod.html")


def saveprice(request):
    if request.method == "POST":
        priceprod_ = float(request.POST.get("priceprod"))
        dateverify_ = request.POST.get("dateverify")
        codprod_ = Product(request.POST.get("product"))

        PriceProd.objects.create(
            priceprod=priceprod_, dateverify=dateverify_, codprod=codprod_
        )

        return redirect("saveprice")

    products = Product.objects.all()
    return render(request, "cadprice.html", {"products": products})


def historyprice(request, product_id):
    product = get_object_or_404(Product, codprod=product_id)
    price_history = PriceProd.objects.filter(codprod=product).order_by("-dateverify")
    return render(request, 'pricehistory.html', {
        'product': product,
        'price_history': price_history
    })
    
def productlist(request):
    
    products = Product.objects.all()
        
    return render(request, 'productlist.html', {'products': products})

def pricechart(request, codprod):
    product_ = get_object_or_404(Product, pk=codprod)
    price_history_ = PriceProd.objects.filter(codprod=product_).order_by("dateverify")

    # Preparando os dados
    dates_ = [entry.dateverify.strftime('%d-%m-%Y') for entry in price_history_]
    prices_ = [float(entry.priceprod) for entry in price_history_]

    # Passando o contexto corretamente
    return render(request, 'pricechart.html', {
        'product': product_,
        'chartdata': JsonResponse({'dates': dates_, 'prices': prices_}).content.decode('utf-8'),
    })

def editproduct(request, codprod):
    product = get_object_or_404(Product, pk=codprod)
    
    if request.method == "POST":
        product.nameprod = request.POST.get("nameprod")
        product.categoryprod = request.POST.get("categoryprod")
        product.descprod = request.POST.get("descprod")
        product.brandprod = request.POST.get("brandprod")
        product.manudateprod = request.POST.get("manudateprod")
        product.weightprod = float(request.POST.get("weightprod"))
        product.save()
        return redirect("productlist")
    
    return render(request, "editproduct.html", {"product": product})

def deleteproduct(request, codprod):
    product = get_object_or_404(Product, pk=codprod)
    product.delete()
    return redirect("productlist")

def alterar(request, codprice):
    # Recupera a instância de PriceProd pelo ID
    price_instance = get_object_or_404(PriceProd, codprice=codprice)
 
    if request.method == 'POST':
        # Cria uma instância do formulário com os dados do POST e a instância de preço
        form = PriceProdForm(request.POST, instance=price_instance)
        if form.is_valid():
            # Salva as alterações no banco de dados
            form.save()
            # Redireciona para o histórico de preços do produto relacionado
            return redirect('historyprice', codprod=price_instance.codprod.codprod)
    else:
        # Se o método for GET, exibe o formulário com os dados atuais do preço
        form = PriceProdForm(instance=price_instance)
 
    # Renderiza o template com o formulário
    return render(request, 'alterar.html', {'form': form})
 
 
def deleteprice(request, codprice):
 
    history_ = get_object_or_404(PriceProd, codprice=codprice)
    prod_ = history_.codprod
    history_.delete()
 
    return redirect('historyprice', prod_.codprod)