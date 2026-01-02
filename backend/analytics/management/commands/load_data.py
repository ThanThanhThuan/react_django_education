import pandas as pd
from django.core.management.base import BaseCommand
from analytics.models import EducationData

class Command(BaseCommand):
    help = 'Load UNESCO data from CSV'

    def handle(self, *args, **kwargs):
        # Example logic - adjust column names based on your specific CSV
        df = pd.read_csv('data/unesco_data.csv') 
        
        # Clean data (remove rows with missing values)
        df = df.dropna(subset=['value']) 
        # indicatorId,geoUnit,year,value
        data_list = []
        for index, row in df.iterrows():
            data_list.append(EducationData(
                country=row['geoUnit'],
                year=row['year'],
                indicator=row['indicatorId'],
                # gender=row.get('Sex', 'Total'), # Adjust based on CSV headers
                value=row['value']
            ))
        
        EducationData.objects.bulk_create(data_list)
        self.stdout.write(self.style.SUCCESS('Data imported successfully!'))