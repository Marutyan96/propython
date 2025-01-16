from django.shortcuts import render
from .models import Course


def home(request):
    courses = Course.objects.all()
    return render(request, 'main/index.html', {'courses': courses})  

def books(request):
    return render(request, 'main/books.html')

def tests(request):
    return render(request, 'main/tests.html')

def login_view(request):
    return render(request, 'main/login.html')

def installation_info(request):
    return render(request, 'main/basics/installation_info.html')

def basic_info(request):
    return render(request, 'main/basics/basic_info.html')

def variables_info(request):
    return render(request, 'main/basics/variables_info.html')

def input_output_info(request):
    return render(request, 'main/basics/input_output_info.html')

def arithmetic_info(request):
    return render(request, 'main/basics/arithmetic_info.html')

def conditional_info(request):
    return render(request, 'main/basics/conditional_info.html')

def loops_info(request):
    return render(request, 'main/basics/loops_info.html')

def functions_info(request):
    return render(request, 'main/basics/functions_info.html')

def list_info(request):
    return render(request, 'main/basics/list_info.html')

def tuple_info(request):
    return render(request, 'main/basics/tuple_info.html')

def range_info(request):
    return render(request, 'main/basics/range_info.html')

def dictionary_info(request):
    return render(request, 'main/basics/dictionary_info.html')

def set_info(request):
    return render(request, 'main/basics/set_info.html')

def string_info(request):
    return render(request, 'main/basics/string_info.html')

def oop_info(request):
    return render(request, 'main/oop_info.html')

def inheritance_info(request):
    return render(request, 'main/inheritance_info.html')

def modules_info(request):
    return render(request, 'main/basics/modules_info.html')

def file_handling_info(request):
    return render(request, 'main/basics/file_handling_info.html')

def exceptions_info(request):
    return render(request, 'main/basics/exceptions_info.html')

def async_programming_info(request):
    return render(request, 'main/async/async_programming_info.html')

def testing_info(request):
    return render(request, 'main/testing_info.html')

def flask_info(request):
    return render(request, 'main/framework/flask_info.html')

def django_info(request):
    return render(request, 'main/framework/django_info.html')

def fastAPI_info(request):
    return render(request, 'main/framework/fastAPI_info.html')

def ml_intro_info(request):
    return render(request, 'main/ml_intro_info.html')

def decorators_info(request):
    return render(request, 'main/basics/decorators_info.html')

def lambda_info(request):
    return render(request, 'main/basics/lambda_info.html')

def vscode_info(request):
    return render(request, 'main/basics/vscode_info.html')


def async_programming_intro(request):
    return render(request, 'main/async/lesson_1_introduction_to_async_programming.html')

def working_with_asyncio(request):
    return render(request, 'main/async/lesson_2_working_with_asyncio.html')

def exception_handling_async(request):
    return render(request, 'main/async/lesson_3_exception_handling_in_async_functions.html')

def async_http_requests(request):
    return render(request, 'main/async/lesson_4_async_http_requests_with_aiohttp.html')


def solid_info(request):
    return render(request, 'main/basics/solid_info.html')

def variable_scope_info(request):
    return render(request, 'main/basics/variable_scope_info.html')

def type_conversion_info(request):
    return render(request, 'main/basics/type_conversion_info.html')

def closures_info(request):
    return render(request, 'main/basics/closures_info.html')

def args_kwargs_info(request):
    return render(request, 'main/basics/args_kwargs_info.html')



def interview_info(request):
    return render(request, 'main/interview_info.html')