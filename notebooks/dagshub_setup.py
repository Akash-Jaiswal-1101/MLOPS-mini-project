import mlflow
import dagshub

mlflow.set_tracking_uri("https://dagshub.com/Akash-Jaiswal-1101/MLOPS-mini-project.mlflow")
dagshub.init(repo_owner='Akash-Jaiswal-1101', repo_name='MLOPS-mini-project', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)