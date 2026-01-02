## Education Analytics Platform
🎓 Education Analytics Platform
📖 Project Overview

A full-stack web application designed to analyze global education trends using real-world data from UNESCO. The platform ingests raw CSV data, serves it via a REST API, 
visualizes historical trends on a React frontend, and uses Machine Learning to predict future statistics (e.g., literacy rates).

🛠 Tech Stack

Component	Technology	Purpose
Frontend	React.js	User Interface & Component State
Visualization	Chart.js	Rendering interactive line graphs
Backend	Django REST Framework	API endpoints & Business Logic
Database	PostgreSQL	Robust relational data storage
Data Processing	Pandas	Cleaning & transforming raw CSV data (ETL)
Machine Learning	Scikit-Learn	Linear Regression for trend prediction
Styling	Bootstrap 5	Responsive layout & UI components

📝 Setup checklist:

    Database: Create unesco_db in PostgreSQL.

    Backend Dependencies:

pip install django djangorestframework django-cors-headers psycopg2-binary pandas scikit-learn

Migrations: Run python manage.py migrate.

Load Data: Place unesco_data.csv in backend/data/ and run python manage.py load_data.

Frontend Dependencies:

npm install axios chart.js react-chartjs-2 bootstrap

Run: Start Django (python manage.py runserver) and React (npm start).

<img width="1710" height="1077" alt="image" src="https://github.com/user-attachments/assets/bb1d5b9e-9fba-4ea6-9eb2-fceae5781a89" />
