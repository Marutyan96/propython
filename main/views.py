from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm
from .models import Article
from difflib import SequenceMatcher
from .views_helpers import * 
from .views_code_editor import * 
from .views_profile import * 
from django.conf import settings  # Импортируем настройки, чтобы получить информацию о суперпользователе
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        image = request.FILES['upload']
        article = Article.objects.create(image=image)  # Сохраните изображение
        url = article.image.url  # Получите URL изображения
        return JsonResponse({'url': url})
    return JsonResponse({'error': 'Ошибка загрузки изображения'}, status=400)


@login_required
def delete_article(request, article_id):
    # Получаем статью или возвращаем 404, если не найдена
    article = get_object_or_404(Article, id=article_id)

    # Проверяем, является ли текущий пользователь создателем сайта
    if request.user.username != settings.SITE_ADMIN_USERNAME:  # Замените SITE_ADMIN_USERNAME на имя вашего пользователя
        return render(request, 'error.html', {'message': 'У вас нет прав на удаление этой статьи.'})

    if request.method == 'POST':
        article.delete()  # Удаляем статью
        return redirect('article_list')  # Перенаправляем на список статей после удаления

    return render(request, 'confirm_delete.html', {'article': article})




def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'main/article_detail.html', {'article': article})

def article_list(request):
    articles = Article.objects.all().order_by('-created_at')  # Получаем все статьи, отсортированные по дате
    return render(request, 'main/articles.html', {'articles': articles})




@login_required
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)  # Передаем request.FILES в форму
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()

            # Проверяем, есть ли загруженное изображение
            if 'image' in request.FILES:
                article.image = request.FILES['image']  # Сохраняем изображение в модели
                article.save()  # Сохраняем изменения

                # Генерируем HTML-код для вставки изображения
                img_tag = f'<img src="{article.image.url}" alt="Uploaded Image" style="max-width: 100%; height: auto;">'
                article.content += img_tag  # Добавляем тег изображения в контент
                article.save()  # Сохраняем изменения в модели

            return redirect('article_list')  # Перенаправляем на список статей
    else:
        form = ArticleForm()
    
    return render(request, 'main/add_article.html', {'form': form})


class SearchHandler:
    def __init__(self):
        self.search_map = {
            'установка': 'installation_info',
            'введение': 'basic_info',
            'переменные': 'variables_info',
            'ввод': 'input_output_info',
            'арифметика': 'arithmetic_info',
            'условия': 'conditional_info',
            'циклы': 'loops_info',
            'функции': 'functions_info',
            'списки': 'list_info',
            'кортежи': 'tuple_info',
            'диапазоны': 'range_info',
            'словарь': 'dictionary_info',
            'множества': 'set_info',
            'строки': 'string_info',
            'декораторы': 'decorators_info',
            'классы': 'oop_info',
            'наследование': 'inheritance_info',
            'модули': 'modules_info',
            'файлы': 'file_handling_info',
            'исключения': 'exceptions_info',
            'асинхронное': 'async_programming_info',
            'тестирование': 'testing_info',
            'flask': 'flask_info',
            'django': 'django_info',
            'fastapi': 'fastapi_info',
            'машинное обучение': 'ml_intro_info',
            'vscode': 'vscode_info',
            'lambda': 'lambda_info',
            'solid': 'solid_info',
            'async_http_requests': 'async_http_requests',
            'exception_handling_async': 'exception_handling_async',
            'working_with_asyncio': 'working_with_asyncio',
            'async_programming_intro': 'async_programming_intro',
        }


    def fuzzy_search(self, query):
        if not query:
            return None

        best_match = None
        best_ratio = 0

        for key in self.search_map.keys():
            ratio = SequenceMatcher(None, query.casefold(), key.casefold()).ratio()
            if ratio > best_ratio:
                best_match = key
                best_ratio = ratio

        if best_ratio > 0.6:
            return self.search_map[best_match]
        else:
            return None


def search(request):
    query = request.GET.get('q')
    if query:
        handler = SearchHandler()
        redirect_url = handler.fuzzy_search(query)  # Пытаемся выполнить нечеткий поиск
        if redirect_url:
            return redirect(redirect_url)
    return render(request, 'main/search_results.html', {'query': query})  # Если ничего не найдено, показываем форму



from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Comment
from .forms import CommentForm

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.all()
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = CommentForm()

    return render(request, 'main/article_detail.html', {'article': article, 'comments': comments, 'form': form})