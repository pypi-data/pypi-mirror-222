from setuptools import find_packages, setup

setup(
    name="gitlab_sdk",
    version="0.1.0",
    description="Client side Python SDK for GitLab Application services",
    author="GitLab",
    url="https://gitlab.com/gitlab-org/analytics-section/product-analytics/gl-application-sdk-python",
    author_email="gitlab_rubygems@gitlab.com",
    packages=find_packages(),
    install_requires=[
        "snowplow_tracker>=1.0.0",
    ],
)
