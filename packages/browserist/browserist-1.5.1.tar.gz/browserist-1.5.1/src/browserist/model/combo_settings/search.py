from dataclasses import dataclass

from ... import helper
from ...model.type.xpath import XPath


@dataclass(kw_only=True, slots=True)
class SearchSettings:
    """Object with data needed to accept or decline cookies from a banner.

    input_xpath: XPath for the search input field.

    button_xpath: XPath for the search button.

    url: Optional URL for the search page.

    await_search_results_url_contains: Optional wait for the search results page URL to change.

    await_search_results_xpath: Optional wait for a search result element to be ready."""

    input_xpath: str
    button_xpath: str
    url: str | None = None
    await_search_results_url_contains: str | None = None
    await_search_results_xpath: str | None = None

    def __post_init__(self) -> None:
        self.input_xpath = XPath(self.input_xpath)
        self.button_xpath = XPath(self.button_xpath)
        self.url = helper.url.mediate_conversion_to_tiny_type_or_none(self.url)
        self.await_search_results_xpath = helper.xpath.mediate_conversion_to_tiny_type_or_none(
            self.await_search_results_xpath)
