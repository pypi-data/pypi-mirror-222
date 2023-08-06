import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="myoconverter",
    version="0.0.2",
    author="Huawei Wang, Aleksi Ikkala",
    author_email="",
    description="Tool for converting OpenSim musculoskeletal (MSK) models to the MuJoCo model format with optimized muscle kinematics and kinetics",
    long_description="Check the [GitHub repository](https://github.com/MyoHub/myo-converter) for up-to-date documentation",
    long_description_content_type="text/markdown",
    url="https://github.com/MyoHub/myo-converter",
    packages=setuptools.find_packages(),
    install_requires=[
      'python>=3.9',
      'mujoco-python==2.3.3',
      'loguru==0.5.3',
      'lxml==4.9.1',
      'numpy==1.21.5',
      'scipy==1.10.0',
      'scikit-learn==1.2.0',
      'opensim==4.4',
      'matplotlib==3.6.2',
      'trimesh==3.22.2',
      'pyvista==0.39.1',
      'networkx==2.8.4',
      'fpdf2==2.7.4',
      'seaborn==0.12.2'
    ]
)
