# pylint: disable=W0622
"""cubicweb-geocoding application packaging information"""

modname = "geocoding"
distname = "cubicweb-geocoding"

numversion = (1, 0, 0)
version = ".".join(str(num) for num in numversion)

license = "LGPL"
author = "LOGILAB S.A. (Paris, FRANCE)"
author_email = "contact@logilab.fr"
description = "geocoding views such as google maps"
web = f"https://forge.extranet.logilab.fr/cubicweb/cubes/{distname}"

classifiers = [
    "Environment :: Web Environment",
    "Framework :: CubicWeb",
    "Programming Language :: Python",
    "Programming Language :: JavaScript",
]

__depends__ = {
    "cubicweb": ">= 4.0.0, < 5.0.0",
    "cubicweb-web": ">= 1.0.0, < 2.0.0",
}
__recommends__ = {}
