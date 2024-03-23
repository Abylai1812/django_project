from django.contrib import admin
from django.urls import path
from darabala import views

urlpatterns = [     
    path('parents/', views.ParentListCreate.as_view(), name='parent-list-create'),
    path('parents/<int:pk>/', views.ParentDetail.as_view(), name='parent-detail'),
    path('children/', views.ChildListCreate.as_view(), name='child-list-create'),
    path('children/<int:pk>/', views.ChildDetail.as_view(), name='child-detail'),
    path('daycares/', views.DaycareListCreate.as_view(), name='daycare-list-create'),
    path('daycares/<int:pk>/', views.DaycareDetail.as_view(), name='daycare-detail'),
    path('clubs/', views.ClubListCreate.as_view(), name='club-list-create'),
    path('clubs/<int:pk>/', views.ClubDetail.as_view(), name='club-detail'),
    path('vouchers/', views.VoucherListCreate.as_view(), name='voucher-list-create'),
    path('vouchers/<int:pk>/', views.VoucherDetail.as_view(), name='voucher-detail'),
    path('child-enrollments/', views.ChildEnrollmentListCreate.as_view(), name='child-enrollment-list-create'),
    path('child-enrollments/<int:pk>/', views.ChildEnrollmentDetail.as_view(), name='child-enrollment-detail'),
]