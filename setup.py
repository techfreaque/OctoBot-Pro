import asyncio

from setuptools import find_packages
from setuptools import setup
from distutils.command.install import install


# from octobot_pro import PROJECT_NAME, VERSION
# todo figure out how not to import octobot_pro.__init__.py here
PROJECT_NAME = "OctoBot-Pro"
VERSION = "0.0.1"  # major.minor.revision


def _post_install():
    import octobot_pro.cli
    asyncio.run(octobot_pro.cli.install_all_tentacles(True))


class InstallWithPostInstallAction(install):
    def run(self):
        install.run(self)
        self.execute(_post_install, (), msg="Installing OctoBot-Pro tentacles")


PACKAGES = find_packages(
    exclude=[
        "tests",
        "octobot_pro.imports*",
        "octobot_pro.user*",
    ]
)

# long description from README file
with open('README.md', encoding='utf-8') as f:
    DESCRIPTION = f.read()

REQUIRED = open('requirements.txt').readlines()
REQUIRES_PYTHON = '>=3.8'

setup(
    name=PROJECT_NAME,
    version=VERSION,
    url='https://github.com/Drakkar-Software/OctoBot-Pro',
    license='GPL-3.0',
    author='Drakkar-Software',
    author_email='drakkar-software@protonmail.com',
    description='Backtesting framework of the OctoBot Ecosystem',
    packages=PACKAGES,
    cmdclass={'install': InstallWithPostInstallAction},
    long_description=DESCRIPTION,
    long_description_content_type='text/markdown',
    tests_require=["pytest"],
    test_suite="tests",
    zip_safe=False,
    data_files=[],
    setup_requires=REQUIRED,
    install_requires=REQUIRED,
    python_requires=REQUIRES_PYTHON,
    entry_points={
        'console_scripts': [
            'octobot_pro = octobot_pro.cli:main'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
