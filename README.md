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

then add dvc add data/data.txt

#### now add dagshub
| to work with dagshub, we need mlflow<3
import dagshub
dagshub.init(repo_owner='larawehbe', repo_name='mlflow-test-saturday', mlflow=True)