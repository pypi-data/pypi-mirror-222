"""Root GraphQL Class
"""

from pydantic import root_validator, ConfigDict, BaseModel
from humps.camel import case


class GraphQlBase(BaseModel):
    """Root Graph QL Class"""
    model_config = ConfigDict(alias_generator=case,
                              populate_by_name=True, extra="forbid")

    @root_validator(pre=True)
    def unwap_nodes(cls, data: dict):  # pylint: disable=no-self-argument
        """Unwraps <object>.nodes.<items> to <object>.<items>

        Args:
            data (dict): The to be validated input data

        Returns:
            dict: The valiated and transformed input data
        """
        for key, value in data.items():
            if isinstance(value, dict) and 'nodes' in value:
                data[key] = value['nodes']

        return data
