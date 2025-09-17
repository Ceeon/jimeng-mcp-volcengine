from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="jimeng-mcp-volcengine",
    version="1.0.1",
    author="Ceeon",
    author_email="your-email@example.com",  # 替换为您的邮箱
    description="即梦AI MCP服务器 - 火山引擎官方API直连版本",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ceeon/jimeng-mcp-volcengine",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Multimedia :: Graphics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "fastmcp>=0.1.0",
        "httpx>=0.24.0",
        "Pillow>=10.0.0",
    ],
    py_modules=["jimeng_mcp", "image_processor"],
    entry_points={
        'console_scripts': [
            'jimeng-mcp-volcengine=jimeng_mcp:run_server',
        ],
    },
    keywords="mcp jimeng ai image-generation volcengine doubao seedream ark",
    project_urls={
        "Bug Reports": "https://github.com/Ceeon/jimeng-mcp-volcengine/issues",
        "Source": "https://github.com/Ceeon/jimeng-mcp-volcengine",
    },
)