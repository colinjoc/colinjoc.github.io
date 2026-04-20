"""Test that the topic filter dropdown on /hdr/results/ works correctly."""

from pathlib import Path

import pytest
from bs4 import BeautifulSoup

PUBLIC_DIR = Path(__file__).parent.parent / "public"
RESULTS_PAGE = PUBLIC_DIR / "hdr" / "results" / "index.html"


@pytest.fixture
def soup():
    """Parse the results page."""
    if not RESULTS_PAGE.exists():
        pytest.skip("Results page not built — run 'hugo' first")
    with open(RESULTS_PAGE) as f:
        return BeautifulSoup(f.read(), "html.parser")


class TestTopicFilterDropdown:
    """The results page must have a working topic filter dropdown."""

    def test_filter_select_exists(self, soup):
        """A <select> element with id='topic-filter' must exist."""
        select = soup.find("select", id="topic-filter")
        assert select is not None, "No <select id='topic-filter'> found"

    def test_filter_has_all_topics_option(self, soup):
        """First option must be 'All topics' with empty value."""
        select = soup.find("select", id="topic-filter")
        options = select.find_all("option")
        assert len(options) > 0
        assert options[0]["value"] == ""
        assert "All" in options[0].text

    def test_filter_options_match_card_domains(self, soup):
        """Every domain in the cards must appear as a filter option, and vice versa."""
        select = soup.find("select", id="topic-filter")
        options = {opt["value"] for opt in select.find_all("option") if opt["value"]}

        cards = soup.find_all("a", class_="card")
        card_domains = {card["data-domain"] for card in cards if card.get("data-domain")}

        assert options == card_domains, (
            f"Mismatch:\n"
            f"  In dropdown but not cards: {options - card_domains}\n"
            f"  In cards but not dropdown: {card_domains - options}"
        )

    def test_filter_options_are_sorted(self, soup):
        """Filter options (excluding 'All topics') must be alphabetically sorted."""
        select = soup.find("select", id="topic-filter")
        options = [opt["value"] for opt in select.find_all("option") if opt["value"]]
        assert options == sorted(options), "Dropdown options are not sorted alphabetically"

    def test_cards_have_data_domain_attribute(self, soup):
        """Every card must have a data-domain attribute for JS filtering."""
        cards = soup.find_all("a", class_="card")
        assert len(cards) > 0, "No cards found"
        missing = [card.find("h3").text for card in cards if not card.get("data-domain")]
        assert not missing, f"Cards missing data-domain: {missing}"

    def test_filter_count_element_exists(self, soup):
        """A count indicator must exist showing number of visible projects."""
        count_el = soup.find(id="filter-count")
        assert count_el is not None, "No element with id='filter-count' found"

    def test_filter_count_shows_total(self, soup):
        """Count element must show total number of projects."""
        count_el = soup.find(id="filter-count")
        cards = soup.find_all("a", class_="card")
        expected = f"{len(cards)} projects"
        assert count_el.text.strip() == expected, (
            f"Expected '{expected}', got '{count_el.text.strip()}'"
        )

    def test_filter_js_exists(self, soup):
        """A script block must exist that wires up the filter."""
        scripts = soup.find_all("script")
        filter_script = [s for s in scripts if s.string and "topic-filter" in s.string]
        assert len(filter_script) == 1, "Expected exactly one script referencing topic-filter"

    def test_no_duplicate_options(self, soup):
        """No duplicate values in the dropdown."""
        select = soup.find("select", id="topic-filter")
        values = [opt["value"] for opt in select.find_all("option") if opt["value"]]
        assert len(values) == len(set(values)), f"Duplicate options: {[v for v in values if values.count(v) > 1]}"

    def test_minimum_topic_count(self, soup):
        """There should be a reasonable number of topics (at least 10)."""
        select = soup.find("select", id="topic-filter")
        options = [opt for opt in select.find_all("option") if opt["value"]]
        assert len(options) >= 10, f"Only {len(options)} topics — expected at least 10"
