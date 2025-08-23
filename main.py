import mlflow
import mlflow.sklearn
from mlflow.models.signature import infer_signature
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1) Point to your tracking server + experiment
# mlflow.set_tracking_uri("http://127.0.0.1:5000")
# mlflow.set_experiment("mlops-course")
import dagshub
dagshub.init(repo_owner='larawehbe', repo_name='mlflow-test-saturday', mlflow=True)
# mlflow.set_tracking_uri("https://dagshub.com/larawehbe/mlflow-test-saturday.mlflow")
mlflow.set_experiment("mlops-course")


# import dagshub
# dagshub.init(repo_owner='larawehbe', repo_name='mlflow-dvc-example', mlflow=True)

X, y = load_iris(return_X_y=True)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

MODEL_NAME = "mlops-course_model"   # will be created in Registry if it doesn't exist

print(f"Training model and logging to MLflow Tracking & Registry servers...")
for n in [10, 50, 100]:
    with mlflow.start_run(run_name=f"rf_n={n}", tags={"model": "rf", "dataset": "iris"}):
        print(f"Training RandomForest with n_estimators={n}")
        # 2) Vary the hyperparam correctly
        max_depth = 5
        clf = RandomForestClassifier(n_estimators=n, max_depth=max_depth, random_state=42)

        # Train & eval
        clf.fit(X_tr, y_tr)
        preds = clf.predict(X_te)
        acc = accuracy_score(y_te, preds)

        # 3) Log params/metrics
        mlflow.log_param("n_estimators", n)
        mlflow.log_param("max_depth", max_depth)
        mlflow.log_metric("accuracy", acc)

        # 4) Save signature so serving knows the input schema
        signature = infer_signature(X_tr, clf.predict(X_tr))

        # 5) Log model AND auto-register in the Model Registry
        info = mlflow.sklearn.log_model(
            sk_model=clf,
            artifact_path="model",
            signature=signature,
            registered_model_name=MODEL_NAME,  # <-- creates/updates a registered model
        )

        print(f"Logged run_id={info.run_id}  |  registered model={MODEL_NAME}")
