import subprocess as sp
import re as re

__version__ = '0.0.4'
try:
    # Try to use git to find current commit.
    p = sp.Popen(
        ["git", "describe", "--always"], stdout=sp.PIPE, stderr=sp.PIPE)
    output, error = p.communicate()
    git_describe = output.decode("utf-8").strip()
    __version__ = re.sub('-g[0-9a-f]*$', '', git_describe)
except sp.CalledProcessError as e:
    pass