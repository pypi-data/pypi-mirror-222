# pylint: disable=too-many-instance-attributes

"""dataset module"""

from dataclasses import dataclass

from matatika import Resource


@dataclass
class Dataset(Resource):
    """Class for dataset objects"""

    dataset_id: str = None
    alias: str = None
    workspace_id: str = None
    source: str = None
    title: str = None
    description: str = None
    questions: str = None
    raw_data: str = None
    visualisation: str = None
    metadata: str = None
    query: str = None
    version: str = None

    attr_translations = {
        "id": "dataset_id",
        "workspaceId": "workspace_id",
        "rawData": "raw_data",
    }

    @classmethod
    def from_dict(cls, resource_dict: dict):
        dataset = super().from_dict(resource_dict)

        dataset.dataset_id = resource_dict.get("id")
        dataset.alias = resource_dict.get("alias")
        dataset.workspace_id = resource_dict.get("workspaceId")
        dataset.source = resource_dict.get("source")
        dataset.title = resource_dict.get("title")
        dataset.description = resource_dict.get("description")
        dataset.questions = resource_dict.get("questions")
        dataset.raw_data = resource_dict.get("rawData")
        dataset.visualisation = resource_dict.get("visualisation")
        dataset.metadata = resource_dict.get("metadata")
        dataset.query = resource_dict.get("query")

        return dataset


@dataclass
class DatasetV0_1(Dataset):  # pylint: disable=invalid-name
    """Class for dataset resource version 0.1"""

    version: str = "datasets/v0.1"


@dataclass
class DatasetV0_2(Dataset):  # pylint: disable=invalid-name
    """Class for dataset resource version 0.2"""

    version: str = "datasets/v0.2"
