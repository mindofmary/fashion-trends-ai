import requests
import json
import os
from datetime import datetime

# ================================
# CONFIGURAÇÕES DO PINTEREST
# ================================
ACCESS_TOKEN = "COLOCA_O_TEUS_TOKEN_AQUI"  # <-- Substitui pelo teu token
BASE_URL = "https://api.pinterest.com/v5"

# Pasta para guardar os dados
DATA_FOLDER = "data/raw"
os.makedirs(DATA_FOLDER, exist_ok=True)


# ================================
# FUNÇÃO PARA BUSCAR PINS
# ================================
def get_pinterest_pins(board_id, limit=25):
    """
    Busca pins de um board específico no Pinterest.
    Args:
        board_id (str): ID do board do Pinterest
        limit (int): Número de pins a buscar (máx. 50)
    Returns:
        list: Lista de pins
    """
    url = f"{BASE_URL}/boards/{board_id}/pins"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    params = {
        "page_size": limit
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        print(f"✅ {limit} pins carregados do board {board_id}")
        return response.json().get("items", [])
    else:
        print(f"❌ Erro ao buscar pins: {response.status_code} - {response.text}")
        return []


# ================================
# SALVAR DADOS EM JSON
# ================================
def save_pins_to_json(pins, filename="pins_raw.json"):
    """
    Salva os pins num ficheiro JSON na pasta data/raw.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(DATA_FOLDER, f"{timestamp}_{filename}")

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(pins, f, indent=4, ensure_ascii=False)

    print(f"💾 Dados salvos em: {filepath}")


# ================================
# EXECUÇÃO
# ================================
if __name__ == "__main__":
    BOARD_ID = "exemplo_board_id"  # <-- Substitui pelo ID do board
    pins = get_pinterest_pins(BOARD_ID, limit=10)

    if pins:
        save_pins_to_json(pins)
