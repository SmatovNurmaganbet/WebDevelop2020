from django.urls import path
from . import views as v
urlpatterns = [
    path("api/vacancies/", v.get_vacancies),
    path('api/vacancies/<int:id>', v.get_vacancy),
    path("api/companies/", v.get_companies),
    path("api/companies/<int:id>/", v.get_company),
    path("api/companies/<int:id>/vacancies/", v.get_company_vacancies),
    path("api/vacancies/top_ten", v.get_top_ten),
    path("api/<int:id>/vacancies/", v.get_top_ten_by_company)
]