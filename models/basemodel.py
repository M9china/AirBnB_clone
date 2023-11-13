#!/usr/bin/python3
"""These Defines the BaseModel class"""

import uuid
from datetime import datetime
import models


class BaseModel():
    """BaseModel CLass"""

    def __init__(self, *args, **kwargs):
        """
        Init method: initializing an instance

        Args:
            args: tuple arguments
            kwargs: keyworded arguments
        """
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            self.id = uuid.UUID(kwargs["id"])
            self.created_at = datetime.strptime(kwargs["created_at"],
                                                "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                "%Y-%m-%dT%H:%M:%S.%f")
            self.my_number = kwargs["my_number"]
            self.name = kwargs["name"]
        else:
            models.storage.new(self)

    def save(self):
        """
        Save method
            saves an instance
        """
        models.storage.save()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        String Method (MAGIC)
            returns a string representation
        """
        a = self.__dict__
        a["id"] = str(a["id"])
        return f"[{BaseModel.__name__}] ({str(self.id)}) {self.__dict__}"

    def to_dict(self):
        """
        to_dict method
            returns a dictionary represntation
        """
        a = self.__dict__
        a["created_at"] = a["created_at"].isoformat()
        a["updated_at"] = a["updated_at"].isoformat()
        a["id"] = str(a["id"])
        a["__class__"] = self.__class__.__name__
        return a
