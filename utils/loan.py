from decimal import Decimal, ROUND_HALF_UP


MONEY = Decimal("0.01")


def calculate_monthly_payment(principal: Decimal, annual_rate_percent: Decimal, years: int) -> Decimal:
    """Calculate a fixed-rate loan payment using the standard amortization formula."""
    if principal < 0 or years <= 0:
        raise ValueError("principal must be non-negative and years must be positive")
    if annual_rate_percent < 0:
        raise ValueError("annual rate must be non-negative")

    months = years * 12
    if annual_rate_percent == 0:
        payment = principal / Decimal(months)
    else:
        monthly_rate = annual_rate_percent / Decimal("1200")
        compound = (Decimal("1") + monthly_rate) ** months
        payment = principal * monthly_rate * compound / (compound - Decimal("1"))
    return payment.quantize(MONEY, rounding=ROUND_HALF_UP)


def build_amortization_schedule(principal: Decimal, annual_rate_percent: Decimal, years: int) -> list[dict]:
    """Build a month-by-month schedule whose final balance is zero."""
    payment = calculate_monthly_payment(principal, annual_rate_percent, years)
    balance = principal
    monthly_rate = annual_rate_percent / Decimal("1200")
    schedule = []

    for month in range(1, years * 12 + 1):
        interest = (balance * monthly_rate).quantize(MONEY, rounding=ROUND_HALF_UP)
        principal_paid = payment - interest
        if month == years * 12:
            principal_paid = balance
            actual_payment = principal_paid + interest
        else:
            actual_payment = payment
        balance = (balance - principal_paid).quantize(MONEY, rounding=ROUND_HALF_UP)
        if balance < 0:
            balance = Decimal("0")
        schedule.append({
            "month": month,
            "payment": actual_payment.quantize(MONEY, rounding=ROUND_HALF_UP),
            "principal": principal_paid.quantize(MONEY, rounding=ROUND_HALF_UP),
            "interest": interest,
            "balance": balance,
        })

    if not schedule:
        raise ValueError("amortization requires at least one month")
    return schedule
