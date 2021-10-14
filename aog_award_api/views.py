from awards.models import Awardee, AwardTitle
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework import permissions
from .serializers import AwardSerializer, AwardTitleSerializer

# Create your views here.


class AwardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Awardee.objects.all().order_by('-created')
    serializer_class = AwardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return Awardee.objects.filter(user=self.request.user)


class AwardTitleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = AwardTitle.objects.all()
    serializer_class = AwardTitleSerializer
    permission_classes = [permissions.IsAuthenticated]
