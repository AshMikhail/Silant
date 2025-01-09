from rest_framework import routers
from . import views
from accounts.views import clientViewset, service_companyViewset, baseCompanyViewset

router = routers.DefaultRouter()
router.register('basecompany', baseCompanyViewset, basename='basecompany')
router.register('client', clientViewset, basename='Client')
router.register('service', service_companyViewset, basename='service')
# router.register('machine', views.machineViewset, basename='Машины')
router.register('machine', views.allMachineViewset, basename='All Машины')
router.register('maintenance', views.maintenanceViewset, basename='ТО')
router.register('reclamation', views.reclamationViewset, basename='Рекламации')
router.register('guide/tom', views.guideTypesOfMaintenanceViewset, basename='Виды ТО')
router.register('guide/rm', views.guideRecoveryMethodViewset, basename='Способ восстановления')
router.register('guide/fnv', views.guideFailureNodeViewset, basename='Узел отказа')
router.register('guide/tm', views.guideTechniqueModelViewset, basename='Модель техники')
router.register('guide/em', views.guideEngineModelViewset, basename='Модель двигателя')
router.register('guide/trm', views.guideTRansmissionModelViewset, basename='Модель трансмиссии')
router.register('guide/mdb', views.guideModelDriveBridgeViewset, basename='Модель ведущего моста')
router.register('guide/mcb', views.guideModelControlledBridgeViewset, basename='Модель управляемого моста')






urlpatterns = [
]

urlpatterns += router.urls