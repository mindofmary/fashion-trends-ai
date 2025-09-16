import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

INPUT_FILE = "pinterest_clean.csv"

def train_model():
    df = pd.read_csv(INPUT_FILE)

    #features (texto) e target (repins)
    X = df["text"].fillna("")
    y = df["repin_count"]

    #vetorização TF-IDF
    vectorizer = TfidfVectorizer(max_features=500)
    X_tfidf = vectorizer.fit_transform(X)

    #dividir em treino-teste
    X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

    #regressão linear
    model = LinearRegression()  
    model.fit(X_train, y_train)

    #previsões
    y_pred = model.predict(X_test)

    #avaliação
    print("📉 MSE:", mean_squared_error(y_test, y_pred))
    print("📊 R²:", r2_score(y_test, y_pred))

    # Obter nomes das features (palavras) e coeficientes
    feature_names = vectorizer.get_feature_names_out()
    coefs = model.coef_

    # Top 10 palavras mais “positivas” (aumentam repins previstos)
    top_pos = sorted(zip(coefs, feature_names), reverse=True)[:10]

    # Top 10 palavras mais “negativas”
    top_neg = sorted(zip(coefs, feature_names))[:10]

    print("\n💡 Palavras associadas a MAIS repins:", top_pos)
    print("\n⚠️ Palavras associadas a MENOS repins:", top_neg)

    #gráfico real vs. previsão
    plt.scatter(y_test, y_pred, alpha=0.5)
    plt.xlabel("Repins reais")
    plt.ylabel("Repins previstos")
    plt.title("Comparação entre Repins Reais e Previstos")
    plt.show()

if __name__ == "__main__":
    train_model()