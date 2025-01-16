from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io
import contextlib
from django.shortcuts import render,redirect


def editor(request):
    return render(request, 'editor/editor.html')

@csrf_exempt  
def run_code(request):
    if request.method == 'POST':
        code = request.POST.get('code', '')
        output = ''
        try:
            # Создаем поток для захвата вывода
            output_stream = io.StringIO()
            with contextlib.redirect_stdout(output_stream):
                local_vars = {}
                exec(code, {}, local_vars)
                
            # Получаем вывод из потока
            output = output_stream.getvalue()
        except Exception as e:
            output = f'Error: {str(e)}'
        
        return JsonResponse({'output': output})



