# better_correct_fast/bcf_three.py
# -*- coding: utf-8 -*-

# A wrapper for the undocumented IfcOpenShell wrapper
# https://github.com/IfcOpenShell/IfcOpenShell/blob/v0.8.0/src/bcf/bcf/v3/bcfxml.py

# TODO does not work with snapshot yet. Snapshots are part of the viewport element with the name "snapshot.jpg". It will be included in the archive under the folder named after top_guid. It is supposed to be saved in the ViewPoint, under "Snapshot", then the text as "snapshot.jpg"

import bcf.v3.bcfxml as BCF # type: ignore

def create(title="BetterCorrectFast: Check this out!", description="Automatically generated topic by BetterCorrectFast", project_name=""): # TODO come up with a better alias # TODO come up with better placeholder values
    
    bcf = BCF.BcfXml().create_new(project_name)
    topic = _add_topic(bcf, title, description)

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

def save(bcf, filename):
    bcf.save(filename)
    # TODO add user output