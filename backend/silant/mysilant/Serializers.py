from rest_framework import serializers
from . import models


class gtomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.guide_types_of_maintenance
        fields = '__all__'

class grmSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.guide_recovery_method
        fields = '__all__'

class gfnSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.guide_failure_node
        fields = '__all__'

class gtmSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.guide_technique_model
        fields = '__all__'

class gemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.guide_engine_model
        fields = '__all__'

class gtrmSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.guide_transmission_model
        fields = '__all__'


class gmdbSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.guide_model_drive_bridge
        fields = '__all__'

class gmcbSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.guide_model_controlled_bridge
        fields = '__all__'

# class machineSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.machine
#         fields = '__all__'

class machineGetSerializer(serializers.Serializer):
    id = serializers.CharField()
    factory_number = serializers.CharField()
    technique_model_id = serializers.CharField(source='technique_model.id', max_length=200)
    technique_model = serializers.CharField(source='technique_model.name', max_length=200)
    engine_model_id = serializers.CharField(source='engine_model.id', max_length=200)
    engine_model = serializers.CharField(source='engine_model.name', max_length=200)
    engine_number = serializers.CharField()
    transmission_model_id = serializers.CharField(source='transmission_model.id', max_length=200)
    transmission_model = serializers.CharField(source='transmission_model.name', max_length=200)
    transmission_number = serializers.CharField()
    model_drive_bridge_id = serializers.CharField(source='model_drive_bridge.id', max_length=200)
    model_drive_bridge = serializers.CharField(source='model_drive_bridge.name', max_length=200)
    number_drive_bridge = serializers.CharField()
    model_controlled_bridge_id = serializers.CharField(source='model_controlled_bridge.id', max_length=200)
    model_controlled_bridge = serializers.CharField(source='model_controlled_bridge.name', max_length=200)
    number_controlled_bridge = serializers.CharField()
    delivery_date_number = serializers.CharField()
    date_shipment_factory = serializers.DateField()
    endpoint_client = serializers.CharField()
    delivery_address = serializers.CharField()
    Equipment = serializers.CharField()
    client = serializers.CharField(source='client.name', max_length=200)
    service_company = serializers.CharField(source='service_company.name', max_length=200)

class maintenanceSerializer(serializers.Serializer):
    id = serializers.CharField()
    date_of_maintenance = serializers.CharField()
    Operating_time = serializers.CharField()
    Order_number = serializers.CharField()
    Order_date = serializers.DateField()
    maintenance_company = serializers.CharField()
    types_of_maintenance = serializers.CharField(source='types_of_maintenance.name', max_length=200)
    types_of_maintenance_id = serializers.CharField(source='types_of_maintenance.id', max_length=200)
    machine_id = serializers.CharField(source='machine.id', max_length=200)
    machine = serializers.CharField(source='machine.factory_number', max_length=200)
    service_company = serializers.CharField()

class reclamationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.reclamation
        fields = '__all__'