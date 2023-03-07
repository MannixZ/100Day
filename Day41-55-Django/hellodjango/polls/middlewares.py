'''自定义中间件'''

from django.http import JsonResponse, HttpRequest
from django.shortcuts import redirect

# 需要登录才能访问的资源路径
LOGIN_REQUIRED_URLS = {'/praise/', '/criticize/', '/excel/', '/teachers_data/'}


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def check_login_middleware(get_resp):
    def wrapper(request: HttpRequest, *args, **kwargs):
        if request.path in LOGIN_REQUIRED_URLS:
            if 'userid' not in request.session:
                if is_ajax(request):
                    return JsonResponse({'code': 10003, 'hint': '请先登录'})
                else:
                    backurl = request.get_full_path()
                    return redirect(f'/login/?backurl={backurl}')
        return get_resp(request, *args, **kwargs)

    return wrapper
