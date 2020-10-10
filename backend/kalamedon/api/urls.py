from django.urls import path

#from kalamedon.api.views import VocabularyAPIView
#from kalamedon.api.views import VocabularyAPIDetail
from kalamedon.api.views import GenericAPIView
from kalamedon.api.views import GenericKDAPIView

app_name = 'kalamedon_api'

urlpatterns = [
    #path('voc/', VocabularyAPIView.as_view()),
    # path('voc/<int:pk>', VocabularyAPIDetail.as_view()),
    #path('voc/<str:object_id>', VocabularyAPIDetail.as_view()),
    path('gen/', GenericAPIView.as_view()),
    path('gen/<str:vocabulary>/', GenericAPIView.as_view()),

    path('kd/', GenericKDAPIView.as_view()),
    path('kd/<str:name>/', GenericKDAPIView.as_view()),
]
