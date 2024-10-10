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

def create(title="BetterCorrectFast: Check this out!", description="Automatically generated topic by BetterCorrectFast", project_name=""): # TODO come up with a better alias # TODO come up with better placeholder values
    
    # Create the elements
    bcf = BCF.BcfXml().create_new(project_name)
    topic = _get_topic(title, description)
    
    # Add the elements
    bcf.topics[topic.guid] = topic

    return bcf

def _get_topic(title, description, author="BetterCorrectFast", topic_type="Issue", topic_status="Open"): # TODO come up with better placeholder values

    # Create the elements
    topic = TOPIC.TopicHandler().create_new(
        title=title,
        description=description,
        author=author,
        topic_type=topic_type,
        topic_status=topic_status
    )

    visualization_info_handler = _get_visualization_info_handler() # TODO activate # TODO add user input for the picture
    
    # Add the elements
    topic.add_visinfo_handler(visualization_info_handler, snapshot_filename="snapshot.png") # TODO activate # TODO make the filename dynamic # TODO just type the stuf that is in there
 
    return topic

def _get_visualization_info_handler(): # A Viewpoint is called VisualizationInfoHandler in IfcOpenShell for some reason
    # TODO get the snapshot etc
    # Create elements
    
    
    image_bytes = _get_image_bytes_from_filepath(_get_default_snapshot_path()) #TODO debug, do this clean
    
    visualization_info = _get_visualization_info()
    
    visualization_info_handler = VIS.VisualizationInfoHandler(visualization_info, snapshot=image_bytes ) # TODO add the snapshot?
    # TODO add the visualizationinfo and add it to the viewpoint
    
    
    return visualization_info_handler

def _get_image_bytes_from_filepath(filepath):
    with open(filepath, "rb") as image_file:
        return image_file.read()

def _get_visualization_info(): # TODO add the bitmaps dynamically
    
    visualization_info = MDL.VisualizationInfo(
        guid=str(uuid.uuid4()),  # Generate a random GUID
    )
    
    return visualization_info

def _get_visualization_bitmap_from_filepath(filepath): # TODO add support for more filetypes than .jpg
    
    bitmap = MDL.VisualizationInfoBitmap(
        bitmap=MDL.BitmapFormat.PNG, # TODO add suppor for more formats
        reference=filepath,
        location=MDL.Point(x=0.0, y=0.0, z=0.0),  # Set your actual location here
        normal=MDL.Direction(x=0.0, y=0.0, z=1.0),  # Set your actual normal here
        up=MDL.Direction(x=0.0, y=1.0, z=0.0),  # Set your actual up vector here
        height=1080.0,  # TODO Set your actual height here
    )
    
    return bitmap

def _get_default_snapshot_path(): # TODO change to icon
    
    current_file = Path(__file__).resolve()
    snapshot_path = current_file.parent / 'assets' / 'icon.png'

    print(f"The default snapshot file is being used {'and is located' if snapshot_path.exists() else ', but was not found'} at: {snapshot_path}") # User feedback
    
    return str(snapshot_path)

def save(bcf, filename):
    bcf.save(filename)
    # TODO add user output