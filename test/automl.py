import pandas as pd
from sklearn.model_selection import train_test_split
from supervised.automl import AutoML
from sklearn.metrics import accuracy_score


df = pd.read_csv('../datasets/train.csv')

X = df.drop("y", axis=1)
y = df["y"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


automl = AutoML(
    mode="Explain",
    total_time_limit=60,
    eval_metric="logloss",
    explain_level=1
)

automl.fit(X_train, y_train)
preds = automl.predict(X_test)
print("Accuracy:", accuracy_score(y_test, preds))

automl.report()

leaderboard = automl.get_leaderboard()
print(leaderboard[["model_type", "metric_value", "train_time"]])
