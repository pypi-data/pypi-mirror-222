"""
Copyright 2022 OVO Energy Ltd

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from os import environ
from pathlib import Path

from setuptools import setup

setup(
    name="VertFlow",
    version=environ["VERTFLOW_VERSION"],
    description="Apache Airflow operator for running Google Cloud Run Jobs using green energy",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    author="OVO Energy",
    author_email="trading.dl@ovoenergy.com",
    packages=["VertFlow"],
    package_dir={"VertFlow": "src"},
    python_requires=">=3.7",
    install_requires=[
        "google-api-python-client<2.0.0,>=1.6.0",
        "requests-cache==0.6.0",
        "geocoder>=1.38.1,<2.0.0",
        "oauth2client<4.0.0",  # Required by googleapiclient
    ],
    license="Apache 2.0",
    keywords=[
        "airflow",
        "gcp",
        "google",
        "cloud run",
        "cloud composer",
        "green",
        "environment",
        "sustainability",
    ],
    url="https://github.com/ovotech/VertFlow",
)
