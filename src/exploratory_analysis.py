import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import nltk
from nltk.corpus import stopwords

INPUT_FILE = "pinterest_clean.csv"

def explore_data():
    df = pd.read_csv(INPUT_FILE)
    print("✅ Dataset carregado:", df.shape)

    print("\n📊 Info:")
    print(df.info())

    print("\n📈 Estatísticas descritivas:")
    print(df.describe(include="all")) 

    #distribuição dos repins
    df["repin_count"].hist(bins=30)
    plt.title("Distribuição de Repins")
    plt.xlabel("Repins")
    plt.ylabel("Frequência")
    plt.xlim(0, 50)
    plt.show()

    # Top 10 palavras mais comuns no texto (removendo stopwords)
    nltk.download('stopwords', quiet=True)
    stop_words = set(stopwords.words('english'))
    words = " ".join(df["text"].dropna().tolist()).split()
    filtered_words = [w for w in words if w.lower() not in stop_words]
    common_words = Counter(filtered_words).most_common(10)
    print("\n🔠 Palavras mais comuns:", common_words)

if __name__ == "__main__":
    explore_data()