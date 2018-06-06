from distutils.core import setup
setup(
  name = 'mbot',
  packages = ['mbot'], # this must be the same as the name above
  version = '0.1',
  description = 'A Messenger bot creatioin library',
  author = 'Stefan Nožinić',
  author_email = 'stefan@lugons.org',
  url = 'https://github.com/fantastic001/mbot', # use the URL to the github repo
  keywords = ['api', 'messenger', 'bot'], # arbitrary keywords
  package_dir = {'mbot': 'src'},
  classifiers = []
)
