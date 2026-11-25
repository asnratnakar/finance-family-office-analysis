from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_ROOT = PROJECT_ROOT / "data"


def read_local_csv(category: str, filename: str) -> pd.DataFrame:
    """Read a commit-ignored local CSV from its category folder."""
    path = DATA_ROOT / category / filename
    if not path.is_file():
        raise FileNotFoundError(f"Local data file is unavailable: {path}")
    return pd.read_csv(path)


def read_checking_accounts() -> pd.DataFrame:
    return read_local_csv("banking", "checkingAccounts.csv")


def read_savings_accounts() -> pd.DataFrame:
    return read_local_csv("banking", "savingsAccounts.csv")


def read_cd_accounts() -> pd.DataFrame:
    return read_local_csv("banking", "cdAccounts.csv")


def read_metal_transactions() -> pd.DataFrame:
    return read_local_csv("metals", "metals_transactionHistory.csv")


def read_metal_spot_prices() -> pd.DataFrame:
    return read_local_csv("metals", "metals_spotPrice.csv")


def find_latest_vanguard_summary() -> Path:
    folder = DATA_ROOT / "portfolio"
    candidates = list(folder.glob("VAN_costbasis_summary_*.csv"))
    if not candidates:
        raise FileNotFoundError("No Vanguard summary CSV found in data/portfolio")

    def report_date(path: Path):
        stem = path.stem.rsplit("_", 1)[-1]
        if len(stem) == 8 and stem.isdigit():
            return stem
        return "00000000"

    return max(candidates, key=report_date)


def read_latest_vanguard_summary() -> pd.DataFrame:
    return pd.read_csv(find_latest_vanguard_summary())
