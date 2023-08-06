from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pyspectrum_lib',
    version='1.0.0',
    py_modules=['spectrum_lib.spectrum_lib'],
    packages=['spectrum_lib'],
    url='https://gitlab.com/neurosdk2/neurosamples/-/tree/main/python',
    license='MIT',
    author='Brainbit Inc.',
    author_email='support@brainbit.com',
    description='Python wrapper for Spectrum math library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    include_package_data=True,
    package_data={"spectrum_lib": ['libs\\spectrumlib-x64.dll',
                               'libs\\spectrumlib-x86.dll']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Intended Audience :: Developers",
    ],
    python_requires='>=3.7',
)