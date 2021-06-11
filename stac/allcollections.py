#
# This file is part of Python Client Library for STAC.
# Copyright (C) 2019-2021 INPE.
#
# Python Client Library for STAC is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""STAC Collections module."""
import json

from pkg_resources import resource_string

from .catalog import Catalog
from .common import Provider
from .item import Item, ItemCollection
from .utils import Utils
from .collection import Collection

class AllCollections(list):
    """ The CCollections object."""
    
    def __init__(self, data):
        """Inicialize intance with list data.
        
        :param data: list with all collections metadata. 
        
        """
        super(AllCollections, self).__init__(data or [])

    def _repr_html_(self): # pragma: no cover
        """HTML repr."""
        return Utils.render_html('collections.html', allcollections = self)
