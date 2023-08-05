"""Eigen Ingenuity

Interface to the Eigen Ingenuity system.

Set the EIGENSERVER environment variable either to hostname, hostname:port
or http://hostname:port/prefix/path as appropriate. It defaults to
localhost:8080.

The various get_XXX methods instantiate connections to different parts
of the Eigen Ingenuity infrastructure.

Currently the only supported subsystem is historian.

h = get_historian("instancename")
h.listDataTags()
"""

from __future__ import (absolute_import, division, print_function, unicode_literals)
import pkg_resources
from eigeningenuity.core import EigenServer
from eigeningenuity.historian import get_historian, list_historians, get_default_historian_name
from eigeningenuity.elastic import get_elastic
from eigeningenuity.events import get_eventlog
from eigeningenuity.assetmodel import get_assetmodel
from eigeningenuity.smartdash import get_smartdash
from eigeningenuity.sql import get_sql
from eigeningenuity.settings import set_azure_client_id, set_azure_tenant_id, disable_azure_auth, disable_token_cache, clear_token_cache

__all__ = ["get_historian", "get_assetmodel", "get_elastic", "get_sql", "get_eventlog", "get_smartdash", "list_historians", "get_default_historian_name", "EigenServer", "set_azure_client_id", "set_azure_tenant_id", "disable_azure_auth", "disable_token_cache", "clear_token_cache"]
__version__ = pkg_resources.require("python-eigen-ingenuity")[0].version
