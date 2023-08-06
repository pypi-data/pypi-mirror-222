import requests
from dataclasses import dataclass, asdict
from enum import Enum
from typing import List, Dict, Any, Union

# Models
class EntityType(Enum):
    identity = "identity"
    nft = "nft"
    token = "token"

@dataclass
class Address:
    address: str
    description: str
    semantic_similarity: float
    network_value: float = 0.0
    rank: float = 0.0

@dataclass
class AddressMatch:
    address: str
    metadata: Dict[str, Any]

@dataclass
class Addresses:
    query: str
    matches: List[Address]

@dataclass
class DescribeInput:
    address: str
    blockchain: str

@dataclass
class DescribeOutput:
    matches: List[AddressMatch]

@dataclass
class Query:
    query: str
    blockchain: str
    entity_type: EntityType
    query_by: List[str]

    def to_dict(self):
        return {k: (v.value if isinstance(v, Enum) else v) for k, v in asdict(self).items()}

@dataclass
class ValidationError:
    loc: List[Union[str, int]]
    msg: str
    type: str

@dataclass
class HTTPValidationError:
    detail: List[ValidationError]

# Exception
class ApiException(Exception):
    def __init__(self, payload):
        self.payload = payload
        super().__init__(self.message)

    @property
    def message(self):
        return str(self.payload)

class OperatorSearchAPI:
    BASE_URL = 'https://api.operator.io/'

    def __init__(self, api_key: str):
        self.api_key = api_key

    def search(self, query: Query) -> Addresses:
        headers = {"X-API-Key": self.api_key}
        response = requests.post(
            self.BASE_URL + 'search/',
            headers=headers,
            json=query.to_dict()
        )
        
        if response.status_code == 200:
            data = response.json()
            return Addresses(query=data['query'], matches=[Address(**address) for address in data['matches']])
        elif response.status_code == 422:
            raise ApiException(HTTPValidationError(**response.json()))
        else:
            raise ApiException(response.json())

    def describe(self, describe_input: DescribeInput) -> DescribeOutput:
        headers = {"X-API-Key": self.api_key}
        response = requests.post(
            self.BASE_URL + 'describe/',
            headers=headers,
            json=asdict(describe_input)
        )

        if response.status_code == 200:
            data = response.json()
            return DescribeOutput(matches=[AddressMatch(**match) for match in data['matches']])
        elif response.status_code == 422:
            raise ApiException(HTTPValidationError(**response.json()))
        else:
            raise ApiException(response.json())
