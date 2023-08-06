from simple_regex_generator.libs.select_regex import SelectRegex
from simple_regex_generator.libs.generator import Generator
from .create_regex_collections import ingest_definition
import json


__all__ = ["SelectRegex", "Generator"]


def generate_collections():
    file_path_config = "./simple_regex_generator/config/config.json"
    config = json.load(open(file_path_config, "r"))
    collections = ingest_definition()
    regex_types = config["regex_types_selected"]
    return (collections, regex_types)
