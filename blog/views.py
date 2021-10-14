from django.shortcuts import render
from blog.models import info, data
from blog import forms

# Create your views here.


def index(request):
    info_list = info.objects.order_by('first_name')
    diction = {'info_list':info_list}
    return render(request, 'index.html', context=diction)

def info_list(request, info_id):
    all_info = info.objects.get(pk=info_id)
    all_data = data.objects.filter(full_name=info_id)
    
    diction = {'all_info':all_info, 'all_data': all_data}
    return render(request, 'info_list.html', context=diction)

def edit_data(request, data_id):
    update_data = data.objects.get(pk=data_id)
    data_edit = forms.data_form(instance=update_data)
    diction ={}
    if request.method == 'POST':
        data_edit = forms.data_form(request.POST, instance=update_data)
        
        if data_edit.is_valid():
            data_edit.save(commit=True)
            
            diction.update({'text': 'Successfully Update'})
        
    diction.update({'data_edit':data_edit})
    diction.update({'data_id': data_id})
    return render(request, 'edit_data.html', context=diction)

def info_form(request):
    new_form = forms.info_form()
    if request.method == 'POST':
        new_form = forms.info_form(request.POST)
        
        if new_form.is_valid():
            new_form.save(commit=True)
            return index(request)
    
    diction = {'new_form':new_form}
    return render(request, 'info_form.html', context=diction)


def data_form(request):
    new_form = forms.data_form
    if request.method == 'POST':
        new_form = forms.data_form(request.POST)
        
        if new_form.is_valid():
            new_form.save(commit=True)
            return index(request)
        
    diction = {'new_form': new_form}
    return render(request, 'data_form.html', context=diction)

def edit_info(request, info_id, ):
    
    update_info = info.objects.get(pk=info_id)
    edit_info = forms.info_form(instance=update_info)
    
    if request.method == 'POST':
        edit_info = forms.info_form(request.POST, instance=update_info)
        
        if edit_info.is_valid():
            edit_info.save(commit=True)
            
            return info_list(request, info_id)
            
        
    diction = {'edit_info':edit_info}
    return render(request, 'edit_info.html', context=diction)

def delete(request, data_id):
    datad = data.objects.get(pk=data_id).delete()
    diction ={'delete': 'Delete this data'}
    return render(request,'delete.html', context=diction)

def delete_info(request, info_id):
    info_delete = info.objects.get(pk=info_id).delete()
    diction ={'delete': 'Delete this Info'}
    return render(request,'delete.html', context=diction)