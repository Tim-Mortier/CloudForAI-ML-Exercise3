import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

def load_data(file_path):
    """
    Load the Titanic dataset from a CSV file.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded dataset.
    """
    return pd.read_csv(file_path)

def fill_missing_values(df):
    """
    Fill missing values in the dataset.

    Args:
        df (pd.DataFrame): Dataset with potential missing values.

    Returns:
        pd.DataFrame: Dataset with missing values handled.
    """
    df['Age'] = df['Age'].fillna(df['Age'].mean())
    df['Cabin'] = df['Cabin'].fillna('Unknown')
    df.dropna(subset=['Embarked'], inplace=True)
    return df

def encode_features(df):
    """
    Encode categorical features in the dataset.

    Args:
        df (pd.DataFrame): Dataset with categorical features.

    Returns:
        pd.DataFrame: Dataset with encoded features.
    """
    label_encoder = LabelEncoder()
    df['Sex'] = label_encoder.fit_transform(df['Sex'])

    one_hot_encoder = OneHotEncoder(sparse_output=False)
    embarked_encoded = one_hot_encoder.fit_transform(df[['Embarked']])
    embarked_df = pd.DataFrame(embarked_encoded, columns=one_hot_encoder.get_feature_names_out(['Embarked']))
    df = pd.concat([df, embarked_df], axis=1)
    df.drop('Embarked', axis=1, inplace=True)
    return df

def preprocess_data(file_path):
    """
    Load and preprocess the Titanic dataset.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pd.DataFrame, pd.Series: Preprocessed feature dataframe (X) and target series (y).
    """
    df = load_data(file_path)
    df = fill_missing_values(df)
    df = encode_features(df)
    df.dropna(inplace=True)
    X = df.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin', 'Survived'])
    y = df['Survived']
    return X, y

def train_model(X, y): 
    """
    Train a Random Forest model.

    Args:
        X (pd.DataFrame): Feature matrix.
        y (pd.Series): Target vector.

    Returns:
        model: Trained Random Forest model object.
    """
    model = RandomForestClassifier()
    model.fit(X, y)
    return model

def save_model(model, filename):
    """
    Save the trained model to a file using pickle.

    Args:
        model: Trained model object.
        filename (str): The filename where the model will be saved.
    """
    with open(filename, 'wb') as file:
        pickle.dump(model, file)

if __name__ == "__main__":
    file_path = "Titanic-Dataset.csv"
    X, y = preprocess_data(file_path)
    random_forest_model = train_model(X, y)
    save_model(random_forest_model, 'random_forest_model.pkl')
    print("Model saved successfully.")
