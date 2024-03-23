from rest_framework import serializers
from .models import Parent, Child, Daycare, Club, Voucher, ChildEnrollment

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'

class DaycareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Daycare
        fields = '__all__'

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'

class VoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voucher
        fields = '__all__'

class ChildEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChildEnrollment
        fields = '__all__'
