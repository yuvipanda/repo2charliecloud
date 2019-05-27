from setuptools import setup, find_packages

setup(
    name='repo2charliecloud',
    version='0.0.1',
    install_requires=[
        'jupyter-repo2docker',
        'charliecloud-bin'
    ],
    description='JupyterHub Spawner for Kubernetes',
    author='Yuvi Panda',
    author_email='yuvipanda@gmail.com',
    license='BSD',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['repo2charliecloud=repo2charliecloud:main']
    }
)
