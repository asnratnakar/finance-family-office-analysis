from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_entry_point_exists():
    entry = ROOT / "PersonalPortfolioAnalysis.py"
    assert entry.is_file()
    assert 'Welcome to Personal Financial Analysis Dashboard' in entry.read_text(encoding="utf-8")


def test_synthetic_data_is_allowed():
    assert (ROOT / "data" / "samples" / "README.md").is_file()


def test_real_data_ignore_rule_exists():
    gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
    assert "data/*" in gitignore
    assert "!data/samples/" in gitignore
    assert "input/" in gitignore
    assert "*.keys" in gitignore
