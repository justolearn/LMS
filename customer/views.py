from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from django.contrib.auth.models import User as user_model
from rest_framework import permissions
from .serializers import UserSerializer, CustomerSerializer
from .models import Customer
# from rest_framework.renderers import TemplateHTMLRenderer
# from rest_framework.decorators import action
# from django.template import loader, RequestContext
# from rest_framework.response import Response
# from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = user_model.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.AllowAny]




# class UserTemplateViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     # queryset = Books.objects.all().order_by('-date_joined')
#     renderer_classes = [TemplateHTMLRenderer]
#     # template_name = 'user/user_list.html'
#     queryset = user_model.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.AllowAny]
#
#     @action(detail=False, methods=['GET'])
#     def user_list(self, request):
#         try:
#             queryset = user_model.objects.all()
#
#             serializer = UserSerializer(queryset, many=True)
#             # return Response({'user_list': serializer.data}, template_name='user/user_list.html')
#             return render(request, 'user/user_list.html', {'user_list': serializer.data})
#         except Exception as e:
#             print('Excepion ', e)
#
#     @action(detail=True, methods=['GET'])
#     def user_detail(self, request, pk):
#         try:
#             queryset = user_model.objects.get(id=pk)
#             queryset = get_object_or_404(user_model, id=pk)
#
#             # serializer = UserSerializer(queryset)
#             # return HttpResponseRedirect({'user': serializer.data}, template_name='user/user_detail.html')
#             # return render(request, 'user/user_detail.html', {'user':  serializer.data})
#             template = loader.get_template("user/user_detail.html")
#             return HttpResponse(template.render({'user': queryset},
#                                                 request=request))
#         except Exception as e:
#             print('Excepion ', e)
