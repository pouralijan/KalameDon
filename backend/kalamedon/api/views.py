from kalamedon.models import Vocabulary
from kalamedon.models import KalameDon

from .serializers import VocabularySerializer
from .serializers import KalameDonSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class GenericKDAPIView(generics.GenericAPIView, mixins.ListModelMixin,
                       mixins.CreateModelMixin, mixins.UpdateModelMixin,
                       mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    serializer_class = KalameDonSerializer
    lookup_field = 'name'

    authentication_classes = [SessionAuthentication,
                              BasicAuthentication, TokenAuthentication]
    #authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return KalameDon.objects.filter(user=user)

    def get(self, request, name=None):
        if name:
            return self.retrieve(request)
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, name=None):
        print(name)
        return self.update(request, name)

    def delete(self, request, name=None):
        return self.destroy(request, name)


class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin,
                     mixins.CreateModelMixin, mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin, mixins.DestroyModelMixin):

    serializer_class = VocabularySerializer
    #queryset = Vocabulary.objects.all()
    lookup_field = 'vocabulary'

    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [SessionAuthentication,
                              BasicAuthentication, TokenAuthentication]
    #authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # return Vocabulary.objects.all()
        return Vocabulary.objects.filter(user=user)

    def get(self, request, vocabulary=None):
        if vocabulary:
            return self.retrieve(request)
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, vocabulary=None):
        print(vocabulary)
        return self.update(request, vocabulary)

    def delete(self, request, vocabulary=None):
        return self.destroy(request, vocabulary)

# class GenericAPIDetail(generics.GenericAPIView, mixins.ListModelMixin):
#    serializer_class = VocabularySerializer
#    queryset_class = Vocabulary.objects.all()


# class VocabularyAPIView(APIView):
#    def get(self, request):
#        vocalularys = Vocabulary.objects.all()
#        serialize = VocabularySerializer(vocalularys, many=True)
#        return Response(serialize.data)
#
#    def post(self, request):
#        serialize = VocabularySerializer(data=request.data)
#        if serialize.is_valid():
#            serialize.save()
#            return Response(serialize.data, status=status.HTTP_201_CREATED)
#        return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class VocabularyAPIDetail(APIView):
#    def get_object(self, object_id):
#        try:
#            return Vocabulary.objects.get(vocabulary=object_id)
#        except Vocabulary.DoesNotExist:
#            raise Http404
#
#    def get(self, request, object_id, format=None):
#        snippet = self.get_object(object_id)
#        serializer = VocabularySerializer(snippet)
#        return Response(serializer.data)
#
#    def put(self, request, object_id, format=None):
#        vocabulary = self.get_object(object_id)
#        serializer = VocabularySerializer(vocabulary, data=request.data)
#        if serializer.is_valobject_id():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#    def delete(self, request, object_id, format=None):
#        vocabulary = self.get_object(object_id)
#        vocabulary.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)
