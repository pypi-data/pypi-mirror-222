from setuptools import setup, find_packages

setup(
    name='pyPPG',
    version='1.0.3',
    description='pyPPG: a python toolbox for PPG morphological analysis.',
    author='Marton A. Goda, PhD',
    author_email="marton.goda@campus.technion.ac.il",
    long_description=0,
    long_description_content_type="text/markdown",
    url="https://github.com/godamartonaron/GODA_pyPPG",
    project_urls={"Bug Tracker": "https://github.com/pypa/sampleproject/issues",},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    packages={"pyPPG", "pyPPG/ppg_bm", "pyPPG/pack_ppg"},
    package_data={
        "pyPPG": ["*"],
        "pyPPG/ppg_bm": ["*"],
        "pyPPG/pack_ppg": ["*"],
    },

    install_requires=["numpy", "mne"],
    python_requires=">=3.10",
    include_package_data=True,
)