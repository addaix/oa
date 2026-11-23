"""The rarely used dependencies are extras, imported lazily (addaix/oa#36).

``import oa`` must work with pandas, tabled and beautifulsoup4 absent, and the parts that
need them must say which extra to install rather than fail with a bare import error.
"""

import re
import subprocess
import sys
from pathlib import Path

import pytest

BLOCKED = ("pandas", "tabled", "bs4", "dill")

PRELUDE = "import sys\n" + "".join(f"sys.modules[{m!r}] = None\n" for m in BLOCKED)


def _run(code):
    return subprocess.run(
        [sys.executable, "-c", PRELUDE + code], capture_output=True, text=True
    )


def test_import_oa_without_the_optional_dependencies():
    r = _run("import oa, oa.chats, oa.util, oa.tools; print('ok')")
    assert r.returncode == 0, r.stderr[-1500:]
    assert r.stdout.strip() == "ok"


def test_chat_html_parsing_names_the_html_extra():
    r = _run(
        "import oa.chats as c\n"
        "try:\n"
        "    c.parse_chat_html('<div id=\"thread\"></div>')\n"
        "except ImportError as e:\n"
        "    print(e)\n"
    )
    assert r.returncode == 0, r.stderr[-1500:]
    assert "'html' extra" in r.stdout


@pytest.mark.parametrize("module", ["oa.batch_embeddings", "oa._resources"])
def test_modules_that_need_extras_name_them(module):
    r = _run(f"try:\n    import {module}\nexcept ImportError as e:\n    print(e)\n")
    assert r.returncode == 0, r.stderr[-1500:]
    assert "extra" in r.stdout


def test_heavy_dependencies_are_not_core():
    text = (Path(__file__).parents[2] / "pyproject.toml").read_text()
    core = text.split("dependencies = [", 1)[1].split("]", 1)[0]
    assert not re.search(r'"(dill|pandas|tabled|beautifulsoup4)"', core)
