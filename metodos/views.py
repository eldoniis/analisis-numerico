from django.shortcuts import render
from metodos.backend.biseccion import doBisection
# Create your views here.
def index(request):
    ans = doBisection(0,1,'log(sin(x)**2+1)-1/2',100,0.0000001)
    print(ans)
    return render(request, 'index.html', {"ans": ans})
