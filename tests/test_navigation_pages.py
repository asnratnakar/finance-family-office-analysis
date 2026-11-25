from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_working_navigation_pages_exist():
    expected = {
        "pages/1_Bank_Accounts.py": "🏦 Bank Accounts",
        "pages/3_Retirement.py": "🎯 Retirement Planning",
        "pages/4_Market_Investments.py": "📈 Market Investments - Portfolio Analysis",
        "pages/5_Metals.py": "🧈 Metals Investment Performance Analysis",
        "pages/6_Loan_Calculator.py": "💳 Loan Repayment Calculator",
        "pages/7_Knowledge_Base.py": "📚 Knowledge Base Hub - Step-by-Step Learning Path",
        "pages/8_Family_Office.py": "👨‍👩‍👧‍👦 Family Office",
    }
    for relative_path, title in expected.items():
        source = (ROOT / relative_path).read_text(encoding="utf-8")
        assert title in source


def test_pages_do_not_read_data_samples():
    for page in (ROOT / "pages").glob("*.py"):
        assert "data/samples" not in page.read_text(encoding="utf-8")
