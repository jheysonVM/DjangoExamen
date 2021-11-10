from django.shortcuts import render

from examen.forms import NoticiaForm

# Create your views here.
# def noticia_add(request):
#     context={}
#     form=NoticiaForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#     context['form']=form
#     return render(request,'noticia_add.html')