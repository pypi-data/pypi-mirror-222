from typing import Any, Callable, Dict, Optional, Tuple

import requests

from ...api.api_http import headers
from ...api.api_request import provision_req
from ...configuration import config
from ...logging import log
from ...model.errors import SeaplaneError
from ...util import unwrap
from ...api.api_substation import SubstationAPI

SEAPLANE_API_KEY_NAME = "SEAPLANE_API_KEY"


def _check_seaplane_api_key() -> None:
    if config.seaplane_api_key is None:
        raise SeaplaneError(
            f"Seaplane API Key `{SEAPLANE_API_KEY_NAME}` is not set,\
                  use `sea.config.set_api_key`."
        )

substation = SubstationAPI(config)

def bloom() -> Callable[[Dict[str, Any]], Any]:
    def model(input: Dict[str, Any]) -> Any:        
        return substation.predict(input["prompt"], input["max_output_length"])

    return model


class Bloom:
    def __init__(self, func: Callable[[Any], Any], id: str, model: Optional[str]) -> None:
        self.func = func
        self.args: Optional[Tuple[Any, ...]] = None
        self.kwargs: Optional[Dict[str, Any]] = None
        self.type = "inference"
        self.model = model
        self.id = id

    def process(self, *args: Any, **kwargs: Any) -> Any:
        self.args = args
        self.kwargs = kwargs

        if self.model == "MPT-30B":
            log.info("Processing MPT-30B Model...")
            self.args = self.args + (bloom(),)

            return self.func(*self.args, **self.kwargs)

    def print(self) -> None:
        log.info(f"id: {self.id}, type: {self.type}, model: {self.model}")
