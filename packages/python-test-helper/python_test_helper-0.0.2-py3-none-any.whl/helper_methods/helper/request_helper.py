from urllib.parse import urljoin, urlsplit

from requests import Session
from requests.exceptions import MissingSchema


def check_url_schema(scheme: str):
    if scheme in ["http", "https"]:
        return
    else:
        raise MissingSchema("Invalid URL, missing schema")


class RequestHelper(Session):
    def __init__(self, base_url: str, request_id: str = None):
        super().__init__()
        self.base_url = base_url.rstrip("/")  # Removing trailing slash, we'll add this on later
        self.verify = False
        self.headers['request-id'] = request_id

        split_url = urlsplit(base_url)

        check_url_schema(split_url.scheme)

    def request(self, method, url: str, *args, **kwargs):
        joined_url = urljoin(self.base_url + "/", url.lstrip("/"))
        return super().request(method, joined_url, *args, **kwargs)
