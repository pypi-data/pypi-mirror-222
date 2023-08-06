from typing import List

import requests

from ..configuration import Configuration, config
from ..util import unwrap
from .api_http import headers
from .api_request import provision_req
import json

class SubstationAPI:
    """
    Class for handle Substation API calls.
    """

    def __init__(self, configuration: Configuration = config) -> None:
        self.url = f"{configuration.substation_endpoint}/completions"        
        self.req = provision_req(configuration._token_api)

    def predict(self, prompt: str, max_output_length: int = 300) -> str:
        result = unwrap(
            self.req(
                lambda access_token: requests.post(
                    self.url,
                    headers=headers(access_token),
                    json={"max_tokens": max_output_length, "prompt": prompt},
                )
            )
        )

        if type(result) is str: # Substation FIX, It needs to returns content-type: application/json       
          return json.loads(result) 
        else:
          return result
