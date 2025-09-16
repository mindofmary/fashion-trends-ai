import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

DATA_PATH = "data/raw//pinterest_clean.csv"

def load_data():
    return pd.read_csv(DATA_PATH)

def train_model(df):
    #features (texto) e target (repins)
    X = df["text"]
    y = df["repin_count"]

    #vetorização TF-IDF
    vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
    X_vec = vectorizer.fit_transform(X).toarray()

    #divisão treino-teste
    X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

    #modelo de regressão linear (simples)
    model = LinearRegression()
    model.fit(X_train, y_train)

    #predições
    y_pred = model.predict(X_test)

    #avaliação
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f"📉 MSE: {mse:.2f}")
    print(f"📊 R²: {r2:.2f}")

    #visualização
    plt.scatter(y_test, y_pred, alpha=0.5, color="blue")
    plt.xlabel("Valores Reais (repins)")
    plt.ylabel("Previsão (repins)")
    plt.title("Previsão de popularidade com TF-IDF e Regressão Linear")
    plt.show()

def main():
    df = load_data()
    train_model(df)

if __name__ == "__main__":
    main()