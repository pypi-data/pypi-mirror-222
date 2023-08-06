import copy
import pprint
import typing

from ..internals.api import _api_session
from ..internals import project, api, errors
from ..stream.stream import Stream


class Dataset:
    @project._check_flockfysh_dir
    @_api_session._authorization_check
    def __init__(self, dataset_id):
        self.__dataset_id = dataset_id

        result = _api_session.get(f"/api/datasets/stats/{dataset_id}", data={
            "expand": "assetCounts",
        }).json()

        if not result["success"]:
            error_code = result["error"]["code"]
            if error_code == "ERROR_NOT_FOUND":
                raise errors.NotFoundException("Dataset not found.")
            else:
                raise RuntimeError("There is a problem fetching datasets")
        self.__dataset_info = result["data"]

    @property
    def info(self):
        return copy.deepcopy(self.__dataset_info)

    @property
    def dataset_id(self):
        return self.__dataset_id
    
    @property
    def length(self):
        return self.__dataset_info["assetCounts"]["total"]

    def create_stream(self, *, asset_stage: typing.Literal["completed", "uploaded", "feedback"] = None,
                      asset_filename_search: str = None):
        return Stream._create(self.__dataset_id, copy.deepcopy(self.__dataset_info), asset_stage=asset_stage,
                              asset_filename_search=asset_filename_search)
