import logging
from typing import Any, Dict, List, Optional

from pydantic import Extra, root_validator

from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM
from langchain.llms.utils import enforce_stop_tokens
from langchain.utils import get_from_dict_or_env

logger = logging.getLogger(__name__)


class Clarifai(LLM):
    """Clarifai large language models.

    To use, you should have an account on the Clarifai platform,
    the ``clarifai`` python package installed, and the
    environment variable ``CLARIFAI_PAT`` set with your PAT key,
    or pass it as a named parameter to the constructor.

    Example:
        .. code-block:: python

            from langchain.llms import Clarifai
            clarifai_llm = Clarifai(pat=CLARIFAI_PAT, \
                user_id=USER_ID, app_id=APP_ID, model_id=MODEL_ID)
    """

    stub: Any  #: :meta private:
    userDataObject: Any

    model_id: Optional[str] = None
    """Model id to use."""

    model_version_id: Optional[str] = None
    """Model version id to use."""

    app_id: Optional[str] = None
    """Clarifai application id to use."""

    user_id: Optional[str] = None
    """Clarifai user id to use."""

    pat: Optional[str] = None

    api_base: str = "https://api.clarifai.com"

    class Config:
        """Configuration for this pydantic object."""

        extra = Extra.forbid

    @root_validator()
    def validate_environment(cls, values: Dict) -> Dict:
        """Validate that we have all required info to access Clarifai
        platform and python package exists in environment."""
        values["pat"] = get_from_dict_or_env(values, "pat", "CLARIFAI_PAT")
        user_id = values.get("user_id")
        app_id = values.get("app_id")
        model_id = values.get("model_id")

        if values["pat"] is None:
            raise ValueError("Please provide a pat.")
        if user_id is None:
            raise ValueError("Please provide a user_id.")
        if app_id is None:
            raise ValueError("Please provide a app_id.")
        if model_id is None:
            raise ValueError("Please provide a model_id.")

        try:
            from clarifai.auth.helper import ClarifaiAuthHelper
            from clarifai.client import create_stub
        except ImportError:
            raise ImportError(
                "Could not import clarifai python package. "
                "Please install it with `pip install clarifai`."
            )
        auth = ClarifaiAuthHelper(
            user_id=user_id,
            app_id=app_id,
            pat=values["pat"],
            base=values["api_base"],
        )
        values["userDataObject"] = auth.get_user_app_id_proto()
        values["stub"] = create_stub(auth)

        return values

    @property
    def _default_params(self) -> Dict[str, Any]:
        """Get the default parameters for calling Clarifai API."""
        return {}

    @property
    def _identifying_params(self) -> Dict[str, Any]:
        """Get the identifying parameters."""
        return {
            **{
                "user_id": self.user_id,
                "app_id": self.app_id,
                "model_id": self.model_id,
            }
        }

    @property
    def _llm_type(self) -> str:
        """Return type of llm."""
        return "clarifai"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        """Call out to Clarfai's PostModelOutputs endpoint.

        Args:
            prompt: The prompt to pass into the model.
            stop: Optional list of stop words to use when generating.

        Returns:
            The string generated by the model.

        Example:
            .. code-block:: python

                response = clarifai_llm("Tell me a joke.")
        """

        try:
            from clarifai_grpc.grpc.api import (
                resources_pb2,
                service_pb2,
            )
            from clarifai_grpc.grpc.api.status import status_code_pb2
        except ImportError:
            raise ImportError(
                "Could not import clarifai python package. "
                "Please install it with `pip install clarifai`."
            )

        # The userDataObject is created in the overview and
        # is required when using a PAT
        # If version_id None, Defaults to the latest model version
        post_model_outputs_request = service_pb2.PostModelOutputsRequest(
            user_app_id=self.userDataObject,
            model_id=self.model_id,
            version_id=self.model_version_id,
            inputs=[
                resources_pb2.Input(
                    data=resources_pb2.Data(text=resources_pb2.Text(raw=prompt))
                )
            ],
        )
        post_model_outputs_response = self.stub.PostModelOutputs(
            post_model_outputs_request
        )

        if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
            logger.error(post_model_outputs_response.status)
            first_model_failure = (
                post_model_outputs_response.outputs[0].status
                if len(post_model_outputs_response.outputs[0])
                else None
            )
            raise Exception(
                f"Post model outputs failed, status: "
                f"{post_model_outputs_response.status}, first output failure: "
                f"{first_model_failure}"
            )

        text = post_model_outputs_response.outputs[0].data.text.raw

        # In order to make this consistent with other endpoints, we strip them.
        if stop is not None:
            text = enforce_stop_tokens(text, stop)
        return text
