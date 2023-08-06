import setuptools
from setuptools import setup, find_packages

with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='SGtSNEpiPy',
    version='1.0.8',
    description='SGtSNEpiPy is a Python interface to SG-t-SNE-П, a powerful tool for visualizing large, sparse, stochastic graphs.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=['Chenshuhao Qin','Yihua Zhong'],
    author_email="cq27@duke.edu, yz737@duke.edu,",
    classifiers=[
                'Programming Language :: Python',
                'Intended Audience :: Developers',
                 ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'juliacall >= 0.9.13',
    ]
)