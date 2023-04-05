import setuptools
# 若Discription.md中有中文 須加上 encoding="utf-8"
with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()
    
setuptools.setup(
    name = "pteropy",
    version = "0.1.2",
    author = "seanbbear",
    author_email="ccoccc14@gmail.com",
    description="簡單存取Pterodactyl api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HansHans135/pteropy",                                         
    packages=setuptools.find_packages(),     
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
    )
