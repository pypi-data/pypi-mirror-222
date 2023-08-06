# Copyright 2020, General Electric Company. All rights reserved. See https://github.com/xcist/code/blob/master/LICENSE

# To install XCIST-CatSim, open Python console, run: pip install [folder name]
# e.g., you can navigate to this folder, run: pip install .

from setuptools import setup, find_packages

setup(name='gecatsim',
      version='0.2.1',
      description='Simulation toolkit for X-ray based cancer imaging',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      url='https://github.com/xcist',
      author='Mingye Wu, Paul FitzGerald, Brion Sarachan, Bruno De Man',
      author_email='Mingye.Wu@ge.com',
      license='BSD 3-Clause License',
      install_requires=['numpy', 'scipy', 'matplotlib'],
      #packages=['src/catsim', 'src/catsim.pyfiles', 'src/reconstruction'],
      packages=find_packages('src'),
      package_dir={'': 'src'},
      zip_safe=False,
      package_data={
          'catsim':[r'lib/*.*', r'cfg/*.cfg', 
                    r'bowtie/*.txt', r'material/*', r'material/edlp/*/*.dat',
                    r'phantom/*.*', r'phantom/CatSimLogo_1024/*.*', r'phantom/poly_bin/poly*',
                    r'scatter/*.dat', r'spectrum/*.dat'],
          'reconstruction':[r'pyfiles/*.*', r'lib/*.*']},
      include_package_data=True)
