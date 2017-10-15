from distutils.core import setup

def find_version(path):
    import re
    # path shall be a plain ascii text file.
    s = open(path, 'rt').read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              s, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Version not found")

setup(
    name="thechef",
    version=find_version("thechef/version.py"),
    author="Yu Feng",
    author_email="rainwoodman@gmail.com",
    url="http://github.com/rainwoodman/theshef",
    description="A python data model of kitchen activities",
    zip_safe = False,
    package_dir = {'thechef': 'thechef'},
    install_requires=[],
    scripts = [],
    packages= ['thechef', 'thechef.tests'],
    license='GPLv3',
#    ext_modules = cythonize(extensions)
)
