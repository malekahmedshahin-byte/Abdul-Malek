from .yarn import *
from .fabric import *
from .dyeing import *
from .costing import *
from .production import *
from .wastage import *
from .unit_conv import *
from .qc import *
# NEW INDUSTRY MODULES
from .spinning import *
from .weaving import *
from .dyeing_advanced import *
from .testing import *
from .costing_advanced import *

"""
TextileLabPro - Research Tools Module
This module provides:
- Citation generators (IEEE, APA, MLA, etc.)
- DOI-based automatic citation
- BibTeX exporter
"""

from .citation import (
    ieee_citation,
    apa_citation,
    mla_citation,
    harvard_citation,
    chicago_citation,
    fetch_doi_metadata,
    generate_citation_from_doi,
    export_bibtex
)


__all__ = [
    "ieee_citation",
    "apa_citation",
    "mla_citation",
    "harvard_citation",
    "chicago_citation",
    "fetch_doi_metadata",
    "generate_citation_from_doi",
    "export_bibtex"
]