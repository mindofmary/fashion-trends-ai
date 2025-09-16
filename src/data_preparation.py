import os
import pandas as pd

DATA_PATH="data/raw/pinterest_finalised_2.csv"
OUTPUT_PATH="data/processed/"
os.makedirs(OUTPUT_PATH, exist_ok=True)

def load_data():
    df = pd.read_csv(DATA_PATH)
    print(f"✅ Dataset carregado com {df.shape[0]} linhas e {df.shape[1]} colunas.")
    return df

def clean_data(df):
    #remover coluna inútil
    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])
    
    #preencher valores nulos
    df["title"] = df["title"].fillna("").astype(str).str.strip()
    df["description"] = df["description"].fillna("").astype(str).str.strip()

    #criar uma coluna de texto unificada
    df["text"] = (df["title"] + " " + df["description"]).str.lower().str.strip()

    #garantir que repin_count é numérico
    df["repin_count"] = pd.to_numeric(df["repin_count"], errors="coerce").fillna(0).astype(int)

    print("✨ Dados limpos e normalizados.")
    return df

def save_clean_data(df):
    output_file = os.path.join(OUTPUT_PATH, "pinterest_clean.csv")
    df.to_csv(output_file, index=False)
    print(f"💾 Dados limpos salvos em {output_file}")

def main():
    df = load_data()
    df = clean_data(df)
    save_clean_data(df)

if __name__ == "__main__":
    main()