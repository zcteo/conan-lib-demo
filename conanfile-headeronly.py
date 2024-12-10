from conan import ConanFile
from conan.tools.files import copy


class Pkg(ConanFile):
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Mypackage here>"
    # No settings/options are necessary, this is header only

    def package(self):
        # This will also copy the "include" folder
        copy(self, "include/*", self.source_folder, self.package_folder)

    def package_info(self):
        # For header-only packages, libdirs and bindirs are not used
        # so it's necessary to set those as empty.
        self.cpp_info.bindirs = []
        self.cpp_info.libdirs = []
