from setuptools import setup, find_packages

setup(
    name='earthml',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'fiona',
        'rasterio',
        'pygeohash',
        'Pillow',
        'laspy',
    ],
    author='Akhil Chhibber',
    author_email='akhil.chibber@gmail.com',
    description='A library to Perform different possible operations on Geo-Spatial Dataset',
    url='https://github.com/akhilchibber',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: GIS',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)