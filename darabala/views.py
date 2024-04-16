from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly
from .models import Parent, Child, Daycare, Club, Voucher, ChildEnrollment
from .serializers import ParentSerializer, ChildSerializer, DaycareSerializer, ClubSerializer, VoucherSerializer, ChildEnrollmentSerializer
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm

def index(request):
    context: dict[str,str]={
        'title':'Dara Bala',
        'content':'Платформа размещения государственного заказа на дополнительное образование детей'
    }
    return render(request,'darabala/index.html', context )

def test(request):
    return render(request, "darabala/test.html")

generics
class ParentListCreate(generics.ListCreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    permission_classes = [IsAuthenticated]

class ParentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = ["gender"]
    search_fields = ["first_name","last_name"]
    ordering_fields = ['iin']

class ChildListCreate(generics.ListCreateAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    permission_classes = [IsAuthenticated]

class ChildDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    permission_classes = [IsAuthenticated]

class DaycareListCreate(generics.ListCreateAPIView):
    queryset = Daycare.objects.all()
    serializer_class = DaycareSerializer
    permission_classes = [IsAuthenticated]

class DaycareDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Daycare.objects.all()
    serializer_class = DaycareSerializer
    permission_classes = [IsAuthenticated]

class ClubListCreate(generics.ListCreateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    permission_classes = [IsAuthenticated]

class ClubDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    permission_classes = [IsAuthenticated]

class VoucherListCreate(generics.ListCreateAPIView):
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer
    permission_classes = [IsAuthorOrReadOnly]

class VoucherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer
    permission_classes = [IsAuthorOrReadOnly]

class ChildEnrollmentListCreate(generics.ListCreateAPIView):
    queryset = ChildEnrollment.objects.all()
    serializer_class = ChildEnrollmentSerializer
    permission_classes = [IsAuthorOrReadOnly]

class ChildEnrollmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChildEnrollment.objects.all()
    serializer_class = ChildEnrollmentSerializer
    permission_classes = [IsAuthorOrReadOnly]
    
    def delete(self, request):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

# # filter
# class CustomPagination(PageNumberPagination):
#     page_size = 5
#     page_size_query_param = 'page_size'
#     max_page_size = 10
    
# class ParentViewSet(viewsets.ModelViewSet):
#     queryset = Parent.objects.all()
#     serializer_class = ParentSerializer
#     pagination_class = CustomPagination
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['gender', 'phone']

# class ChildViewSet(viewsets.ModelViewSet):
#     queryset = Child.objects.all()
#     serializer_class = ChildSerializer
#     pagination_class = CustomPagination
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['gender', 'date_of_birth']  

# class DaycareViewSet(viewsets.ModelViewSet):
#     queryset = Daycare.objects.all()
#     serializer_class = DaycareSerializer
#     pagination_class = CustomPagination
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['name', 'address']  

# class ClubViewSet(viewsets.ModelViewSet):
#     queryset = Club.objects.all()
#     serializer_class = ClubSerializer
#     pagination_class = CustomPagination
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['age_group', 'cost']  

# class VoucherViewSet(viewsets.ModelViewSet):
#     queryset = Voucher.objects.all()
#     serializer_class = VoucherSerializer
#     pagination_class = CustomPagination
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['status', 'amount']  

# class ChildEnrollmentViewSet(viewsets.ModelViewSet):
#     queryset = ChildEnrollment.objects.all()
#     serializer_class = ChildEnrollmentSerializer
#     pagination_class = CustomPagination
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['enrollment_date']  

# # viewsets 
# class ParentViewSet(viewsets.ModelViewSet):
#     queryset = Parent.objects.all()
#     serializer_class = ParentSerializer

# class ChildViewSet(viewsets.ModelViewSet):
#     queryset = Child.objects.all()
#     serializer_class = ChildSerializer

# class DaycareViewSet(viewsets.ModelViewSet):
#     queryset = Daycare.objects.all()
#     serializer_class = DaycareSerializer

# class ClubViewSet(viewsets.ModelViewSet):
#     queryset = Club.objects.all()
#     serializer_class = ClubSerializer

# class VoucherViewSet(viewsets.ModelViewSet):
#     queryset = Voucher.objects.all()
#     serializer_class = VoucherSerializer

# class ChildEnrollmentViewSet(viewsets.ModelViewSet):
#     queryset = ChildEnrollment.objects.all()
#     serializer_class = ChildEnrollmentSerializer

def child_list(request):
    # Загрузить детей и их родителей за один запрос - select_related
    children = Child.objects.select_related('parent').all()
    return render(request, 'child_list.html', {'children': children})

def club_list(request):
    # Загрузить клубы и их ваучеры за два запроса - prefetch_related
    clubs = Club.objects.prefetch_related('vouchers').all()
    return render(request, 'club_list.html', {'clubs': clubs})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            iin = form.cleaned_data['iin']
            password = form.cleaned_data['password']
            user = authenticate(username=iin, password=password)
            if user is not None:
                login(request, user)
                return redirect('darabala/parent_detail')
    else:
        form = LoginForm(request)
    return render(request, 'darabala/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('darabala/parent_detail')
    else:
        form = RegistrationForm()
    return render(request, 'darabala/register.html', {'form': form})