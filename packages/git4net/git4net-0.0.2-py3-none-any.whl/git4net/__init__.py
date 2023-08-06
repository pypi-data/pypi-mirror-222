"""
An OpenSource Python package for the extraction of fine-grained
and time-stamped co-editing networks from git repositories.
"""

from pkg_resources import get_distribution

__author__ = "Christoph Gote"
__email__ = "cgote@ethz.ch"
__version__ = get_distribution('git4net').version

from .extraction import mine_git_repo
from .extraction import mine_github
from .extraction import get_unified_changes
from .extraction import get_commit_dag
from .extraction import identify_file_renaming
from .extraction import text_entropy
from .extraction import mining_state_summary
from .extraction import check_mining_complete
from .disambiguation import disambiguate_aliases_db
from .visualisation import get_line_editing_paths
from .visualisation import get_commit_editing_dag
from .visualisation import get_coediting_network
from .visualisation import get_coauthorship_network
from .visualisation import get_bipartite_network
from .complexity import compute_complexity

import logging

logging.basicConfig(level=logging.INFO,
                    format='[%(asctime)s]  %(name)s:%(levelname)-10s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
