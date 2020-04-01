from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from .models import Vacancy, Company
from django.http.request import HttpRequest

def get_vacancies(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    print(vacancies_json)
    return JsonResponse(vacancies_json, safe=False)

def get_vacancy(request, id):
    vacancies = Vacancy.objects.all()
    for i in vacancies:
        if i.id == id:
            return JsonResponse(i.to_json())
    return HttpResponse("<h1>No such file .(</h1>")

def get_companies(request):
    companies = Company.objects.all()
    companies_json = [com.to_json() for com in companies]
    return JsonResponse(companies_json, safe=False)

def get_company(request, id):
    companies = Company.objects.all()
    for i in companies:
        if i.id == id:
            return JsonResponse(i.to_json())
    return HttpResponse("<h1>No such file .(</h1>")

def get_company_vacancies(request, id):
    vacancies = Vacancy.objects.all()
    out = []
    for i in vacancies:
        if i.company_id.id == id:
            out.append(i.to_json())
    return JsonResponse(out, safe=False)

def get_top_ten(request):
    vacancies = Vacancy.objects.all().order_by('-salary')
    vacancies_json = [vac.to_json() for vac in vacancies[:10]]
    return JsonResponse(vacancies_json, safe=False)

def get_top_ten_by_company(request, id):
    vacancies = Vacancy.objects.filter(company_id=id).order_by('-salary')
    vacancies_json = [vac.to_json() for vac in vacancies[:10]]
    return JsonResponse(vacancies_json, safe=False)
