from rest_framework import serializers
from .models import Parent, Child, Daycare, Club, Voucher, ChildEnrollment

class VoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voucher
        fields = '__all__'

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = '__all__'

class DaycareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Daycare
        fields = '__all__'

class ChildSerializer(serializers.ModelSerializer):
    vouchers = VoucherSerializer(many=True, read_only=True)
    
    class Meta:
        model = Child
        fields = '__all__'

class ParentSerializer(serializers.ModelSerializer):
    children = ChildSerializer(many=True, read_only=True)

    class Meta:
        model = Parent
        fields = '__all__'


class ChildEnrollmentSerializer(serializers.ModelSerializer):
    child = ChildSerializer()
    voucher = VoucherSerializer()
    daycare = DaycareSerializer()
    club = ClubSerializer()
    
    class Meta:
        model = ChildEnrollment
        fields = '__all__'