#!/usr/bin/python3
"""file storage"""

import json
from models.basemodel import BaseModel


class FileStorage:
    """FileStorage Class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        all method
            returns the class attribute __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        new method
            adds an instance of a class to the class attribute __objects
        """
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """
        save method:
            saves to a json file
        """
        json_obj = FileStorage.__objects
        json_obj_data = {json_key: json_obj[json_key].to_dict()
                         for json_key in json_obj.keys()}
        json_obj_data_to_json = json.dumps(json_obj_data)
        with open(FileStorage.__file_path, "w") as json_file:
            json_file.write(json_obj_data_to_json)

    def reload(self):
        """
        reload method
            reload data from a json file
        """
        try:
            with open(FileStorage.__file_path, "r") as json_file:
                py_dict = json.load(json_file)
                for val in py_dict.values():
                    cls_name = val["__class__"]
                    #self.new(eval((cls_name)(**val)))
                    if cls_name == "BaseModel":
                        #self.new(eval(BaseModel(**val)))
                        self.new(BaseModel(**val))
        except FileNotFoundError:
            return
