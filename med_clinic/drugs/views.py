from django.shortcuts import render,redirect
from .models import drug
from .forms import add_drug_form
from django.contrib.auth.decorators import login_required
from accounts.decorators import unauthenticated_user, allowed_users
from django.template.loader import render_to_string
from django.http import JsonResponse
# Create your views here.

@login_required(login_url="accounts:login")
#@allowed_users(allowed_roles=['admin','secretary','doctor'])
def index(request):
    context = {}
    url_parameter = request.GET.get("q")
    
    if url_parameter:
        drugs_list = drug.objects.filter(brand__icontains=url_parameter).order_by('name')
    else:
        drugs_list = drug.objects.all()


    if request.is_ajax():
        html = render_to_string(
            template_name="partials/drugs_search.html", 
            context={"drugs_list": drugs_list}
        )

        data_dict = {"html_from_view": html}

        return JsonResponse(data=data_dict, safe=False)
    user = request.user.groups.get()
    drug_form = add_drug_form()
    context = {
        'drug_form':drug_form,
        'drugs_list':drugs_list,
        'user':user
        }
    return render(request, "drugs/index.html", context)


@login_required(login_url="accounts:login")
@allowed_users(allowed_roles=['admin','secretary','doctor'])
def add_drug(request):
    drug_form = add_drug_form()
    if request.method=='POST':
        drug_form = add_drug_form(request.POST)
        if drug_form.is_valid():
            drug_form.save()
            return redirect('drugs:drugs')  
    return render(request, 'drugs:add_drug')

@login_required(login_url="accounts:login")
@allowed_users(allowed_roles=['admin','secretary','doctor'])
def edit_drug(request, id):

    _drug = drug.objects.get(id = id)

    drug_form = add_drug_form(instance=_drug)

    if request.method=='POST':
        drug_form = add_drug_form(request.POST,instance=_drug)
        if drug_form.is_valid():
            drug_form.save()
            return redirect('drugs:drugs')
            
    context = {"drug_form":drug_form}          
    return render(request, 'drugs/edit_drug.html', context)

@login_required(login_url="accounts:login")
@allowed_users(allowed_roles=['admin','secretary','doctor'])
def delete_drug(request, id):
    drug.objects.get(id=id).delete()
    return redirect('drugs:drugs')