# Copyright 2022-2023 XProbe Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import platform
import shutil
import subprocess
import sys
import warnings
from sysconfig import get_config_vars

import numpy as np
from Cython.Build import cythonize
from pkg_resources import parse_version
from setuptools import Command, Extension, setup
from setuptools.command.develop import develop
from setuptools.command.install import install
from setuptools.command.sdist import sdist

try:
    import distutils.ccompiler

    if sys.platform != "win32":
        from numpy.distutils.ccompiler import CCompiler_compile

        distutils.ccompiler.CCompiler.compile = CCompiler_compile
except ImportError:
    pass

# From https://github.com/pandas-dev/pandas/pull/24274:
# For mac, ensure extensions are built for macos 10.9 when compiling on a
# 10.9 system or above, overriding distuitls behaviour which is to target
# the version that python was built for. This may be overridden by setting
# MACOSX_DEPLOYMENT_TARGET before calling setup.py
if sys.platform == "darwin":
    if "MACOSX_DEPLOYMENT_TARGET" not in os.environ:
        current_system = platform.mac_ver()[0]
        python_target = get_config_vars().get(
            "MACOSX_DEPLOYMENT_TARGET", current_system
        )
        target_macos_version = "10.9"

        parsed_python_target = parse_version(python_target)
        parsed_current_system = parse_version(current_system)
        parsed_macos_version = parse_version(target_macos_version)
        if parsed_python_target <= parsed_macos_version <= parsed_current_system:
            os.environ["MACOSX_DEPLOYMENT_TARGET"] = target_macos_version


repo_root = os.path.dirname(os.path.abspath(__file__))
os.chdir(repo_root)


cythonize_kw = dict(language_level=sys.version_info[0])
define_macros = []
if os.environ.get("CYTHON_TRACE"):
    define_macros.append(("CYTHON_TRACE_NOGIL", "1"))
    define_macros.append(("CYTHON_TRACE", "1"))
    cythonize_kw["compiler_directives"] = {"linetrace": True}

# Fixes Python 3.11 compatibility issue
#
# see also:
# - https://github.com/cython/cython/issues/4500
# - https://github.com/scoder/cython/commit/37f270155dbb5907435a1e83fdc90e403d776af5
if sys.version_info >= (3, 11):
    define_macros.append(("CYTHON_FAST_THREAD_STATE", "0"))

cy_extension_kw = {
    'define_macros': define_macros,
}

if "MSC" in sys.version:
    extra_compile_args = ["/std:c11", "/Ot", "/I" + os.path.join(repo_root, "misc")]
    cy_extension_kw["extra_compile_args"] = extra_compile_args
else:
    extra_compile_args = ["-O3"]
    if sys.platform != "darwin":
        # for macOS, we assume that C++ 11 is enabled by default
        extra_compile_args.append("-std=c++0x")
    cy_extension_kw["extra_compile_args"] = extra_compile_args


# The pyx with C sources.
ext_include_source_map = {
    "xorbits/_mars/_utils.pyx": [
        ["xorbits/_mars/lib/mmh3_src"],
        ["xorbits/_mars/lib/mmh3_src/MurmurHash3.cpp"],
    ],
}


def _discover_pyx():
    exts = dict()
    for root, _, files in os.walk(os.path.join(repo_root, "xorbits"), followlinks=True):
        for fn in files:
            if not fn.endswith(".pyx"):
                continue
            full_fn = os.path.relpath(os.path.join(root, fn), repo_root)
            include_dirs, source = ext_include_source_map.get(
                full_fn.replace(os.path.sep, "/"), [[], []]
            )
            mod_name = full_fn.replace(".pyx", "").replace(os.path.sep, ".")
            exts[mod_name] = Extension(
                mod_name,
                [full_fn] + source,
                include_dirs=[np.get_include()] + include_dirs,
                **cy_extension_kw,
            )
    return exts


extensions_dict = _discover_pyx()
cy_extensions = list(extensions_dict.values())

extensions = cythonize(cy_extensions, **cythonize_kw) + [
    Extension(
        "xorbits._mars.lib.mmh3",
        [
            "xorbits/_mars/lib/mmh3_src/mmh3module.cpp",
            "xorbits/_mars/lib/mmh3_src/MurmurHash3.cpp",
        ],
    )
]


class ExtraCommandMixin:
    _extra_pre_commands = []

    def run(self):
        [self.run_command(cmd) for cmd in self._extra_pre_commands]
        super().run()

    @classmethod
    def register_pre_command(cls, cmd):
        cls._extra_pre_commands.append(cmd)


class CustomInstall(ExtraCommandMixin, install):
    pass


class CustomDevelop(ExtraCommandMixin, develop):
    pass


class CustomSDist(ExtraCommandMixin, sdist):
    pass


class BuildWeb(Command):
    """build_web command"""

    user_options = []
    _web_src_path = "xorbits/web/ui"
    _web_dest_path = "xorbits/web/ui/static/bundle.js"
    _commands = [
        ["npm", "install"],
        ["npm", "run", "build"],
    ]

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    @classmethod
    def run(cls):
        if int(os.environ.get("NO_WEB_UI", "0")):
            return

        npm_path = shutil.which("npm")
        web_src_path = os.path.join(repo_root, *cls._web_src_path.split("/"))
        web_dest_path = os.path.join(repo_root, *cls._web_dest_path.split("/"))

        if npm_path is None:
            warnings.warn("Cannot find NPM, may affect displaying Xorbits web UI")
            return
        else:
            replacements = {"npm": npm_path}
            cmd_errored = False
            for cmd in cls._commands:
                cmd = [replacements.get(c, c) for c in cmd]
                proc_result = subprocess.run(cmd, cwd=web_src_path)
                if proc_result.returncode != 0:
                    warnings.warn(f'Failed when running `{" ".join(cmd)}`')
                    cmd_errored = True
                    break
            if not cmd_errored:
                assert os.path.exists(web_dest_path)


CustomInstall.register_pre_command("build_web")
CustomDevelop.register_pre_command("build_web")
CustomSDist.register_pre_command("build_web")


# Resolve path issue of versioneer
sys.path.append(repo_root)
versioneer = __import__("versioneer")


# build long description
def build_long_description():
    readme_path = os.path.join(os.path.dirname(os.path.abspath(repo_root)), "README.md")

    with open(readme_path, encoding="utf-8") as f:
        return f.read()


setup_options = dict(
    version=versioneer.get_version(),
    ext_modules=extensions,
    cmdclass=versioneer.get_cmdclass(
        {
            "build_web": BuildWeb,
            "install": CustomInstall,
            "develop": CustomDevelop,
            "sdist": CustomSDist,
        }
    ),
    long_description=build_long_description(),
    long_description_content_type="text/markdown",
)
setup(**setup_options)
