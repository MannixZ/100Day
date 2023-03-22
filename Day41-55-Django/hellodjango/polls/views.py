import io
import json
import uuid
from urllib.parse import quote

import requests
import xlwt
from bpmappers import RawField
from django.http import JsonResponse, HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect
from reportlab.pdfgen import canvas
from bpmappers.djangomodel import ModelMapper

from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Subject, Teacher, User
from .utils import *
from .yzm import *



# 自定义实现的分页器，和 settings 中的 DEFAULT_PAGINATION_CLASS 设置区分
from rest_framework.pagination import PageNumberPagination

class CustomizedPagination(PageNumberPagination):
    # 默认页面大小
    page_size = 5
    # 页面大小对应的查询参数
    page_size_query_param = 'size'
    # 页面大小的最大值
    max_page_size = 50

# Create your views here.

def show_all_subjects(request):
    subjects = Subject.objects.all().order_by('no')
    return render(request, 'subjects.html', {'subjects': subjects})


def show_all_teachers(request):
    try:
        sno = int(request.GET.get('sno'))
        teachers = []
        if sno:
            subject = Subject.objects.only('name').get(no=sno)
            teachers = Teacher.objects.filter(subject=subject).order_by('no')
        return render(request, 'teachers.html', {
            'subject': subject,
            'teachers': teachers
        })
    except (ValueError, Subject.DoesNotExist):
        return redirect('/')


def praise_or_criticize(request: HttpRequest):
    '''好评'''
    if request.session.get("userid"):
        try:
            tno = int(request.GET.get('tno'))
            teacher = Teacher.objects.get(no=tno)
            if request.path.startswith('/praise'):
                teacher.good_count += 1
                count = teacher.good_count
            else:
                teacher.bad_count += 1
                count = teacher.bad_count
            teacher.save()
            data = {'code': 20000, 'mesg': '投票成功', 'count': count}
        except (ValueError, Teacher.DoesNotExist):
            data = {'code': 20001, 'mesg': '投票失败'}
    else:
        data = {"code": 20002, 'mesg': "请先登录"}
    return JsonResponse(data)


def login(request: HttpRequest):
    hint = ''
    if request.method == 'POST':
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            username = request.POST.get('username')
            password = request.POST.get('password')
            if username and password:
                password = gen_md5_digest(password)
                user = User.objects.filter(username=username, password=password).first()
                if user:
                    request.session['userid'] = user.no
                    request.session['username'] = user.username
                    return redirect('/')
                else:
                    hint = '用户名或密码错误'
            else:
                hint = '请输入有效的用户名和密码'
        else:
            return HttpResponse("Please enable cookies and try again.")
    request.session.set_test_cookie()
    return render(request, 'login.html', {'hint': hint})


def logout(request: HttpRequest):
    '''注销'''
    request.session.flush()
    return redirect('/')


def get_captcha(request: HttpRequest) -> HttpResponse:
    '''验证码'''
    captcha_text = gen_random_code()
    request.session['captcha'] = captcha_text
    image_data = Captcha.instance().generate(captcha_text)
    return HttpResponse(image_data, content_type='image/png')


def export_teachers_excel(request: HttpResponse):
    # 创建工作簿
    wb = xlwt.Workbook()
    # 添加工作表
    sheet = wb.add_sheet('老师信息表')
    # 查询所有老师的信息
    queryset = Teacher.objects.all().select_related('subject')
    # 向 excel 表单中写入表头
    colnames = ('姓名', '介绍', '好评数', '差评数', '学科')
    for index, name in enumerate(colnames):
        sheet.write(0, index, name)
    # 向单元格中写入老师的数据
    props = ('name', 'intro', 'good_count', 'bad_count', 'subject')
    for row, teacher in enumerate(queryset):
        for col, prop in enumerate(props):
            # getattr(对象, 对象属性, '') 获取对象属性值
            value = getattr(teacher, prop, '')
            if isinstance(value, Subject):
                value = value.name
            sheet.write(row + 1, col, value)
    # 保存Excel
    buffer = BytesIO()
    wb.save(buffer)
    # 将二进制数据写入响应的消息体中并设置MIME类型
    resp = HttpResponse(buffer.getvalue(), content_type='application/vnd.ms-excel')
    # 中文文件名需要处理成百分号编码
    filename = quote('老师.xls')
    # 通过响应头告知浏览器下载该文件以及对应的文件名
    resp['content-disposition'] = f'attachment; filename*=utf-8\'\'{filename}'
    return resp


def export_pdf(request: HttpResponse):
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.setFont("Helvetica", 80)
    pdf.setFillColorRGB(0.2, 0.5, 0.3)
    pdf.drawString(100, 550, 'hello, world')
    pdf.showPage()
    pdf.save()
    resp = HttpResponse(buffer.getvalue(), content_type='application/pdf')
    resp['content-disposition'] = 'inline; filename="demo.pdf'
    return resp


def get_teachers_data(request: HttpResponse):
    # 创建工作簿
    queryset = Teacher.objects.all().only('name', 'good_count', 'bad_count')
    names = [teacher.name for teacher in queryset]
    good_counts = [teacher.good_count for teacher in queryset]
    bad_counts = [teacher.bad_count for teacher in queryset]
    # return JsonResponse({'names': names, 'good_counts': good_counts, 'bad_counts': bad_counts})
    return render(request, 'teachers_count.html',
                  {'names': names, 'good_counts': good_counts, 'bad_counts': bad_counts})


class SubjectMapper(ModelMapper):
    isHot = RawField('is_hot')

    class Meta:
        model = Subject
        exclude = ('is_hot',)


def api_show_subjects(request: HttpResponse):
    queryset = Subject.objects.all()
    subjects = []
    for subject in queryset:
        subjects.append(SubjectMapper(subject).as_dict())
    return JsonResponse(subjects, safe=False)


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('no', 'name')

from django.views.decorators.cache import cache_page
# cache_page 和 method_decorator 属于声明式编程缓存
# RESTful FBV 实现方法，基于 函数实现
# @api_view(('GET',))
# # 缓存装饰器
# @cache_page(timeout=86400, cache='default')
# def show_subjects(request: HttpRequest) -> HttpResponse:
#     subjects = Subject.objects.all().order_by('no')
#     # 创建序列化器对象并指定要序列化的模型
#     serializer = SubjectSerializer(subjects, many=True)
#     # 通过序列化器的data属性获得模型对应的字典并通过创建Response对象返回JSON格式的数据
#     return Response(serializer.data)


# get_redis_connection 属于编程式缓存
from django_redis import get_redis_connection

@api_view(('GET',))
# 缓存装饰器
def show_subjects(request: HttpRequest) -> HttpResponse:
    """获取学科数据"""
    redis_cli = get_redis_connection()
    # 先尝试从缓存中获取学科数据
    data = redis_cli.get('vote:polls:subjects')
    if data:
        # 如果获取到学科数据就进行反序列化操作
        data = json.loads((data))
    else:
        # 如果缓存中没有获取到学科数据就查询数据库
        queryset = Subject.objects.all()
        data = SubjectSerializer(queryset, many=True).data
        # 将查到的学科数据序列化后放到缓存中
        redis_cli.set('vote:polls:subjects', json.dumps(data), ex=86400)
    return Response({"code": 20000, 'subjects': data})


# RESTful CBV 实现方法，基于 类实现
from rest_framework.generics import ListAPIView  # ListAPIView 自带实现 GET 方法
from rest_framework.viewsets import ModelViewSet  # ModelViewSet 自带实现 GET、POST、PUT、PATCH、DELETE 方法， urls 中需要注册路由才可使用对应继承的类
from django.utils.decorators import method_decorator


@method_decorator(decorator=cache_page(timeout=86400, cache='default'), name='get')
class SubjectView(ModelViewSet):
    # 通过queryset指定如何获取学科数据
    queryset = Subject.objects.all()
    # 通过serializer_class指定如何序列化学科数据
    serializer_class = SubjectSerializer
    # 使用自定义的分页器, 如果不希望数据分页，可以将pagination_class属性设置为None来取消默认的分页器。
    pagination_class = CustomizedPagination

class TeacherSerialize(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('__all__')


# FBV 实现通过学科找到对应的老师
@api_view(('GET',))
def show_teachers(request: HttpRequest) -> HttpResponse:
    try:
        sno = int(request.GET.get('no'))
        subject = Subject.objects.only('name').get(no=sno)
        teachers = Teacher.objects.filter(subject=subject).defer('subject').order_by('no')
        subject_seri = SubjectSerializer(subject)
        teacher_seri = TeacherSerialize(teachers, many=True)
        return Response({'subject': subject_seri.data, 'teacher': teacher_seri.data})
    except (TypeError, ValueError, Subject.DoesNotExist):
        return Response(status=404)

# 同上，改为 CBV 实现
class TeacherView(ListAPIView):
    serializer_class = TeacherSerialize

    def get_queryset(self):
        queryset = Teacher.objects.defer('subject')
        try:
            sno = self.request.GET.get('sno', '')
            queryset = queryset.filter(subject__no=sno)
            return queryset
        except ValueError:
            raise Http404('No teachers found.')


# 第三方api 发送短信验证码
def send_mobile_code(tel, code):
    '''发送短信验证码'''
    resp = requests.post(
        url='http://sms-api.luosimao.com/v1/send.json',
        auth=('api', 'key-自己的APIKey'),
        data={
            'mobile': tel,
            'message': f'您的短信验证码是{code}，打死也不能告诉别人哟。【Python小课】'
        },
        verify=False
    )
    return resp.json()

import random
import re
TEL_PATTERN  = re.compile(r'1[3-9]\d{9}]')

def check_tel(tel):
    '''检查手机号'''
    return TEL_PATTERN.fullmatch(tel) is not None


def random_code(length=6):
    '''生成随机短信验证码'''
    return ''.join(random.choice('1234567890', k=length))


# 发送短信验证码 FBV
@api_view(('GET', ))
def get_mobilecode(request, tel):
    '''获取短信验证码'''
    if check_tel(tel):
        redis_cli = get_redis_connection()
        if redis_cli.exists(f'vote:block-mobile:{tel}'):
            data = {'code': 30001, 'message': '请不要再60秒内重复发送短信验证码'}
        else:
            code = random_code()
            send_mobile_code(tel, code)
            # 通过Redis阻止60秒内容重复发送短信验证码
            redis_cli.set(f'vote:block-mobile:{tel}', 'x', ex=60)
            # 将验证码在Redis中保留10分钟（有效期10分钟）
            redis_cli.set(f'vote2:valid-mobile:{tel}', code, ex=600)
            data = {'code': 30000, 'message': '短信验证码已发送，请注意查收'}
    else:
        data = {'code': 30002, 'message': '请输入有效的手机号'}
    return Response(data)


# 文件数据上传到云储存服务
import qiniu
AUTH = qiniu.Auth('密钥管理中的AccessKey', '密钥管理中的SecretKey')
BUCKET_NAME = 'myvote'

def upload_file_to_qiniu(key, file_path):
    '''上传指定路径的文件到七牛云'''
    token = AUTH.upload_token(BUCKET_NAME, key)
    return qiniu.put_file(token, key, file_path)

def upload_stream_to_qiniu(key, stream, size):
    '''上传二进制数据到七牛云'''
    token = AUTH.upload_token(BUCKET_NAME, key)
    return qiniu.put_stream(token, key, stream, None, size)

# 上传数据函数
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload(request: HttpResponse):
    # 如果上传的文件小于2.5M，则photo对象的类型为InMemoryUploadedFile，文件在内存中
    # 如果上传的文件超过2.5M，则photo对象的类型为TemporaryUploadedFile，文件在临时路径下
    photo = request.FILES.get('photo')
    _, ext = os.path.splitext(photo.name)
    # 通过UUID和原来文件的扩展名生成独一无二的新的文件名
    filename = f'{uuid.uuid1().hex}{ext}'
    # 对于内存中的文件，可以使用上面封装好的函数upload_stream_to_qiniu上传文件到七牛云
    # 如果文件保存在临时路径下，可以使用upload_file_to_qiniu实现文件上传
    upload_stream_to_qiniu(filename, photo.file, photo.size)
    return redirect('/static/html/upload.html')