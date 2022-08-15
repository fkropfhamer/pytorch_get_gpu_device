import setuptools

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name="pytorch_get_gpu_device",
    version="1.0.0",
    author="fkropfhamer",
    description="A helper function to get a pytorch gpu device.",
    packages=["pytorch_get_gpu_device"],
    install_requires=[
        'torch >= 1.11'
    ],
    keywords=["pytorch", "gpu"],
    license="MIT",
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires=">=3.7",
    url="https://github.com/fkropfhamer/pytorch_get_gpu_device",
)
