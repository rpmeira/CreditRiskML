import kaggle
from pathlib import Path


def main():
    # Configuração do caminho absoluto
    project_root = Path(__file__).resolve().parents[2]  # Volta duas pastas (CreditRiskML/)
    raw_data_path = project_root / "fase_1_mvp" / "data" / "raw"  # Caminho completo

    # Garante que o diretório existe
    raw_data_path.mkdir(parents=True, exist_ok=True)

    # Download do dataset via Kaggle API
    dataset_name = "rikdifos/credit-card-approval-prediction"
    kaggle.api.dataset_download_files(dataset_name, path=str(raw_data_path), unzip=True)

    print(f"Dados baixados em: {raw_data_path}")


if __name__ == "__main__":
    main()
