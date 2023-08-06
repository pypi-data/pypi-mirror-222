# -*- coding: utf-8 -*-

"""
properties_step
A SEAMM plug-in for Properties
"""

# Bring up the classes so that they appear to be directly in
# the properties_step package.

from .properties import Properties  # noqa: F401, E501
from .properties_parameters import PropertiesParameters  # noqa: F401, E501
from .properties_step import PropertiesStep  # noqa: F401, E501
from .tk_properties import TkProperties  # noqa: F401, E501

from .metadata import metadata  # noqa: F401

# Handle versioneer
from ._version import get_versions

__author__ = "Paul Saxe"
__email__ = "psaxe@molssi.org"
versions = get_versions()
__version__ = versions["version"]
__git_revision__ = versions["full-revisionid"]
del get_versions, versions
