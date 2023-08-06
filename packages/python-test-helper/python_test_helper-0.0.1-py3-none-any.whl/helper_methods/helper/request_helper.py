from urllib.parse import urljoin

from requests import Session
from requests.exceptions import MissingSchema


def check_url_schema(base_url: str):
    # Regex? ^(http|https)://
    if base_url.startswith("http://") or base_url.startswith("https://"):
        return
    else:
        raise MissingSchema("Invalid URL, missing schema")


class RequestHelper(Session):
    def __init__(self, base_url: str, request_id: str = None):
        super().__init__()
        self.base_url = base_url
        self.verify = False
        self.headers['request-id'] = request_id

        check_url_schema(base_url)

    def request(self, method, url, *args, **kwargs):
        joined_url = urljoin(self.base_url, url)
        return super().request(method, joined_url, *args, **kwargs)
