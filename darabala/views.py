from django.shortcuts import render

def index(request):
    context: dict[str,str]={
        'title':'Dara Bala',
        'content':'Платформа размещения государственного заказа на дополнительное образование детей'
    }
    return render(request,'darabala/index.html', context )
