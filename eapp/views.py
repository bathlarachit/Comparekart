from django.shortcuts import render
from eapp.utils import flipkart,amazon
# Create your views here.
def feature(request):
    return render(request,'eapp/feature.html')
def about(request):
    return render(request,'eapp/about.html')
def home(request):
    return render(request,'eapp/index.html')
def findproduct(request):
    if request.method=="POST":
        k=request.POST.get('search1')
        f=flipkart(k)
        a=amazon(k)
        data={}

        for i in range(0,4):
            x=str(i)
            try:
                data["f"+x+"name"]=f[i][0]
                data["f"+x+"price"]=f[i][1]
                data["f"+x+"link"]=f[i][6]
            except:
                pass

            try:
                data["a"+x+"name"]=a[i][0]
                data["a"+x+"price"]=a[i][1]
                data["a"+x+"link"]=a[i][4]
            except:
                pass
            if not data :
                data['message']='No products'
            data['name']=k


        return render(request,'eapp/result.html',data)

    else:
        return render(request,'eapp/index.html')
