from django.shortcuts import render

# Create your views here.
def landing_page(request):
    return render(request, 'index.html')

def auth_page(request):
    return render(request, 'auth.html')

def dashboard_page(request):
    return render(request, 'dashboard.html')

def farming_guide(request):
    return render(request, 'farming_guide.html')

def market_intelligence(request):
    return render(request, 'market_intelligence.html')