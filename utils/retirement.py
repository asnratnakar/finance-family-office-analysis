from decimal import Decimal


def estimate_future_value(principal: Decimal, annual_rate: Decimal, years: int) -> Decimal:
    """Hand-calculable retirement projection helper."""
    if principal < 0 or annual_rate < 0 or years < 0:
        raise ValueError("retirement inputs must be non-negative")
    return principal * (Decimal("1") + annual_rate / Decimal("100")) ** years
