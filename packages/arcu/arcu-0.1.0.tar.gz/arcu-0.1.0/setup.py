from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='arcu',
    version='0.1.0',
    description='Find representative subpopulations in single cell imaging data.',
    author='Harris Davis',
    author_email='harris.davis@outlook.com',
    url='https://github.com/harrismdavis/arcu',
    license='MIT',
    python_requires='>=3.6',
    long_description=long_description,
    long_description_content_type = 'text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
    keywords=[
        'image analysis',
        'single-cell bioinformatics',
        'computational biology',
    ],
    install_requires=[
        'numpy>=1.22.4',
        'pandas>=1.3.2',
    ],
    ext_modules=[],
)