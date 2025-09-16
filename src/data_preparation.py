import pandas as pd

INPUT_FILE="pinterest_finalised_2.csv"
OUTPUT_FILE="pinterest_clean.csv"

def load_and_clean_data():
    df = pd.read_csv(INPUT_FILE)
    print("✅ Dataset carregado:", df.shape)

    # Remover coluna inútil
    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])
    
    # Preencher valores nulos
    df["title"] = df["title"].fillna("").astype(str).str.strip()
    df["description"] = df["description"].fillna("").astype(str).str.strip()

    # Criar uma coluna de texto unificada
    df["text"] = (df["title"] + " " + df["description"]).str.lower().str.strip()

    # Garantir que repin_count é numérico
    df["repin_count"] = pd.to_numeric(df["repin_count"], errors="coerce").fillna(0).astype(int)

    df.to_csv(OUTPUT_FILE, index=False)
    print("💾 Dataset limpo guardado como:", OUTPUT_FILE)

if __name__ == "__main__":
    load_and_clean_data()