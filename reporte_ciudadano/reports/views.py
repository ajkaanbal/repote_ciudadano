from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)

from .models import Report
from .serializers import ReportSerializer


# Create your views here.
class ReportList(ListCreateAPIView):
    serializer_class = ReportSerializer
    queryset = Report.objects.all()


class Report(RetrieveUpdateDestroyAPIView):
    serializer_class = ReportSerializer
    queryset = Report.objects.all()

