from django.shortcuts import render
from django.http import HttpResponse

# Перша сторінка: Інформація про проєкт
def project_info(request):
    content = """
    <h1>Про проєкт: Навчальна ІС</h1>
    <p><b>Дата створення:</b> 18 березня 2026 року</p>
    <p><b>Версія:</b> 1.0.0 Alpha</p>
    <p><b>Статус:</b> в розробці </p>
    <hr>
    <a href="/about-me/">Перейти до резюме автора</a>
    """
    return HttpResponse(content)

# Друга сторінка: Інформація про тебе
def about_me(request):
    content = """
    <h1>Резюме автора</h1>
    <ul>
        <li><b>ПІБ:</b> Пряников Родіон</li>
        <li><b>Рік народження:</b> 2005</li>
        <li><b>Освіта:</b> Студент 3 курсу</li>
        <li><b>Університет:</b> ХНЕУ імені Семена Кузнеця</li>
        <li><b>Спеціальність:</b> Кібербезпека</li>
    </ul>
    <hr>
    <a href="/">Назад на головну</a>
    """
    return HttpResponse(content)
