from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status
from .models import Parent, Child, Daycare, Club, Voucher, ChildEnrollment
from .serializers import ParentSerializer, ChildSerializer, DaycareSerializer, ClubSerializer, VoucherSerializer, ChildEnrollmentSerializer

def index(request):
    context: dict[str,str]={
        'title':'Dara Bala',
        'content':'Платформа размещения государственного заказа на дополнительное образование детей'
    }
    return render(request,'darabala/index.html', context )

def test(request):
    return render(request, "darabala/test.html")

class ParentListCreate(generics.ListCreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class ParentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer

class ChildListCreate(generics.ListCreateAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

class ChildDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

class DaycareListCreate(generics.ListCreateAPIView):
    queryset = Daycare.objects.all()
    serializer_class = DaycareSerializer

class DaycareDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Daycare.objects.all()
    serializer_class = DaycareSerializer

class ClubListCreate(generics.ListCreateAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class ClubDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class VoucherListCreate(generics.ListCreateAPIView):
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer

class VoucherDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Voucher.objects.all()
    serializer_class = VoucherSerializer

class ChildEnrollmentListCreate(generics.ListCreateAPIView):
    queryset = ChildEnrollment.objects.all()
    serializer_class = ChildEnrollmentSerializer

class ChildEnrollmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChildEnrollment.objects.all()
    serializer_class = ChildEnrollmentSerializer
    
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