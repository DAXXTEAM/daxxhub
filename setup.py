
from setuptools import setup, find_packages
from os import path
base_dir = path.abspath(path.dirname(__file__))
setup(
  name = 'daxxhub',        
  packages = ['daxxhub'],
  include_package_data=True,
  version = '1.2',    
  license='MIT',     
  description = 'daxxhub Logo Generator', 
  author = 'Mr Daxx',                  
  author_email = 'mrdaxxteam@gmail.com',     
  url = 'https://github.com/daxxteam/daxxhub',   
  download_url = 'https://github.com/daxxteam/daxxhub/archive/0.1.tar.gz',    
  keywords = ['daxxhub', 'logo', 'generator'], 
  install_requires=[           
          'pillow',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
