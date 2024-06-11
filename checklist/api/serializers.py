from rest_framework import serializers
from checklist.models import CheckList

class CheckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckList
        fields = '__all__'


# With Reference Count
class CheckListSerializer_ReferenceCount(serializers.ModelSerializer):
    
    references_count = serializers.SerializerMethodField()

    def get_references_count(self, instance):
        lookup_model_count = instance.checkListId.count()
        return lookup_model_count

    class Meta:
        model = CheckList
        # fields = '__all__'
        fields = ['id', 'amName', 'enName', 'references_count']



# from rest_framework import serializers
# from myapp.models import MyModel  # import your model

# class MyModelSerializer(serializers.ModelSerializer):
#     references_count = serializers.SerializerMethodField()

#     def get_references_count(self, instance):
#         # Assuming lookup_model is the related model you want to count references for
#         lookup_model_count = instance.lookup_model_set.count()
#         return lookup_model_count

#     class Meta:
#         model = MyModel
#         fields = ['id', 'other_fields', 'references_count']  # Add 'references_count' to fields
