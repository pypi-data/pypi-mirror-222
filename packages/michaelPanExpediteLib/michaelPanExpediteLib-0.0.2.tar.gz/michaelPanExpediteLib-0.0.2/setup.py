import setuptools
with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()
setuptools.setup(
    name="michaelPanExpediteLib",  # 库的名称
    version="0.0.2",  # 库的版本号
    author="chuntong pan",  # 库的作者
    author_email="panzhang1314@gmail.com",  # 作者邮箱
    description="Expedite array circulation",  # 库的简述
    install_requires=['numba', 'tqdm'],  # 需要的依赖库
    long_description=long_description,
    long_description_content_type="text/markdown",
    platforms=["all"],
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent"],
)
