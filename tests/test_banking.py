from decimal import Decimal

import pandas as pd

from utils.banking import (
    calculate_cd_maturity,
    calculate_future_value,
    calculate_present_value,
    latest_checking_balances,
    normalize_savings_accounts,
)


def test_checking_latest_balance_uses_month_and_year_not_row_text():
    frame = pd.DataFrame({
        "Account Name": ["Checking", "Checking", "Checking"],
        "Month": ["Dec", "Jan", "Feb"],
        "Year": [2025, 2026, 2026],
        "Ending Balance": [100, 200, 300],
    })

    latest = latest_checking_balances(frame)

    assert latest.iloc[0]["Month"] == "Feb"
    assert latest.iloc[0]["Year"] == 2026
    assert latest.iloc[0]["Ending Balance"] == 300


def test_savings_supports_ending_balance_and_current_balance_columns():
    frame = pd.DataFrame({
        "Account Name": ["Savings A", "Savings B"],
        "Current Balance": [1000, 2500],
    })

    result = normalize_savings_accounts(frame)

    assert result["Balance"].tolist() == [1000, 2500]


def test_cd_maturity_uses_true_effective_annual_apy():
    maturity = calculate_cd_maturity(Decimal("5500"), Decimal("4.5"), 24)
    assert maturity == Decimal("6006.14")


def test_future_value_matches_annual_compounding():
    future = calculate_future_value(Decimal("10000"), Decimal("4.5"), Decimal("5"), 1)
    assert future == Decimal("12461.82")


def test_present_value_reverses_future_value():
    present = calculate_present_value(Decimal("15000"), Decimal("4.5"), Decimal("5"), 1)
    assert present == Decimal("12036.77")
