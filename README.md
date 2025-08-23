## without db, only local server
```
mlflow ui 
python3 main.py
```

## with local server
mlflow server \
  --host 0.0.0.0 --port 5000 \
  --backend-store-uri sqlite:///mlflow.db \
  --artifacts-destination ./artifacts



## init dvc 
pip3 install dvc
dvc init
#### create data/ folder and add a data.txt file
dvc add data/
