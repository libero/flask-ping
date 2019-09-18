from setuptools import setup

setup(
    name='flask-ping',
    url='https://github.com/libero/flask-ping',
    project_urls={
        'Code': 'https://github.com/libero/flask-ping',
        'Issue tracker': 'https://github.com/libero/publisher/issues'
    },
    license='MIT',
    maintainer='eLife sciences publications',
    description='Blueprint for a /ping endpoint that can be added to python Flask applications',
    packages=['flask_ping'],
    python_requires=">=3.7, <4.0",
    install_requires=["Flask>=1.0, <2.0"],
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
