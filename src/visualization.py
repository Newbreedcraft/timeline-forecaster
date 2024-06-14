import pandas as pd
import matplotlib.pyplot as plt

def plot_predictions(data_path):
    df = pd.read_csv(data_path)
    plt.figure(figsize=(10, 6))
    plt.scatter(df['task_id'], df['duration'], label='Actual Duration')
    plt.xlabel('Task ID')
    plt.ylabel('Duration (days)')
    plt.title('Project Timeline Predictions')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    plot_predictions('data\\processed\\processed_data.csv')
