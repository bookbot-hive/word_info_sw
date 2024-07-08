from setuptools import find_packages, setup
import os

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")) as f:
    long_description = f.read()

install_requires = ["gruut[sw]", "openai==0.28"]

if __name__ == "__main__":
    setup(
        name="word_info_sw",
        description="Swahili Word Info.",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="w11wo",
        author_email="wilson@bookbotkids.com",
        url="https://github.com/bookbot-hive/word_info_sw",
        license="Apache License",
        packages=find_packages(),
        install_requires=install_requires,
        dependency_links=["https://synesthesiam.github.io/prebuilt-apps/"],
        include_package_data=True,
        platforms=["linux", "unix", "windows"],
        python_requires=">=3.6",
    )
