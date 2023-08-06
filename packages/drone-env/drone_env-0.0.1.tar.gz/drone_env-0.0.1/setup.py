from setuptools import setup


setup(
    name='drone_env',
    version='0.0.1',
    description="A OpenAI Gym Env for Parrot Mini Drone",
    install_requires=['gymnasium==0.28.1', 'numpy==1.25.1', 'matlabengine==9.14.3']
)
