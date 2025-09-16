import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re

DATA_PATH="data/processed/pinterest_clean.csv"

def load_data():
    return pd.read_csv(DATA_PATH)

def basic_stats(df):
    print("📊 Informações gerais do dataset:")
    print(df.info())
    print("\n📈 Estatísticas descritivas:")
    print(df.describe(include="all"))

def plot_repin_distribution(df):
    plt.figure(figsize=(8, 5))
    df['repin_count'].hist(bins=50, color='skyblue', edgecolor='black')
    plt.title("Distribuição de Repins")
    plt.xlabel("Número de Repins")
    plt.ylabel("Frequência")
    plt.show()

def top_words(df, text_column="text", top_n=20):
    all_text = " ".join(df[text_column].dropna())
    words = re.findall(r"\b[a-z]{3,}\b", all_text)  # filtra palavras com 3+ letras
    counter = Counter(words)
    print(f"📝 Top {top_n} palavras:")
    for word, freq in counter.most_common(top_n):
        print(f"{word}: {freq}")

def main():
    df = load_data()
    basic_stats(df)
    plot_repin_distribution(df)
    top_words(df, text_column="text", top_n=20)

if __name__ == "__main__":
    main()