import distutils.command.build
import shutil
import tarfile
from pathlib import Path
import urllib.request

from setuptools import setup

from setuptools_rust import Binding, RustExtension


PROJECT_ROOT_DIR = Path(__file__).resolve().parent
SRC_DIR = PROJECT_ROOT_DIR / "src"
BUILD_DIR = PROJECT_ROOT_DIR / "build"

CRATE_TARBALL_PATH = SRC_DIR / "notmongo-rs.tar.gz"
RUST_SOURCE_DIR = SRC_DIR / "notmongo-rs"
PY_SOURCE_DIR = SRC_DIR / "notmongo"


notmongo_version = (PY_SOURCE_DIR / 'version.txt').read_text().strip()


# Download notmongo-rs from crates.io
#
# TODO: This should really be done in the build function, however `setup` fails
#       if the rust sources don't already exist.
def ensure_rust_source_code_exists():
    # Fetch the tarball, if needed
    if not CRATE_TARBALL_PATH.exists():
        print('Downloading "notmongo-rs" from crates.io')
        download_url = (
            f"https://crates.io/api/v1/crates/notmongo/{notmongo_version}/download"
        )

        with urllib.request.urlopen(download_url) as response:
            with CRATE_TARBALL_PATH.open("wb") as outfile:
                shutil.copyfileobj(response, outfile)

    # Unzip the archive, if needed
    if not RUST_SOURCE_DIR.exists():
        print("Extracting rust source")
        with tarfile.open(CRATE_TARBALL_PATH) as zfile:
            zfile.extractall(SRC_DIR)

        shutil.move(SRC_DIR / f"notmongo-{notmongo_version}", RUST_SOURCE_DIR)

ensure_rust_source_code_exists()


class BuildCommand(distutils.command.build.build):
    def run(self):
        # TODO: Would be great to download the rust source here, but this causes
        # `setup` to fail

        # Chain to the regular build function
        super().run()

        # Find the built shared object as well as the built `notmongo` module
        # and move the shared object into the module
        so_path = next(iter(BUILD_DIR.glob("**/notmongo-rs*.so")))
        python_module_path = so_path.parent / "notmongo"

        assert python_module_path.exists(), f"Could not find python module at {python_module_path}"

        shared_objects_dir = python_module_path / "shared_objects"
        shared_objects_dir.mkdir(exist_ok=True)
        shutil.move(so_path, shared_objects_dir / "libnotmongo.so")

setup(
    name="notmongo",
    version=notmongo_version,
    rust_extensions=[
        RustExtension(
            "notmongo-rs",
            binding=Binding.NoBinding,
            path="src/notmongo-rs/Cargo.toml",
        )
    ],
    packages=["notmongo-rs", "notmongo"],
    package_dir={"": "src"},
    zip_safe=False,
    cmdclass={"build": BuildCommand},
    extras_require={
        "dev": [
            "black",
            "isort",
            "pre_commit",
            "pytest",
            "pytest-asyncio",
        ]
    },
)
