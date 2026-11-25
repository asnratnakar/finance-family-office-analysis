from decimal import Decimal
from pathlib import Path

import pandas as pd

from utils.portfolio_calc_van import calculate_vanguard_summary, sort_vanguard_summaries_by_date


def test_vanguard_summary_reconciles_fixed_synthetic_holdings():
    cost_basis = pd.DataFrame(
        {
            "Symbol": ["VTI", "VXUS"],
            "Cost": ["6000.00", "3000.00"],
            "Market Value": ["7200.00", "2700.00"],
            "Gain/Loss": ["1200.00", "-300.00"],
        }
    )

    summary = calculate_vanguard_summary(cost_basis)

    assert summary["holding_count"] == 2
    assert summary["total_cost"] == Decimal("9000.00")
    assert summary["market_value"] == Decimal("9900.00")
    assert summary["gain_loss"] == Decimal("900.00")
    assert summary["return_percent"].quantize(Decimal("0.01")) == Decimal("10.00")


def test_vanguard_filename_sort_uses_date_not_text():
    paths = ["VAN_summary_12052024.csv", "VAN_summary_03042026.csv", "VAN_summary_04162025.csv"]

    sorted_paths = sort_vanguard_summaries_by_date(paths)

    assert [Path(path).name for path in sorted_paths] == [
        "VAN_summary_12052024.csv",
        "VAN_summary_04162025.csv",
        "VAN_summary_03042026.csv",
    ]


def test_vanguard_missing_column_is_rejected():
    try:
        calculate_vanguard_summary(pd.DataFrame({"Symbol": ["VTI"]}))
    except ValueError as error:
        assert "missing Vanguard columns" in str(error)
    else:
        raise AssertionError("missing Vanguard columns should be rejected")
