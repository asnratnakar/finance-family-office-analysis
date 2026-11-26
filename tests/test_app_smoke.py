from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_entry_point_exists():
    entry = ROOT / "PersonalPortfolioAnalysis.py"
    assert entry.is_file()
    assert 'Welcome to Personal Financial Analysis Dashboard' in entry.read_text(encoding="utf-8")


def test_real_data_ignore_rule_exists():
    gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
    assert "data/*" in gitignore
    assert "input/" in gitignore
    assert "*.keys" in gitignore


def test_local_data_category_folders_exist():
    for category in ("banking", "metals", "portfolio"):
        assert (ROOT / "data" / category).is_dir()


def test_local_data_loader_module_exists():
    assert (ROOT / "utils" / "local_data.py").is_file()


def test_sample_data_directory_does_not_exist():
    assert not (ROOT / "data" / "sample").is_dir()
