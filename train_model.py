import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load your dataset
df = pd.read_csv('path_to_your_asl_dataset.csv')  # Update with your actual path

# Assume columns: landmark_0_x, landmark_0_y, ..., landmark_20_z, label
X = df.drop('label', axis=1).values
y = df['label'].values

# Train model
clf = RandomForestClassifier()
clf.fit(X, y)

# Save model
joblib.dump(clf, 'asl_model.pkl')
print("Model trained and saved as asl_model.pkl")