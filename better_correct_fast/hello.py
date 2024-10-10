# better_correct_fast/hello.py
# -*- coding: utf-8 -*-

# TODO simple test module to see if the package works to begin with, delete this hello.py later

import bcf.v3.bcfxml as BCF # type: ignore

def say_hello():
    print("Hello, World!")
    bcf = BCF.BcfXml()
    print(bcf)