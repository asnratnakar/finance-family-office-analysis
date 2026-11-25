from decimal import Decimal

from utils.retirement import estimate_future_value


def test_retirement_future_value_matches_hand_calculation():
    assert estimate_future_value(Decimal("10000"), Decimal("7"), 10).quantize(Decimal("0.01")) == Decimal("19671.51")
