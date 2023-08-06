"""Setup file."""
from setuptools import setup
import versioneer

if __name__ == "__main__":
    setup(
        name="caf.toolkit",
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
    )
