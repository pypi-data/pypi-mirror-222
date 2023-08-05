from typing import Any, List, Mapping, Optional

from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.embeddings.base import Embeddings
from langchain.llms.base import LLM
from langchain.vectorstores import Qdrant
from pydantic import BaseModel
import requests

from ..api.api_http import headers
from ..api.api_request import provision_req
from ..api.api_substation import SubstationAPI
from ..apps.vector import vector_store
from ..configuration import config
from ..util import unwrap


class SeaplaneEmbeddingFunction(BaseModel, Embeddings):
    
    url = config.substation_embed_endpoint
    req = provision_req(config._token_api)

    def _embed(self, query: str) -> List[float]:
        result = unwrap(
            self.req(
                lambda access_token: requests.post(
                    self.url,
                    json={"query": query},
                    headers=headers(access_token),
                )
            )
        )

        return result["embeddings"]

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        embeddings = []
        for text in texts:
            response = self._embed("Represent the Science document for Retrieval: " + text)
            embeddings.append(response)
        return embeddings

    def embed_query(self, query: str) -> List[float]:
        response = self._embed("Represent the Science sentence: " + query)
        return response


seaplane_embeddings = SeaplaneEmbeddingFunction()


def langchain_vectorstore(index_name: str, embeddings: Embeddings = seaplane_embeddings) -> Qdrant:
    vectorstore = Qdrant(
        client=vector_store._get_client(),
        collection_name=index_name,
        embeddings=embeddings,
    )

    return vectorstore


class SeaplaneLLM(LLM):

    substation_api = SubstationAPI(config)

    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
    ) -> str:
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")
        result = self.substation_api.predict(prompt, 5000)                
        return result["choices"][0]["text"]["generated_text"]

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"model": "MPT-30B", "provider": "Seaplane"}
