from setuptools import setup


setup(
  name = 'wagtailversesblock',   
  packages = ['wagtailversesblock'],   
  version = '1.0.0',
  license='BSD 3-Clause',   
  description = 'Bible verse highlighter/formatter streamfield block for Wagtail CMS.',
  long_description=open('README.md').read(),
  long_description_content_type='text/markdown',
  author = 'Noah Rahm, Correct Syntax', 
  author_email = 'correctsyntax@yahoo.com',     
  url = 'https://github.com/Correct-Syntax/wagtail-versesblock', 
  keywords = ['wagtail', 'Bible', 'verses', 'highlighter', 'streamfield', 'django'], 
  install_requires=[           
    'wagtail>=2.9'
  ],
  classifiers=[
    'Environment :: Web Environment',
    'Framework :: Django',
    'Framework :: Wagtail',
    'Framework :: Wagtail :: 2',
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: BSD License', 
    'Programming Language :: Python :: 3',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
  ],
)
