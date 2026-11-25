from datetime import date
from decimal import Decimal, ROUND_HALF_UP

import pandas as pd


MONEY = Decimal("0.01")
MONTHS = {
    "jan": 1, "january": 1, "feb": 2, "february": 2,
    "mar": 3, "march": 3, "apr": 4, "april": 4,
    "may": 5, "jun": 6, "june": 6, "jul": 7, "july": 7,
    "aug": 8, "august": 8, "sep": 9, "september": 9,
    "oct": 10, "october": 10, "nov": 11, "november": 11,
    "dec": 12, "december": 12,
}


def normalize_checking_accounts(frame: pd.DataFrame) -> pd.DataFrame:
    required = {"Account Name", "Month", "Year", "Ending Balance"}
    missing = sorted(required - set(frame.columns))
    if missing:
        raise ValueError("missing checking columns: " + ", ".join(missing))

    result = frame.copy()
    result["Month"] = result["Month"].astype(str).str.strip()
    result["Year"] = pd.to_numeric(result["Year"])

    def month_number(value: str) -> int:
        return MONTHS.get(str(value).lower().strip(), 0)

    result["__month_number"] = result["Month"].map(month_number)
    if (result["__month_number"] == 0).any():
        raise ValueError("checking data contains an invalid month")
    result["__date"] = result.apply(
        lambda row: date(int(row["Year"]), int(row["__month_number"]), 1), axis=1
    )
    result["Ending Balance"] = pd.to_numeric(result["Ending Balance"])
    return result.sort_values(["Account Name", "__date"])


def latest_checking_balances(frame: pd.DataFrame) -> pd.DataFrame:
    normalized = normalize_checking_accounts(frame)
    latest = normalized.sort_values("__date").groupby("Account Name", as_index=False).tail(1)
    return latest[["Account Name", "Month", "Year", "Ending Balance"]].copy()


def normalize_savings_accounts(frame: pd.DataFrame) -> pd.DataFrame:
    if "Account Name" not in frame.columns:
        raise ValueError("missing savings columns: Account Name")
    balance_column = "Ending Balance" if "Ending Balance" in frame.columns else "Current Balance"
    if balance_column not in frame.columns:
        raise ValueError("missing savings balance column")
    result = frame[["Account Name", balance_column]].copy()
    result["Balance"] = pd.to_numeric(result[balance_column])
    return result[["Account Name", "Balance"]]


def calculate_cd_maturity(principal: Decimal, apy_percent: Decimal, term_months: int) -> Decimal:
    """Apply APY as a true effective annual rate over the CD term."""
    if principal < 0:
        raise ValueError("principal must be non-negative")
    if apy_percent < 0:
        raise ValueError("APY must be non-negative")
    if term_months < 0:
        raise ValueError("term months must be non-negative")
    years = Decimal(term_months) / Decimal("12")
    maturity = principal * (Decimal("1") + apy_percent / Decimal("100") ) ** years
    return maturity.quantize(MONEY, rounding=ROUND_HALF_UP)


def calculate_future_value(present_value: Decimal, annual_rate_percent: Decimal, years: Decimal, compounds_per_year: int) -> Decimal:
    if present_value < 0 or annual_rate_percent < 0 or years < 0:
        raise ValueError("PV/FV inputs must be non-negative")
    if compounds_per_year <= 0:
        raise ValueError("compounding frequency must be positive")
    rate = annual_rate_percent / Decimal("100") / Decimal(compounds_per_year)
    periods = years * Decimal(compounds_per_year)
    future = present_value * (Decimal("1") + rate) ** periods
    return future.quantize(MONEY, rounding=ROUND_HALF_UP)


def calculate_present_value(future_value: Decimal, annual_rate_percent: Decimal, years: Decimal, compounds_per_year: int) -> Decimal:
    if future_value < 0 or annual_rate_percent < 0 or years < 0:
        raise ValueError("PV/FV inputs must be non-negative")
    if compounds_per_year <= 0:
        raise ValueError("compounding frequency must be positive")
    rate = annual_rate_percent / Decimal("100") / Decimal(compounds_per_year)
    periods = years * Decimal(compounds_per_year)
    present = future_value / (Decimal("1") + rate) ** periods
    return present.quantize(MONEY, rounding=ROUND_HALF_UP)
