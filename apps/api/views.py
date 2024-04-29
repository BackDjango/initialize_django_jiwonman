from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import LimitOffsetPagination

from .models import Board
from .serializers import BoardSerializer

class BoardViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    pagination_class = LimitOffsetPagination