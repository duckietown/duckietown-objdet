# coding=utf-8

# add an import for each test file in this directory
from .test1 import *
from .test2 import *


def jobs_comptests(context):
    """ Hook for comptests. No need to modify."""
    from comptests.registrar import jobs_registrar_simple
    jobs_registrar_simple(context)
