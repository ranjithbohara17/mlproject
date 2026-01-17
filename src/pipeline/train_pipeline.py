import os
import sys
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression


# Paths
ARTIFACTS_DIR = "artifacts"
DATA_PATH = os.path.join("artifacts", "data.csv")

MODEL_PATH = os.path.join("artifacts", "model.pkl")
PREPROCESSOR_PATH = os.path.join("artifacts", "preprocessor.pkl")


def save_object(file_path, obj):
    with open(file_path, "wb") as file:
        pickle.dump(obj, file)


def train_model():

    print("Reading dataset...")
    df = pd.read_csv(DATA_PATH)

    print("Splitting features and target...")
    X = df.drop("math_score", axis=1)
    y = df["math_score"]

    print("Train test split...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    num_features = ["reading_score", "writing_score"]

    cat_features = [
        "gender",
        "race_ethnicity",
        "parental_level_of_education",
        "lunch",
        "test_preparation_course"
    ]

    print("Building preprocessing pipeline...")

    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(handle_unknown="ignore")

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, num_features),
            ("cat", categorical_transformer, cat_features)
        ]
    )

    print("Building model pipeline...")

    model = LinearRegression()

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model)
        ]
    )

    print("Training model...")
    pipeline.fit(X_train, y_train)

    print("Saving model and preprocessor...")

    # Extract fitted parts
    fitted_preprocessor = pipeline.named_steps["preprocessor"]
    fitted_model = pipeline.named_steps["model"]

    os.makedirs(ARTIFACTS_DIR, exist_ok=True)

    save_object(PREPROCESSOR_PATH, fitted_preprocessor)
    save_object(MODEL_PATH, fitted_model)

    print("Training completed successfully ✅")


if __name__ == "__main__":
    train_model()
