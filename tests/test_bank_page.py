from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_bank_page_preserves_required_labels():
    source = (ROOT / "pages" / "1_Bank_Accounts.py").read_text(encoding="utf-8")
    required = [
        "🏦 Bank Accounts",
        "💰 Checking Accounts",
        "🏪 Savings Accounts",
        "💳 Certificate of Deposit (CD) Accounts",
        "📊 Fed Funds vs Inflation vs Savings Rate",
        "What would you like to calculate?",
        "Future Value (PV → FV)",
        "Present Value (FV → PV)",
    ]
    for label in required:
        assert label in source


def test_bank_page_uses_local_category_loader():
    source = (ROOT / "pages" / "1_Bank_Accounts.py").read_text(encoding="utf-8")
    assert "read_checking_accounts" in source
    assert "read_savings_accounts" in source
    assert "read_cd_accounts" in source
    assert "data/samples" not in source
