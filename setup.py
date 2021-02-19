from setuptools import setup

setup(
    name="nhsuk-jinja-components",
    version="0.0.1",
    author="Richard Pope",
    description="NHS UK Design system components ported Digital Land's GOV.UK Jinja library",
    license="MIT",
    packages=["nhsuk-jinja-components"],
    package_data={'nhsuk-jinja-components': ['templates/**.*']},
    python_requires=">=3.5",
    install_requires=[
        "jinja2",
    ],
)
