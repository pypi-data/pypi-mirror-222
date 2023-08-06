import os
import numpy as np
from PIL import Image

from readyocr.entities.entity_list import EntityList


class Invoice():
    """ 
    Creates a new document, ideally representing a single item in the dataset.
    
    :param id: Unique id of the Page
    :type id: str
    :param width: Width of page, in pixels
    :type width: float
    :param height: Height of page, in pixels
    :type height: float
    :param page_num: Page number in the document linked to this Page object
    :type page_num: int
    :param children: Child entities in the Page
    :type children: List
    """

    def __init__(
        self,
        id: str,
        width: int,
        height: int,
        page_num: int=-1,
        image: Image=None,
    ):
        super().__init__(width=width, height=height)
        self.id = id
        self.metadata = {}
        self.page_num = page_num
        self.image = image
        self._single_fields = EntityList()
        self._line_item_groups = EntityList()

    def __repr__(self):
        return os.linesep.join([
            f"Invoice(id: {self.id}, width: {self.width}, height: {self.height}, page_num: {self.page_num})",
        ])
    
    def export_json(self):
        return {
            "id": self.id,
            "pageNumber": self.page_num,
            "dimension": {
                "width": self.width,
                "height": self.height
            },
            "singleFields": [x.export_json() for x in self._single_fields],
            "lineItemGroups": [x.export_json() for x in self._line_item_groups],
        }