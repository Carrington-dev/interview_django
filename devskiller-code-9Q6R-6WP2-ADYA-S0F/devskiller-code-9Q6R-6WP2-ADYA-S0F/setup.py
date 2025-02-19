from setuptools import find_packages, setup


packages = [
    "pytest<7,>=5",
    "pytest-django",
    "pytest-sugar",
    "pytest-timeout",
]

setup(
    name="django-leave-request",
    version="1.2.0",
    author="Devskiller",
    author_email="support@devskiller.com",
    packages=find_packages(),
    python_requires=">=3.8",
    include_package_data=True,
    zip_safe=False,
    install_requires=packages
    + [
        "django==4.1",
        "factory-boy==2.12",
        "faker==17.6.0",
        "pycountry==22.3.5",
        "python-dateutil==2.8.2",
        "pytz==2022.7.1",
        "setuptools",
        "wheel",
    ],
    setup_requires=["pytest-runner"],
    tests_require=packages,
)
