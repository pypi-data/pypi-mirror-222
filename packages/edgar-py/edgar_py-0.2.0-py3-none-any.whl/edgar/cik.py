"""
"""

import datetime
import re
import typing

import bs4
import pandas as pd
import requests


class CIKLookup:
    """
    API wrapper for the SEC `CIK Lookup`_ tool.

    .. py:attribute:: address

        The URL address of the CIK Lookup tool.

        :type: str
        :value: https://www.sec.gov/cgi-bin/cik_lookup

    :param name: The company name (i.e., the search term)

    .. CIK Lookup: https://www.sec.gov/cgi-bin/cik_lookup
    """
    address = "https://www.sec.gov/cgi-bin/cik_lookup"

    def __init__(self, name: str):
        self.name = name

        with requests.post(
            self.address, data={"company": self.name}, timeout=100
        ) as response:
            self._soup = bs4.BeautifulSoup(response.text, features="lxml")

    @property
    def count(self) -> int:
        """
        The number of search results returned by the CIK Lookup tool.
        """
        element = self._soup.select_one("table tr > td:last-child > p")

        return int(re.search(r"\d+", element.text).group())

    @property
    def truncated(self) -> bool:
        """
        Whether the search results returned by the CIK Lookup tool were truncated.

            The search will return as many as 100 records that match your keyword(s), but after
            that it will truncate (cut off) the list. If this happens, it means that you need to be
            more specific.
        """
        element = self._soup.select_one("table tr > td:last-child > p")

        return "truncated" in element.text

    @property
    def results(self) -> pd.DataFrame:
        """
        The search results returned by the CIK Lookup tool.
        """
        if self.count == 0:
            return pd.DataFrame({})
        element = self._soup.select_one("table > tr > td:last-child > pre:last-of-type")

        data = [[y.strip() for y in x.split(maxsplit=1)] for x in element.text.split("\n") if x]
        cik_code, company_name = zip(*data)
        href = [f"https://sec.gov/{e.attrs['href']}" for e in element.select("a")]

        return pd.DataFrame(
            {"CIK Company": cik_code, "Company Name": company_name, "URL": href}
        )

    @property
    def timestamp(self) -> datetime.datetime:
        """
        The timestamp of the search query submitted to the CIK Lookup tool.
        """
        element = self._soup.select_one("table > tr > td:last-child > p:last-of-type")

        return datetime.datetime.strptime(
            element.text.strip(), "Generated at %H:%M:%S EDT on %B %d, %Y"
        )


class CompanyDatabaseSearch:
    """
    API wrapper for the EDGAR `Company Database Search`_ tool.

    .. py:attribute:: address

        The URL address of the EDGAR Company Database Search tool.

        :type: str
        :value: "https://www.edgarcompany.sec.gov/servlet/CompanyDBSearch"

    .. py:attribute:: search_keys

        :type: list[str]

    :param kwargs:

    .. _Company Database Search: https://www.edgarcompany.sec.gov/servlet/CompanyDBSearch
    """
    address = "https://www.edgarcompany.sec.gov/servlet/CompanyDBSearch"

    search_keys = [
        "cik", "company_name", "reporting_file_number", "series_id", "series_name",
        "class_contract_id", "class_contract_name", "state_country", "city", "state_incorporation",
        "zip_code", "last_update_from", "last_update_to"
    ]

    def __init__(self, **kwargs: str):
        self.search_parameters = {}
        for key in self.search_keys:
            self.__setattr__(key, kwargs[key] if key in kwargs else "")

    @classmethod
    def company_information(cls, cik: str) -> typing.Dict[str, typing.Any]:
        """
        Scrapes the Detailed Company Information page for a company specified by its Central Index
        Key (CIK).

        :param cik: A Central Index Key (CIK)
        :return: Dictionary of the detailed company information
        """
        params = {"page": "detailed", "cik": cik, "main_back": 1}
        with requests.get(cls.address, params=params, timeout=100) as response:
            soup = bs4.BeautifulSoup(response.text, features="lxml")

        rows = soup.select(
            "form > table > tr:nth-child(3) > td > table > tr:nth-child(2) > td > table > tr"
        )[1:]
        data = dict(
            zip(
                [r.select_one("td:nth-child(2)").text.strip().strip(":") for r in rows],
                [r.select_one("td:nth-child(3)").text.strip() for r in rows]
            )
        )

        data["Fiscal Year End"] = datetime.datetime.strptime(
            data["Fiscal Year End"], "%m%d"
        )
        data["Date of Last Update"] = datetime.datetime.strptime(
            data["Date of Last Update"], "%Y-%m-%d %H:%M:%S.%f"
        )

        return data

    @classmethod
    def last_update(cls) -> datetime.datetime:
        """
        :return: The timestamp of the last update of the EDGAR Company Database
        """
        with requests.get(cls.address, params={"page": "main"}, timeout=100) as response:
            soup = bs4.BeautifulSoup(response.text, features="lxml")

        element = soup.select_one("table > tr:nth-child(3) > td > span")
        regex = re.compile(r"The company database was last updated on (.*)\.")

        return datetime.datetime.strptime(
            regex.search(element.text).group(1), "%m/%d/%y at %I/%M %p EDT"
        )

    @classmethod
    def country_options(cls) -> typing.Dict[str, str]:
        """
        Scrapes valid state/country codes that the :py:attr:`CompanyDatabaseSearch.state_country`
        and :py:attr:`CompanyDatabaseSearch.state_incorporation` properties can assume. Each
        state/country code is mapped to the name of the state/country it represents.

        .. note::

            Keys with corresponding values followed by an asterisk represent country names that are
            no longer in use. These keys may still be selected if the company being searched still
            has a business country equal to one of them.

        :return: Dictionary of state/country codes mapped to their corresponding state/country name
        """
        with requests.get(cls.address, params={"page": "main"}, timeout=100) as response:
            soup = bs4.BeautifulSoup(response.text, features="lxml")

        element = soup.select_one("select[name='state_country']")
        return {e.attrs["value"]: e.text.strip() for e in element.select("option")}

    @property
    def cik(self) -> str:
        """
        A company Central Index Key (CIK).

        .. note::

            Leading zeros are not required as they will automatically be added if the specified CIK
            is less than 10 digits. Any search containing a CIK will return at most one result. 
        """
        return self.search_parameters["cik"]

    @cik.setter
    def cik(self, value: str) -> None:
        regex = re.compile(r"^\d{,10}$")
        self.search_parameters["cik"] = value if regex.search(value) else ""

    @property
    def company_name(self) -> str:
        """
        A company name.

        .. note::

            This can either be a company name or the beginning of a company name. Companies having
            a name equal to or beginning with the specified will be returned. 
        """
        return self.search_parameters["company_name"]

    @company_name.setter
    def company_name(self, value: str) -> None:
        self.search_parameters["company_name"] = value.upper()

    @property
    def reporting_file_number(self) -> str:
        r"""
        A company reporting file name. A reporting file number should adhere to the regular
        expression ``(\d{3}-\d{5}|\d{3}-\d{5}-\d{2})``.

        .. note::

            This can either be a reporting file number or the beginning of a reporting file number.
            Companies having a reporting file number equal to or beginning with the specified value
            will be returned. 
        """
        return self.search_parameters["reporting_file_number"]

    @reporting_file_number.setter
    def reporting_file_number(self, value: str) -> None:
        regex = re.compile(r"^(\d{,3}|\d{3}-\d{,5}|\d{3}-\d{5}-\d{,2})$")
        self.search_parameters["reporting_file_number"] = value if regex.search(value) else ""

    @property
    def series_id(self) -> str:
        r"""
        A company series identifier. A series identifier should adhere to the regular expression
        ``S\d{9}``.

        .. note::

            This can either be a series identifier or the beginning of a series identifier. Series
            identifier having a name equal to or beginning with the specified value will be
            returned. The series identifier needs to start with S. 
        """
        return self.search_parameters["series_id"]

    @series_id.setter
    def series_id(self, value: str) -> None:
        regex = re.compile(r"^S\d{,9}$")
        self.search_parameters["series_id"] = value if regex.search(value) else ""

    @property
    def series_name(self) -> str:
        """
        A series name.

        .. note::

            This can be a series name or the beginning of a series name. Series having a name equal
            to or beginning with the specified value will be returned. 
        """
        return self.search_parameters["series_name"]

    @series_name.setter
    def series_name(self, value: str) -> None:
        self.search_parameters["series_name"] = value.upper()

    @property
    def class_contract_id(self) -> str:
        r"""
        A company class identifier. A class identifier should adhere to the regular expression
        ``C\d{9}``.

        .. note::

            This can either be a class identifier or the beginning of a class identifier. Class
            identifier having a name equal to or beginning with the specified value will be
            returned. The class identifier needs to start with C.
        """
        return self.search_parameters["class_contract_id"]

    @class_contract_id.setter
    def class_contract_id(self, value: str) -> None:
        regex = re.compile(r"^C\d{,9}$")
        self.search_parameters["class_contract_id"] = value if regex.search(value) else ""

    @property
    def class_contract_name(self) -> str:
        """
        A class (contract) name.

        .. note::

            This can be a class (contract) name or the beginning of a class (contact) name. Classes
            (Contracts) having a name equal or beginning with the specified value will be returned. 
        """
        return self.search_parameters["class_contract_name"]

    @class_contract_name.setter
    def class_contract_name(self, value: str) -> None:
        self.search_parameters["class_contract_name"] = value.upper()

    @property
    def state_country(self) -> str:
        """
        The business state/country of a company.

        .. note::
        
            See :py:meth:`CompanyDatabaseSearch.country_options` for valid values this property can
            assume.
        """
        return self.search_parameters["state_country"]

    @state_country.setter
    def state_country(self, value: str) -> None:
        options = self.country_options()
        self.search_parameters["state_country"] = value if value in options else "NONE"

    @property
    def city(self) -> str:
        """
        The business city of a company.

        .. note::

            This can either be a city name or the beginning of a city name. Companies having a city
            name equal to or beginning with the specified value will be returned.

        """
        return self.search_parameters["city"]

    @city.setter
    def city(self, value: str) -> None:
        self.search_parameters["city"] = value.upper()

    @property
    def state_incorporation(self) -> str:
        """
        The state of incorporation of a company.

        .. note::
        
            See :py:meth:`CompanyDatabaseSearch.country_options` for valid values this property can
            assume.
        """
        return self.search_parameters["state_incorporation"]

    @state_incorporation.setter
    def state_incorporation(self, value: str) -> None:
        options = self.country_options()
        self.search_parameters["state_incorporation"] = value if value in options else "NONE"

    @property
    def zip_code(self) -> str:
        """
        The ZIP code of a company.

        .. note::

            This can either be a ZIP code or the beginning of a ZIP code. Companies having a ZIP
            code equal to or beginning with the specified value will be returned. 
        """
        return self.search_parameters["zip_code"]

    @zip_code.setter
    def zip_code(self, value: str) -> None:
        regex = re.compile(r"^(\d{,5}|\d{5}-\d{,4})$")
        self.search_parameters["zip_code"] = value if regex.search(value) else ""

    @property
    def last_update_from(self) -> str:
        """
        The start of a date range during which a company had company updates.

        .. note::

            If only a _from_ date is set, companies that have had company updates since the
            specified date will be returned. If both a _from_ date and a _to_ date
            (:py:attr:`CompanyDatabaseSearch.last_update_to`) are set, companies that have had
            company updates between the specified dates will be returned.
        """
        return self.search_parameters["last_update_from"]

    @last_update_from.setter
    def last_update_from(self, value: typing.Optional[datetime.datetime]) -> None:
        try:
            self.search_parameters["last_update_from"] = value.strftime("%m/%d/%y")
        except (AttributeError, ValueError):
            self.search_parameters["last_update_from"] = ""

    @property
    def last_update_to(self) -> str:
        """
        The end of a date range during which a company had company updates.

        .. note::

            If only a _to_ date is set, companies that have had company updates before the
            specified date will be returned. If both a _from_ date
            (:py:attr:`CompanyDatabaseSearch.last_update_from`) and a _to_ date are set, companies
            that have had company updates between the specified dates will be returned.
        """
        return self.search_parameters["last_update_to"]

    @last_update_to.setter
    def last_update_to(self, value: datetime.datetime) -> None:
        try:
            self.search_parameters["last_update_to"] = value.strftime("%m/%d/%y")
        except (AttributeError, ValueError):
            self.search_parameters["last_update_to"] = ""

    @property
    def count(self) -> int:
        """
        The number of search results returned by the Company Database Search tool.
        """
        params = {
            "start_row": -1, "end_row": -1, "main_back": 0, **self.search_parameters,
            "page": "count", "submit_button": "Submit"
        }
        with requests.get(self.address, params=params, timeout=100) as response:
            soup = bs4.BeautifulSoup(response.text, features="lxml")

        element = soup.select_one(
            "table > tr:nth-child(3) > td > table > tr:nth-child(1) > td > table > tr > td"
        )
        try:
            return int(re.search(r"^\d+", element.text).group())
        except AttributeError:
            return 0

    @property
    def results(self) -> pd.DataFrame:
        """
        The search results returned by the Company Database Search tool.
        """
        dataframes = []

        params = {
            "start_row": -1, "end_row": -1, "main_back": 0, **self.search_parameters,
            "page": "summary", "submit_button": "Submit"
        }

        for npage in range(self.count // 10 + 1):
            with requests.get(self.address, params=params, timeout=100) as response:
                dataframes.append(
                    self._scrape_page(bs4.BeautifulSoup(response.text, features="lxml"))
                )

            params["submit_button"] = "Next >>"
            params["end_row"] = (npage + 1) * 10
            params["start_row"] = params["end_row"] - 9

        return pd.concat(dataframes).reset_index(drop=True)

    def _scrape_page(self, soup: bs4.BeautifulSoup) -> pd.DataFrame:
        """
        Scrapes the entries on a page of results returned by the Company Database Search tool.

        :param soup: The parsed HTML of a page of results
        :return: DataFrame of the entries of the results.
        """
        columns = [
            "Company Name", "URL", "CIK", "State of Incorporation", "Date of Last Update",
            "Regulated Entity Type"
        ]
        dataframe = pd.DataFrame(columns=columns)

        rows = soup.select("form#the_form > table > tr:nth-child(3) > td > table > tr")[2:-1]
        for idx, row in enumerate(rows):
            href = row.select_one("table > tr:nth-last-child(4) > td > a")

            cik = re.search(
                r"^CIK:\s+(\d{10})?$",
                row.select_one("table > tr:nth-last-child(3) > td:nth-child(3)").text
            ).group(1)
            state_incorporation = re.search(
                r"^State of Incorporation:\s+(.*)$",
                row.select_one("table > tr:nth-last-child(3) > td:nth-child(4)").text
            ).group(1)
            last_update = re.search(
                r"^Date of Last Update:\s+(\d{2}/\d{2}/\d{2})?$",
                row.select_one("table > tr:nth-last-child(2) > td:nth-child(3)").text
            ).group(1)
            entity_type = re.search(
                r"^Regulated Entity Type:\s+(.*)$",
                row.select_one("table > tr:nth-last-child(2) > td:nth-child(4)").text
            ).group(1)

            dataframe.loc[idx, :] = [
                " ".join(href.text.split()),
                f"https://edgarcompany.sec.gov{href.attrs['href']}",
                cik,
                state_incorporation,
                datetime.datetime.strptime(last_update, "%m/%d/%y") if last_update else "",
                entity_type
            ]

        return dataframe
