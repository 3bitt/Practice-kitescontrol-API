from rest_framework import viewsets, request, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models.vw_instructorHours import InstructorHours
from api.serializers.statistics.InstructorHoursSerializer import InstructorHoursSerializer


# class InstructorHoursView(viewsets.ReadOnlyModelViewSet):
#     # queryset = InstructorHours.objects.all()
#     serializer_class = InstructorHoursSerializer
#
#     def get_queryset(self):
#         date_start = request.query_params.get('startDate', None)
#         date_end = request.query_params.get('endDate', None)
#         result = InstructorHours.objects.filter(date__range=(date_start, date_end))
#         return result

@api_view(['GET'])
def api_get_instructor_hours(request):

    try:
        date_start = request.query_params.get('startDate', None)
        date_end = request.query_params.get('endDate', None)
        result = InstructorHours.objects.filter(date__range=(date_start, date_end))

        serializer = InstructorHoursSerializer(result, many=True)
        print('\n&&&&&&&&&&\n', date_start, date_end, '\n\n')
        print('DATA ', serializer.data)
        return Response(serializer.data)
    except InstructorHours.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
