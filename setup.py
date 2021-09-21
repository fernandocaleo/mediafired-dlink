from setuptools import setup, find_packages

setup(
    name="mediafire-dl",
    version="0.1.0",
    description="UN script simple para descargar enlaces de mediafire basado en gdown",
    url="https://github.com/fernandocaleo/mediafired-dlink",
    author="Fernando Caleo",
    author_email="fcaleo@nauta.cu",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="audo ai",
    py_modules=['mediafire_dl'],
    install_requires=[
        "requests",
        "tqdm",
    ],
    entry_points={
        "console_scripts": ["mediafire-dl=mediafire_dl:main"],
    },
)
