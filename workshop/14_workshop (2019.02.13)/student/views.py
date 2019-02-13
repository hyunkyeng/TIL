from django.shortcuts import render

# Create your views here.

students = {'박성주': 5, '김예랑': 10, '박경철': 1}

def info(request):
    teacher = '김준호'
    return render(request, 'info.html', {'teacher': teacher, 'students': students})
    
def info_age(request, name):
    # age = students[name]   #이 방식은 에러가 뜬다.
    age = students.get(name, 'unknown')
    return render(request, 'info_age.html', {'age': age, 'name': name})