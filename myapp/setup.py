from setuptools import setup

setup(
    name="My Django app",
    version="1.0.0",
    entry_points={
        "console_scripts": [
            "foo = package_name.module_name:func_name",
            "foo_dev = package_name.module_name:func_name [develop]"
        ],
        "gui_scripts": [
            "bar = gui_package_name.gui_module_name:gui_func_name"
        ]
    },
    author="shin",
    author_email="me@example.com",
    description="my Django app",
    keywords="hello world example examples",
    url="https://github.com/Bakushin10/Django",   # project home page, if any
    project_urls={
        "Bug Tracker": "https://github.com/Bakushin10/Django",
        "Documentation": "https://github.com/Bakushin10/Django",
        "Source Code": "https://github.com/Bakushin10/Django",
    },
)