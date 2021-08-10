from django.shortcuts import render

# Create your views here.

def add_numbers(request):
    if request.method=='GET':
        return render(request,'addition.html')
    elif request.method=='POST':
        num1=int(request.POST['num1'])
        num2=int(request.POST['num2'])
        res=num1+num2
        print(res)
        return render(request,'addition.html',{'result':res})

def sub_numbers(request):
    if request.method=='GET':
        return render(request,'subtraction.html')
    elif request.method=='POST':
        num1=int(request.POST['num1'])
        num2=int(request.POST['num2'])
        res=num1-num2
        context={}
        context['result']=res
        context['num1']=num1
        context['num2']=num2
        return render(request,'subtraction.html',context)

def mul_numbers(request):
    if request.method=='GET':
        return render(request,'multiplication.html')
    elif request.method=='POST':
        num1=request.POST['num1']
        num2=request.POST['num2']
        res=int(num1)*int(num2)
        context={}
        context['result']=res
        context['num1']=num1
        context['num2']=num2
        return render(request,'multiplication.html',context)

def div_numbers(request):
    if request.method=='GET':
        return render(request,'division.html')
    elif request.method=='POST':
        num1=request.POST['num1']
        num2=request.POST['num2']
        res=int(num1)/int(num2)
        # print(res)
        context={}
        context['num1']=num1
        context['num2']=num2
        context['result']=res
        return render(request,'division.html',context)

def cube(request):
    if request.method=='GET':
        return render(request,'cube.html')
    elif request.method=='POST':
        num=request.POST['num']
        res=int(num)**3
        context={}
        context['num']=num
        context['result']=res
        return render(request,'cube.html',context)