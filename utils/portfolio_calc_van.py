from decimal import Decimal

import pandas as pd


SUMMARY_COLUMNS = {"Symbol", "Cost", "Market Value", "Gain/Loss"}
ACTUAL_SUMMARY_COLUMNS = {
    "Symbol/CUSIP": "Symbol",
    "Total cost": "Cost",
    "Market Value": "Market Value",
    "Total Gain Loss": "Gain/Loss",
}


def normalize_vanguard_summary(cost_basis: pd.DataFrame) -> pd.DataFrame:
    """Normalize repository Vanguard CSV columns to utility column names."""
    if ACTUAL_SUMMARY_COLUMNS.keys() - set(cost_basis.columns):
        missing = sorted(ACTUAL_SUMMARY_COLUMNS.keys() - set(cost_basis.columns))
        if SUMMARY_COLUMNS - set(cost_basis.columns):
            raise ValueError("missing Vanguard columns: " + ", ".join(missing))
        return cost_basis
    return cost_basis.rename(columns=ACTUAL_SUMMARY_COLUMNS)


def calculate_vanguard_summary(cost_basis: pd.DataFrame) -> dict:
    """Summarize a Vanguard cost-basis fixture without guessing missing values."""
    cost_basis = normalize_vanguard_summary(cost_basis)
    if not SUMMARY_COLUMNS.issubset(cost_basis.columns):
        missing = sorted(SUMMARY_COLUMNS - set(cost_basis.columns))
        raise ValueError("missing Vanguard columns: " + ", ".join(missing))

    total_cost = sum((Decimal(str(value)) for value in cost_basis["Cost"]), Decimal("0"))
    market_value = sum(
        (Decimal(str(value)) for value in cost_basis["Market Value"]),
        Decimal("0"),
    )
    gain_loss = market_value - total_cost
    return {
        "holding_count": len(cost_basis),
        "total_cost": total_cost,
        "market_value": market_value,
        "gain_loss": gain_loss,
        "return_percent": (
            gain_loss / total_cost * Decimal("100")
            if total_cost != 0
            else None
        ),
    }


def sort_vanguard_summaries_by_date(paths: list) -> list:
    """Sort MMDDYYYY filenames chronologically, not lexically."""
    from datetime import datetime

    def parse_date(path):
        name = str(path).replace("\\", "/").rsplit("/", 1)[-1]
        digits = "".join(character for character in name if character.isdigit())
        if len(digits) >= 8:
            return datetime.strptime(digits[:8], "%m%d%Y")
        return datetime.min

    return sorted(paths, key=parse_date)
