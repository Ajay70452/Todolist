from django.shortcuts import render, redirect
from .models import Mad

def todo(request):
    mad = Mad.objects.all()
    if request.method == 'POST':
        new_mad = Mad(
            text=request.POST['text']
        )
        new_mad.save()
        return redirect('/')


    return render(request,'list/index.html',{'jake':mad})

def delete(request,pk):
    mad = Mad.objects.get(id=pk)
    mad.delete()
    return redirect('/')


