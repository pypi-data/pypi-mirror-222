from commmons import html_from_url
from lxml import html
from pydash import head

from hypersquirrel.core import Watchlist


def get_url_and_filename(root, fileid):
    atag = root.xpath(f"//div[@data-video-id='{fileid}']/div/a")[0]
    url = atag.attrib["href"]
    return url, atag.text


def get_divs_with_fileid(root):
    divs = root.xpath("//div[contains(@class, 'video-thumb')]")
    for div in divs:
        fileid = div.attrib.get("data-video-id")
        if fileid:
            yield div


def _scrape(root):
    for div in get_divs_with_fileid(root):
        fileid = div.attrib.get("data-video-id")
        sourceurl, filename = get_url_and_filename(div, fileid)
        thumbnailurl = div.xpath(".//img")[0].attrib["src"]
        yield {
            "fileid": f"xh{fileid}",
            "sourceurl": sourceurl,
            "filename": filename,
            "thumbnailurl": thumbnailurl
        }


def scrape(url):
    root = html_from_url(url)
    yield from _scrape(root)


def scrape_html(html_string: str):
    root = html.fromstring(html_string)
    yield from _scrape(root)


def is_xh_html(w: Watchlist):
    if w.html:
        tree = html.fromstring(w.html)
        title = head(tree.xpath("//head/title"))

        if title is not None and "xHamster" in title.text:
            return True

    return False
