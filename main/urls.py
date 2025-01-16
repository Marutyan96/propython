# main/urls.py
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.books, name='books'),
    path('tests/', views.tests, name='tests'),
    path('accounts/', include('allauth.urls')),  # URL для all
    path('search/', views.search, name='search'),
    path('installation/', views.installation_info, name='installation_info'),
    path('basic/', views.basic_info, name='basic_info'),
    path('variables/', views.variables_info, name='variables_info'),
    path('input-output/', views.input_output_info, name='input_output_info'),
    path('arithmetic/', views.arithmetic_info, name='arithmetic_info'),
    path('conditional/', views.conditional_info, name='conditional_info'),
    path('loops/', views.loops_info, name='loops_info'),
    path('functions/', views.functions_info, name='functions_info'),
    path('lists/', views.list_info, name='list_info'),
    path('tuples/', views.tuple_info, name='tuple_info'),
    path('ranges/', views.range_info, name='range_info'),
    path('dictionaries/', views.dictionary_info, name='dictionary_info'),
    path('sets/', views.set_info, name='set_info'),
    path('strings/', views.string_info, name='string_info'),
    path('oop/', views.oop_info, name='oop_info'),
    path('inheritance/', views.inheritance_info, name='inheritance_info'),
    path('modules/', views.modules_info, name='modules_info'),
    path('file-handling/', views.file_handling_info, name='file_handling_info'),
    path('exceptions/', views.exceptions_info, name='exceptions_info'),
    path('search/', views.search, name='search'),
    path('async_programming',views.async_programming_info, name='async_programming_info'),
    path('flask/', views.flask_info, name='flask_info'),
    path('django/', views.django_info, name='django_info'),
    path('fastAPI/', views.fastAPI_info, name='fastAPI_info'),
    path('ml-intro/', views.ml_intro_info, name='ml_intro_info'),
    path('testing/', views.testing_info, name='testing_info'),
    path('decorators_info/', views.decorators_info, name='decorators_info'),
    path('lambda/', views.lambda_info, name='lambda_info'),
    path('vscode/', views.vscode_info, name='vscode_info'),
    path('async-programming/intro/', views.async_programming_intro, name='async_programming_intro'),
    path('async-programming/working-with-asyncio/', views.working_with_asyncio, name='working_with_asyncio'),
    path('async-programming/exception-handling/', views.exception_handling_async, name='exception_handling_async'),
    path('async-programming/http-requests/', views.async_http_requests, name='async_http_requests'),
    path('solid/', views.solid_info, name='solid_info'),
    path('type_conversion/', views.type_conversion_info, name='type_conversion_info'),
    path('variable_scape/', views.variable_scope_info, name='variable_scope_info'),
    path('closures/', views.closures_info, name='closures_info'),
    path('args_kwargs_info/', views.args_kwargs_info, name='args_kwargs_info'),
    path('interview_info/', views.interview_info, name='interview_info'),
    path('editor', views.editor, name='editor'),
    path('run/', views.run_code, name='run_code'),
    path('account_signup/', views.account_signup, name='account_signup'), # Ваш маршрут для регистрации
    path('account_login/', views.account_login, name='account_login'),  # Определите маршрут для входа
    path('profile/', views.profile_view, name='profile'),  # Ваш маршрут для профиля
    path('login_view/', views.login_view, name='login_view'),
    path('add/', views.add_article, name='add_article'),
    path('articles/', views.article_list, name='article_list'),
    path('articles/<int:article_id>/',  views.article_detail, name='article_detail'),  # URL для деталей статьи
    path('article/<int:article_id>/delete/', views.delete_article, name='delete_article'),
    path('article/<int:pk>/', views.article_detail, name='article_detail'),

]
