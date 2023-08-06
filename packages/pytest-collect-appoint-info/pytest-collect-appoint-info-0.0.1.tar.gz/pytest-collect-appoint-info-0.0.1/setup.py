import setuptools

setuptools.setup(
    name="pytest-collect-appoint-info",  # Replace with your own username
    version="0.0.1",
    author="jin.fang",
    author_email="xxxxxxxx@example.com",
    description="set your encoding",
    long_description="show Chinese for your mark.parametrize().",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Pytest",
    ],
    license='MIT License',
    packages=['pytest_collect_appoint_info'],
    keywords=[
        "pytest",
        "py.test",
        "pytest_collect",
    ],
    install_requires=[
        'pytest'
    ],
    python_requires=">=3.6",
    # 入口模块或者入口函数
    entry_points={
        'pytest11': [
            'pytest-collect-appoint-info = pytest_collect_appoint_info'
        ]
    },

    zip_safe=False,
)
