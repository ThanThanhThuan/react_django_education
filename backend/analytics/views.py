from rest_framework import viewsets, filters # Import filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import EducationData
from .serializers import EducationDataSerializer
from sklearn.linear_model import LinearRegression
import numpy as np

class EducationViewSet(viewsets.ModelViewSet):
    queryset = EducationData.objects.all()
    serializer_class = EducationDataSerializer
    
    # Add these two lines to enable ?search=India
    filter_backends = [filters.SearchFilter]
    search_fields = ['country'] 

    @action(detail=False, methods=['get'])
    def predict(self, request):
        # ... (keep your existing predict logic here)
        # pass
        """
        Predict future trends for a specific country and indicator.
        Query params: ?country=India&indicator=Literacy Rate
        """
        country = request.query_params.get('country')
        indicator = request.query_params.get('indicator')
        
        # data = EducationData.objects.filter(country=country, indicator=indicator).order_by('year')
        data = EducationData.objects.filter(geoUnit=country, indicatorId=indicator).order_by('year')
        
        if not data.exists():
            return Response({"error": "No data found"}, status=404)

        # Prepare ML Data
        X = np.array([d.year for d in data]).reshape(-1, 1)
        y = np.array([d.value for d in data])

        model = LinearRegression()
        model.fit(X, y)

        # Predict next 5 years
        future_years = np.array([[y] for y in range(X[-1][0] + 1, X[-1][0] + 6)])
        predictions = model.predict(future_years)

        return Response({
            "country": country,
            "indicator": indicator,
            "future_years": future_years.flatten(),
            "predicted_values": predictions
        })