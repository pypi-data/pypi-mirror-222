from setuptools import setup, find_packages


setup(
    name="lynkpy",
    version="0.0.5",
    author="Siddharth",
    author_email="ssiddharth408@gmail.com",
    description="basic utilities",
    long_description="basic utilities",
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    install_requires=[             # List any dependencies your package needs
        'concurrent_log_handler', 'Pillow'
    ],
    python_requires='>=3.8',
)