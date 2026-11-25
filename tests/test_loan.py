from decimal import Decimal

from utils.loan import build_amortization_schedule, calculate_monthly_payment


def test_monthly_payment_matches_hand_calculation():
    payment = calculate_monthly_payment(Decimal("200000"), Decimal("5.5"), 30)
    assert payment == Decimal("1135.58")


def test_zero_interest_payment_is_principal_divided_by_months():
    payment = calculate_monthly_payment(Decimal("12000"), Decimal("0"), 1)
    assert payment == Decimal("1000.00")


def test_amortization_final_balance_is_zero():
    schedule = build_amortization_schedule(Decimal("12000"), Decimal("0"), 1)
    assert len(schedule) == 12
    assert schedule[-1]["balance"] == Decimal("0")
    assert sum(row["principal"] for row in schedule) == Decimal("12000.00")


def test_negative_principal_is_rejected():
    try:
        calculate_monthly_payment(Decimal("-1"), Decimal("5"), 1)
    except ValueError as error:
        assert "principal" in str(error)
    else:
        raise AssertionError("negative principal should be rejected")
