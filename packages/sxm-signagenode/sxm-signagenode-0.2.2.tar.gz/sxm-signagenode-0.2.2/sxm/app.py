

from ebs.signagenode.app import SignageApplication
from .node import StarXMediaNode


class StarXMediaApplication(SignageApplication):
    _node_class = StarXMediaNode
