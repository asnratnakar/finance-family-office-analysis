from decimal import Decimal

import pandas as pd


def calculate_metal_valuation(transactions: pd.DataFrame, spot_prices: pd.DataFrame) -> pd.DataFrame:
    """Aggregate metal costs and quantities and apply the dated spot-price table."""
    required_transactions = {"Metal", "Cost", "Quantity_oz"}
    required_prices = {"Metal", "Spot Price USD"}
    if not required_transactions.issubset(transactions.columns):
        raise ValueError("transactions require Metal, Cost, and Quantity_oz")
    if not required_prices.issubset(spot_prices.columns):
        raise ValueError("spot prices require Metal and Spot Price USD")

    grouped = transactions.groupby("Metal", as_index=False).agg({
        "Cost": "sum",
        "Quantity_oz": "sum",
    })
    grouped["Cost"] = grouped["Cost"].map(Decimal)
    grouped["Quantity_oz"] = grouped["Quantity_oz"].map(Decimal)

    price_lookup = {
        str(row["Metal"]): Decimal(str(row["Spot Price USD"]))
        for _, row in spot_prices.iterrows()
    }

    records = []
    for row in grouped.itertuples(index=False):
        metal = str(row.Metal)
        quantity = row.Quantity_oz
        cost = row.Cost
        price = price_lookup.get(metal)
        if quantity == 0:
            market_value = Decimal("0")
            gain_loss = -cost
        elif price is None:
            market_value = None
            gain_loss = None
        else:
            market_value = price * quantity
            gain_loss = market_value - cost
        records.append({
            "Metal": metal,
            "Cost": cost,
            "Quantity_oz": quantity,
            "Spot Price USD": price,
            "Market Value": market_value,
            "Gain/Loss": gain_loss,
        })
    return pd.DataFrame(records)
