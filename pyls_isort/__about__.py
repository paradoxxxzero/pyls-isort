from email import message_from_string

try:
    from pkg_resources import get_distribution
    dist = get_distribution(__package__)
    pkgInfo = get_distribution(__package__).get_metadata('PKG-INFO')

    __metadata__ = message_from_string(pkgInfo)
    del pkgInfo, dist

    __title__ = __metadata__['Name']
    __version__ = __metadata__['Version']

    __summary__ = __metadata__['Summary']
    __uri__ = __metadata__['Home-page']
    __author__ = __metadata__['Author']
    __email__ = __metadata__['Author-email']

    __license__ = __metadata__['License']
    __copyright__ = "Copyright 2017 %s" % __author__
except:
    pass