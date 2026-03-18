from django.http import HttpResponse

# Спільний стиль для обох сторінок
COMMON_STYLE = """
<style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #f4f7f6;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
    }
    .card {
        background: white;
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        width: 100%;
        max-width: 500px;
        text-align: center;
    }
    h1 { color: #2c3e50; margin-bottom: 20px; }
    p, li { color: #546e7a; font-size: 1.1em; line-height: 1.6; }
    ul { list-style: none; padding: 0; text-align: left; }
    li { margin-bottom: 10px; border-bottom: 1px solid #eee; padding-bottom: 5px; }
    hr { border: 0; border-top: 1px solid #eee; margin: 20px 0; }
    .btn {
        display: inline-block;
        background-color: #3498db;
        color: white;
        padding: 12px 25px;
        text-decoration: none;
        border-radius: 25px;
        transition: background 0.3s ease;
    }
    .btn:hover { background-color: #2980b9; }
    b { color: #2c3e50; }
</style>
"""

def project_info(request):
    content = f"""
    {COMMON_STYLE}
    <div class="card">
        <h1>Проєкт: Навчальна ІС</h1>
        <p><b>Дата створення:</b> 18 березня 2026 року</p>
        <p><b>Версія:</b> 1.0.0 Alpha</p>
        <p><b>Статус:</b> В розробці</p>
        <hr>
        <a href="/about-me/" class="btn">Резюме автора →</a>
    </div>
    """
    return HttpResponse(content)

def about_me(request):
    content = f"""
    {COMMON_STYLE}
    <div class="card">
        <h1> Резюме автора</h1>
        <ul>
            <li><b>ПІБ:</b> Пряников Родіон</li>
            <li><b>Рік народження:</b> 2005</li>
            <li><b>Освіта:</b> Студент 3 курсу</li>
            <li><b>Університет:</b> ХНЕУ ім. С. Кузнеця</li>
            <li><b>Спеціальність:</b> Кібербезпека</li>
        </ul>
        <hr>
        <a href="/" class="btn">← На головну</a>
    </div>
    """
    return HttpResponse(content)