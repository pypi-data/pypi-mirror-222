from setuptools import setup, find_packages

setup(
    name='level3_NI_test',
    version='0.2.1',
    description='Test uploading module to PyPi',
    author='Hamza Daoud',
    author_email='hamzadaoud99@gmail.com',
    packages=find_packages(),
    install_requires=[],  # List any dependencies your package needs
    classifiers=[
        'Development Status :: 3 - Alpha',  # Choose an appropriate status
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
