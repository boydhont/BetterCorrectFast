# better_correct_fast/bcf_three.py
# -*- coding: utf-8 -*-

# A wrapper for the undocumented IfcOpenShell wrapper
# https://github.com/IfcOpenShell/IfcOpenShell/blob/v0.8.0/src/bcf/bcf/v3/bcfxml.py

# TODO does not work with snapshot yet. Snapshots are part of the viewport element with the name "snapshot.jpg". It will be included in the archive under the folder named after top_guid. It is supposed to be saved in the ViewPoint, under "Snapshot", then the text as "snapshot.jpg"
# TODO delete this icon.png later on

import bcf.v3.bcfxml as BCF # type: ignore

from pathlib import Path

def create(title="BetterCorrectFast: Check this out!", description="Automatically generated topic by BetterCorrectFast", project_name=""): # TODO come up with a better alias # TODO come up with better placeholder values
    
    bcf = BCF.BcfXml().create_new(project_name)
    topic = _add_topic(bcf, title, description)

    default_snapshot_path = _get_default_snapshot_path() 

    return bcf

def _add_topic(bcf, title, description, author="BetterCorrectFast", topic_type="Issue", topic_status="Open"): # TODO come up with better placeholder values

    topic = bcf.add_topic(
        title=title,
        description=description,
        author=author,
        topic_type=topic_type,
        topic_status=topic_status
    )

    return topic

def _get_default_snapshot_path():
    
    current_file = Path(__file__).resolve()
    snapshot_path = current_file.parent / 'assets' / 'icon.jpg'

    print(f"The default snapshot file is being used {'and is located' if snapshot_path.exists() else ', but was not found'} at: {snapshot_path}") # User feedback
    
    return snapshot_path

def save(bcf, filename):
    bcf.save(filename)
    # TODO add user output