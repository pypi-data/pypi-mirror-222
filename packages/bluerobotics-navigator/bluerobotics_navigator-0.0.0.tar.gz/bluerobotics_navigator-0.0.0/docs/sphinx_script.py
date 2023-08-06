import sys
from subprocess import run

SPHINXBUILD = "sphinx-build"
SOURCEDIR = "source"
BUILDDIR = "build"

if __name__ == "__main__":
    target = sys.argv[1]
    run([SPHINXBUILD, "-M", target, SOURCEDIR, BUILDDIR] + sys.argv[2:])