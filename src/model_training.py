import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

def train_model(data_path, model_path):
    df = pd.read_csv(data_path)
    X = df[['task_id', 'resources_allocated']]
    y = df['duration']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    print(f'Mean Absolute Error: {mae}')

    joblib.dump(model, model_path)

if __name__ == "__main__":
    train_model('data\\processed\\processed_data.csv', 'models\\project_timeline_model.pkl')
