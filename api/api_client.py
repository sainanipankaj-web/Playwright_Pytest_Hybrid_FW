import requests
from utils.logger import get_logger


logger = get_logger()


class APIClient:

    def __init__(
            self,
            base_url=None,
            headers=None,
            auth_token=None
    ):

        self.base_url = base_url

        self.session = requests.Session()

        default_headers = {

            "Content-Type":
            "application/json"
        }

        if headers:

            default_headers.update(
                headers
            )

        self.session.headers.update(
            default_headers
        )

        if auth_token:

            self.set_bearer_token(
                auth_token
            )


    def set_bearer_token(
            self,
            token
    ):

        self.session.headers.update({

            "Authorization":
            f"Bearer {token}"
        })

        logger.info(
            "Bearer token added"
        )


    def add_headers(
            self,
            headers
    ):

        self.session.headers.update(
            headers
        )

        logger.info(
            f"Headers updated:{headers}"
        )


    def get(
            self,
            endpoint,
            params=None,
            **kwargs
    ):

        url = self._build_url(
            endpoint
        )

        logger.info(
            f"GET : {url}"
        )

        response = self.session.get(
            url,
            params=params,
            **kwargs
        )

        self._log_response(
            response
        )

        return response


    def post(
            self,
            endpoint,
            json=None,
            data=None,
            **kwargs
    ):

        url = self._build_url(
            endpoint
        )

        logger.info(
            f"POST : {url}"
        )

        response = self.session.post(

            url,

            json=json,

            data=data,

            **kwargs
        )

        self._log_response(
            response
        )

        return response


    def put(
            self,
            endpoint,
            json=None,
            **kwargs
    ):

        url = self._build_url(
            endpoint
        )

        response = self.session.put(
            url,
            json=json,
            **kwargs
        )

        self._log_response(
            response
        )

        return response


    def delete(
            self,
            endpoint,
            **kwargs
    ):

        url = self._build_url(
            endpoint
        )

        response = self.session.delete(
            url,
            **kwargs
        )

        self._log_response(
            response
        )

        return response


    def _build_url(
            self,
            endpoint
    ):

        if self.base_url:

            return (
                self.base_url +
                endpoint
            )

        return endpoint


    def _log_response(
            self,
            response
    ):

        logger.info(

            f"Status:"
            f"{response.status_code}"
        )

        logger.info(

            f"Response:"
            f"{response.text[:300]}"
        )


    def close(self):

        self.session.close()