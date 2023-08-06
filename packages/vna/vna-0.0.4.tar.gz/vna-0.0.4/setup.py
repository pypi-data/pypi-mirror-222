from setuptools import setup
import distutils.sysconfig

setup(
    name='vna',
    version='0.0.4',
    description='Instrument control library for the PicoVNA 106 and PicoVNA 108. Please note that additional libraries are required, not installed by this package. See the Python Programming Manual for details.',
    url='http://picotech.com',
    author='AAI Robotics Ltd',
    author_email='help@aairobotics.com',
    license='MIT',
    packages=["vna"],
    include_package_data=True,
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Unix",
        "Operating System :: MacOS",
    ],
)
