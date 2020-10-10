from rest_framework import serializers
from kalamedon.models import Vocabulary
from kalamedon.models import KalameDon


class KalameDonSerializer(serializers.ModelSerializer):
    class Meta:
        model = KalameDon
        fields = ["user", "name"]


class VocabularySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vocabulary
        fields = ["user", "kalamedon", "vocabulary", "i_know",
                  "definition", "level", "examples"]
