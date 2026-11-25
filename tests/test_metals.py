from decimal import Decimal

import pandas as pd

from utils.metals import calculate_metal_valuation


def test_metal_cost_market_value_and_gain_use_fixed_data():
    transactions = pd.DataFrame({
        "Metal": ["Gold", "Silver"],
        "Cost": ["2500", "300"],
        "Quantity_oz": ["1", "10"],
    })
    prices = pd.DataFrame({
        "Metal": ["Gold", "Silver"],
        "Spot Price USD": [2600, 31],
    })

    result = calculate_metal_valuation(transactions, prices).set_index("Metal")

    assert result.loc["Gold", "Cost"] == Decimal("2500")
    assert result.loc["Gold", "Market Value"] == Decimal("2600")
    assert result.loc["Gold", "Gain/Loss"] == Decimal("100")
    assert result.loc["Silver", "Market Value"] == Decimal("310")


def test_missing_metal_price_is_unavailable_not_zero():
    transactions = pd.DataFrame({"Metal": ["Platinum"], "Cost": ["1000"], "Quantity_oz": ["2"]})
    prices = pd.DataFrame({"Metal": ["Gold"], "Spot Price USD": [2600]})

    result = calculate_metal_valuation(transactions, prices).iloc[0]

    assert result["Market Value"] is None
    assert result["Gain/Loss"] is None


def test_zero_quantity_has_zero_market_value_and_records_cost_loss():
    transactions = pd.DataFrame({"Metal": ["Gold"], "Cost": ["500"], "Quantity_oz": ["0"]})
    prices = pd.DataFrame({"Metal": ["Gold"], "Spot Price USD": [2600]})

    result = calculate_metal_valuation(transactions, prices).iloc[0]

    assert result["Market Value"] == Decimal("0")
    assert result["Gain/Loss"] == Decimal("-500")
