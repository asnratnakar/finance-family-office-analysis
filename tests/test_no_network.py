import socket

import pandas as pd

from utils.metals import calculate_metal_valuation


def test_utility_calculations_make_no_network_requests(monkeypatch):
    def deny_network(*args, **kwargs):
        raise AssertionError("network access is forbidden")

    monkeypatch.setattr(socket, "create_connection", deny_network)

    transactions = pd.DataFrame(
        {
            "Metal": ["Gold", "Silver"],
            "Cost": ["2500", "300"],
            "Quantity_oz": ["1", "10"],
        }
    )
    prices = pd.DataFrame(
        {
            "Metal": ["Gold", "Silver"],
            "Spot Price USD": [2600, 31],
        }
    )
    result = calculate_metal_valuation(transactions, prices)

    assert len(result) == 2
