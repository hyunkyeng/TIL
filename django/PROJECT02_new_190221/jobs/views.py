import os
from django.shortcuts import render
from faker import Faker
import requests
from .models import Job



# Create your views here.
def index(request):
    return render(request, 'jobs/index.html')
    
def pastlife(request):
    name = request.GET.get('name')
    #db에 있는지 확인
    person = Job.objects.filter(name=name).first()
    #person = Job.objexts.get(name=name) #없으면 에러가 뜸
    
    #있으면, 원래 직업을 가져오고
    if person:
        pastjob = person.pastjob
    #없으면 faker로 새로운 직업을 넣어서 모델에 저잘하고 가져옵니다.
    else:
        faker = Faker('ko_kr')
        pastjob = faker.job()
        person = Job(name=name, pastjob=pastjob)
        person.save()
        
        
    # giphy
    GIPHY_API = os.getenv('GIPHY_API')
    url = f'http://api.giphy.com/v1/gifs/search?api_key={GIPHY_API}&q={pastjob}$limit=1&lang=ko'
    data = requests.get(url).json()
    image = data.get('data')[0].get('images').get('original').get('url')
    
    
        
    return render(request, 'jobs/pastlife.html', {'person': person, 'image': image})