export DAGSHUB_USER="larawehbe"
export DAGSHUB_TOKEN="a34088c281b85d322f6f186009db1e874e612a5e"



docker run --rm -p 8000:8000 \
  -e MLFLOW_TRACKING_URI="https://dagshub.com/larawehbe/mlflow-test-saturday.mlflow" \
  -e MLFLOW_TRACKING_USERNAME="$DAGSHUB_USER" \
  -e MLFLOW_TRACKING_PASSWORD="$DAGSHUB_TOKEN" \
  -e DAGSHUB_OWNER="larawehbe" \
  -e DAGSHUB_REPO="mlflow-test-saturday" \
  iris-api:latest