# https://pole-emploi.io/data/api/rome?tabgroup-api=documentation&doc-section=api-doc-section-caracteristiques
from ...base import Api as BaseApi
import requests


class ApiMetier(BaseApi):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # params
        self.url = kwargs.get(
            "url", "https://api.pole-emploi.io/partenaire/rome-metiers/v1/metiers"
        )

    def scope(self) -> str:
        return "api_rome-metiersv1 nomenclatureRome"

    def _get(self, url: str, kwargs: dict):
        # headers
        headers = kwargs.pop("headers", {})
        headers = self._get_auth_header(headers)

        # params
        params = [(k, kwargs[k]) for k in kwargs.keys()]

        return requests.get(url, params=params, headers=headers)

    def theme(self, **kwargs):
        url = self.url + "/theme"

        code: str = kwargs.pop("code", None)
        if code:
            url += f"/{code.upper()}"

        return self._get(url, kwargs)

    def metier(self, **kwargs):
        url = self.url + "/metier"
        code: str = kwargs.pop("code", None)
        if code:
            url += f"/{code.upper()}"
        return self._get(url, kwargs)

    def granddomain(self, **kwargs):
        url = self.url + "/grand-domaine"
        code: str = kwargs.pop("code", None)
        if code:
            url += f"/{code.upper()}"
        return self._get(url, kwargs)

    def domaineprofessionnel(self, **kwargs):
        url = self.url + "/domaine-professionnel"
        code: str = kwargs.pop("code", None)
        if code:
            url += f"/{code.upper()}"
        return self._get(url, kwargs)

    def appellation(self, **kwargs):
        url = self.url + "/appellation"
        code: int = kwargs.pop("code", None)
        query = kwargs.get("q")
        if code:
            url += f"/{code}"
        elif query:
            url += "/requete"

        return self._get(url, kwargs)
