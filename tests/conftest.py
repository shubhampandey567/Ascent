import shutil
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "tools"))

import srs  # noqa: E402
import tracker  # noqa: E402


@pytest.fixture
def workspace(tmp_path):
    """A throwaway copy of the curriculum with an empty tracker, so tests never touch real progress."""
    shutil.copytree(REPO / "curriculum", tmp_path / "curriculum")
    (tmp_path / "tracker").mkdir()
    tracker.use_root(tmp_path)
    yield tmp_path
    tracker.use_root(REPO)


def run(*args: str) -> None:
    """Run a tracker command the way the Mentor does."""
    tracker.main(list(args))


@pytest.fixture
def cli():
    return run


__all__ = ["srs", "tracker"]
