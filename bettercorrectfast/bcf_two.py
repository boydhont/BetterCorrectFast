# better_correct_fast/bcf_two.py
# -*- coding: utf-8 -*-

# A wrapper for the undocumented IfcOpenShell wrapper
# https://github.com/IfcOpenShell/IfcOpenShell/blob/v0.8.0/src/bcf/bcf/v3/bcfxml.py

# TODO does not work with snapshot yet. Snapshots are part of the viewport element with the name "snapshot.jpg". It will be included in the archive under the folder named after top_guid. It is supposed to be saved in the ViewPoint, under "Snapshot", then the text as "snapshot.jpg"
# TODO delete this icon.png later on

import uuid

import bcf.v2.bcfxml as BCF # type: ignore
import bcf.v2.topic as TOPIC # type: ignore
import bcf.v2.visinfo as VIS # type:ignore
import bcf.v2.model as MDL # type: ignore

from pathlib import Path

def create(title="BetterCorrectFast: Check this out!", description="Automatically generated topic by BetterCorrectFast", image_filepath=None, project_name=""): # TODO come up with a better alias # TODO come up with better placeholder values
    
    # Create the elements
    bcf = BCF.BcfXml().create_new(project_name)
    topic = _get_topic(title, description, image_filepath)
    
    # Add the elements
    bcf.topics[topic.guid] = topic

    return bcf

def _get_topic(title, description, image_filepath, author="BetterCorrectFast", topic_type="Issue", topic_status="Open"): # TODO come up with better placeholder values

    # Create the elements
    topic = TOPIC.TopicHandler().create_new(
        title=title,
        description=description,
        author=author,
        topic_type=topic_type,
        topic_status=topic_status
    )

    visualization_info_handler = _get_visualization_info_handler(image_filepath) # TODO insert the image filepath here # TODO add user input for the picture
    
    # Add the elements
    topic.add_visinfo_handler(visualization_info_handler, snapshot_filename="snapshot.png")
 
    return topic

def _get_visualization_info_handler(image_filepath):
    
    visualization_info = _get_visualization_info()
    
    image_filepath = image_filepath if image_filepath is not None else _get_default_snapshot_path()
    image_bytes = _get_image_bytes_from_filepath(image_filepath)

    visualization_info_handler = VIS.VisualizationInfoHandler(visualization_info, snapshot=image_bytes )
    
    return visualization_info_handler

def _get_image_bytes_from_filepath(filepath):
    try:
        with open(filepath, "rb") as image_file:
            return image_file.read()
    except:
        return None # TODO check if return None is ok to begin with

def _get_visualization_info():
    
    visualization_info = MDL.VisualizationInfo(
        guid=str(uuid.uuid4()),  # Generate a random GUID
    )
    
    return visualization_info

def _get_default_snapshot_path(): # TODO might be unsafe if the filepath does not exits
    
    current_file = Path(__file__).resolve()
    snapshot_path = current_file.parent / 'assets' / 'icon.png'

    snapshot_path_exists = snapshot_path.exists()
    print(f"The default snapshot file is being used {'and is located' if snapshot_path_exists else ', but was not found'} at: {snapshot_path}") # User feedback
    
    if not snapshot_path_exists: return None
    return str(snapshot_path)
