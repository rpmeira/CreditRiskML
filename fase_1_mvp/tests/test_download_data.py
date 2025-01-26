from pathlib import Path
# from ..src import download_data


def test_raw_data_directory_created():
    project_root = Path(__file__).resolve().parents[2]  # Volta duas pastas (CreditRiskML/)
    raw_path = project_root / "fase_1_mvp" / "data" / "raw"

    assert raw_path.exists(), f"Diretório {raw_path} não foi criado!"
    assert raw_path.is_dir(), f"{raw_path} não é um diretório!"
