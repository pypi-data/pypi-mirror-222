from setuptools import setup, find_packages

setup(
    name="VizTyping",
    version="0.0.0.2",
    py_modules=["VizTyping"],
    install_requires=[
        'docarray'
    ],
    author="zrTalker",
    author_email="gy.song@aliyun.com",
    description="A typing tool for Vizor and VizNrn ",
    license="MIT",
    packages=find_packages(),
    keywords="Vizor VizNrn",
    url="https://git.baijiashilian.com/innovation/aiprojects/ai_group/viztyping",

)
