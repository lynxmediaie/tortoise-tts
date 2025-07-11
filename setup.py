import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tortoise-tts",
    packages=setuptools.find_packages(),
    version="3.0.0",
    author="James Betker",
    author_email="james@adamant.ai",
    description="A high quality multi-voice text-to-speech library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/neonbjb/tortoise-tts",
    project_urls={},
    scripts=[
        'scripts/tortoise_tts.py',
    ],
    include_package_data=True,
    install_requires=[
        'tqdm',
        'rotary_embedding_torch',
        'inflect',
        'progressbar',
        'einops',
        'unidecode',
        'scipy',
        'librosa',
        'transformers==4.31.0',
        'tokenizers==0.13.0',
        'scipy==1.12.0',
        'scikit-learn==1.6.0',
        'fastapi',
        'uvicorn',
        'deepspeed==0.8.3',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
