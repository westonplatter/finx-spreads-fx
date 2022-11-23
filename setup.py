import setuptools

package_name = "finx_spreads_fx"

version_text = None
with open(f"{package_name}/version.txt", "r", encoding="utf-8") as f:
    version_text = f.read()

with open("README.md", "r") as f:
    long_description = f.read()

deps = [
    "ib_insync",
    "loguru",
    "pandas",
    "numpy",
    "pydantic",
    "python-dotenv",
    "pytz",
    "requests",
]

project_url = f"https://github.com/westonplatter/{package_name.replace('_', '-')}/"

setuptools.setup(
    name=package_name,
    version=version_text,
    description="Finx package for quantifying FX spreads",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="westonplatter",
    author_email="westonplatter+finx@gmail.com",
    license="BSD-3",
    url=project_url,
    python_requires=">=3.6",
    packages=[package_name],
    install_requires=deps,
    project_urls={
        "Issue Tracker": f"{project_url}/issues",
        "Source Code": f"{project_url}",
    },
)
