conda env create -f environment.yml

env FLASK_APP=api.py flask run

curl -F file=@test2-predictions.csv localhost:5000/pred