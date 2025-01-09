from rest_framework import viewsets
from . import models
from . import Serializers


class guideTypesOfMaintenanceViewset(viewsets.ModelViewSet):
    queryset = models.guide_types_of_maintenance.objects.all()
    serializer_class = Serializers.gtomSerializer

class guideRecoveryMethodViewset(viewsets.ModelViewSet):
    queryset = models.guide_recovery_method.objects.all()
    serializer_class = Serializers.grmSerializer

class guideFailureNodeViewset(viewsets.ModelViewSet):
    queryset = models.guide_failure_node.objects.all()
    serializer_class = Serializers.gfnSerializer

class guideTechniqueModelViewset(viewsets.ModelViewSet):
    queryset = models.guide_technique_model.objects.all()
    serializer_class = Serializers.gtmSerializer

class guideEngineModelViewset(viewsets.ModelViewSet):
    queryset = models.guide_engine_model.objects.all()
    serializer_class = Serializers.gemSerializer

class guideTRansmissionModelViewset(viewsets.ModelViewSet):
    queryset = models.guide_transmission_model.objects.all()
    serializer_class = Serializers.gtrmSerializer

class guideModelDriveBridgeViewset(viewsets.ModelViewSet):
    queryset = models.guide_model_drive_bridge.objects.all()
    serializer_class = Serializers.gmdbSerializer

class guideModelControlledBridgeViewset(viewsets.ModelViewSet):
    queryset = models.guide_model_controlled_bridge.objects.all()
    serializer_class = Serializers.gmcbSerializer

# class machineViewset(viewsets.ModelViewSet):
#     queryset = models.machine.objects.all()
#     serializer_class = Serializers.machineSerializer

class allMachineViewset(viewsets.ModelViewSet):
    queryset = models.machine.objects.all()
    serializer_class = Serializers.machineGetSerializer

class maintenanceViewset(viewsets.ModelViewSet):
    queryset = models.maintenance.objects.all()
    serializer_class = Serializers.maintenanceSerializer

class reclamationViewset(viewsets.ModelViewSet):
    queryset = models.reclamation.objects.all()
    serializer_class = Serializers.reclamationSerializer
