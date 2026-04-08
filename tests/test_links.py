"""Test that all internal links on the site resolve to existing pages."""

import os
import re
from pathlib import Path
from urllib.parse import urlparse

import pytest
from bs4 import BeautifulSoup

PUBLIC_DIR = Path(__file__).parent.parent / "public"


def get_all_html_files():
    """Find all HTML files in public/."""
    return list(PUBLIC_DIR.rglob("*.html"))


def get_internal_links(html_path):
    """Extract all internal href links from an HTML file."""
    with open(html_path) as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        parsed = urlparse(href)
        # Skip external links, anchors, mailto, javascript
        if parsed.scheme in ("http", "https", "mailto", "javascript", ""):
            if parsed.netloc and parsed.netloc != "example.com" and parsed.netloc != "colinjoc.github.io":
                continue  # external
            if href.startswith("#"):
                continue  # anchor
            if href.startswith("mailto:"):
                continue
            # Internal link
            links.append((href, str(html_path.relative_to(PUBLIC_DIR))))
    return links


def resolve_link(href, public_dir):
    """Check if an internal link resolves to a file in public/."""
    parsed = urlparse(href)
    path = parsed.path

    # Strip the base URL if present
    path = re.sub(r"^https?://[^/]+", "", path)

    if not path or path == "/":
        return (public_dir / "index.html").exists()

    # Remove trailing slash
    path = path.rstrip("/")

    # Try exact path
    target = public_dir / path.lstrip("/")
    if target.exists():
        return True

    # Try path/index.html
    target_index = public_dir / path.lstrip("/") / "index.html"
    if target_index.exists():
        return True

    # Try path.html
    target_html = public_dir / (path.lstrip("/") + ".html")
    if target_html.exists():
        return True

    # Try as static file (css, js, images)
    if target.suffix:
        return target.exists()

    return False


class TestSiteLinks:
    """All internal links must resolve."""

    def test_public_dir_exists(self):
        assert PUBLIC_DIR.exists(), f"Run 'hugo' first — {PUBLIC_DIR} not found"

    def test_index_exists(self):
        assert (PUBLIC_DIR / "index.html").exists()

    def test_all_internal_links_resolve(self):
        """Every internal href in every HTML page must resolve to an existing file."""
        broken = []
        all_html = get_all_html_files()
        assert len(all_html) > 0, "No HTML files found"

        for html_file in all_html:
            links = get_internal_links(html_file)
            for href, source in links:
                if not resolve_link(href, PUBLIC_DIR):
                    broken.append(f"{source} → {href}")

        if broken:
            msg = f"{len(broken)} broken links:\n" + "\n".join(f"  {b}" for b in broken)
            pytest.fail(msg)

    def test_nav_links_resolve(self):
        """Navigation links must work from every page."""
        nav_targets = ["/", "/principles/", "/hdr/", "/hdr/results/"]
        for target in nav_targets:
            assert resolve_link(target, PUBLIC_DIR), f"Nav link {target} is broken"

    def test_results_cards_have_valid_links(self):
        """Each result card on /hdr/results/ must link to an existing page."""
        results_page = PUBLIC_DIR / "hdr" / "results" / "index.html"
        if not results_page.exists():
            pytest.skip("Results page not built")

        with open(results_page) as f:
            soup = BeautifulSoup(f.read(), "html.parser")

        cards = soup.find_all("a", class_="card")
        assert len(cards) > 0, "No result cards found"

        for card in cards:
            href = card["href"]
            assert resolve_link(href, PUBLIC_DIR), f"Card link broken: {href}"

    def test_css_loads(self):
        """CSS file must exist."""
        assert (PUBLIC_DIR / "css" / "style.css").exists()

    def test_no_empty_pages(self):
        """No HTML page should be essentially empty (< 100 bytes of content)."""
        for html_file in get_all_html_files():
            size = html_file.stat().st_size
            assert size > 100, f"{html_file.relative_to(PUBLIC_DIR)} is too small ({size} bytes)"
