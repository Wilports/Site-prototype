from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView
from .forms import *
from .models import *
from django.core.paginator import Paginator


def index(request):

    return render(request, 'perevozka/index.html')


def orders(request):

    form = OrdersForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(form.cleaned_data)
        form = form.save()
        return redirect("thanks")

    return render(request, 'perevozka/orders.html', {"form": form})


def thanks(request):

    return render(request, "perevozka/thanks.html", {"order": Orders.objects.latest('id')})


def pays(request):

    return render(request, "perevozka/pays.html")


def trucks(request):

    trucks = Trucks.objects.all()
    form = OrdersForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(form.cleaned_data)
        form = form.save()
        return redirect("thanks")

    return render(request, "perevozka/trucks.html",  {"trucks": trucks, "form": form})


def comments(request):

    form = CommentsForm(request.POST or None)
    posts = Comments.objects.all()

    paginator = Paginator(posts, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if request.method == "POST" and form.is_valid():
        print(form.cleaned_data)
        form = form.save()
        return redirect(request.path)

    return render(request, 'perevozka/comments.html', {"form": form,  "page_obj": page_obj})


class NewsHome(ListView):
    paginate_by = 5
    model = News
    template_name = 'perevozka/news.html'
    context_object_name = "news"


class NewsDetailView(DetailView):
    model = News
    template_name = 'perevozka/news-detail.html'
    context_object_name = "article"
