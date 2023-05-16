from django.shortcuts import  render
import requests

def test(request):
    url ='http://127.0.0.1:8000/api/add?a=1&b=2'
    response = requests.get(url)
    data = response.json()
    print(data)
    context = {
        'data': data
    }
    return render(request, 'test.html', context=context)
