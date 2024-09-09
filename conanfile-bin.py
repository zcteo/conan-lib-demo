from conan import ConanFile
from conan.tools.files import copy, collect_libs


class Pkg(ConanFile):
    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Mypackage here>"

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": True}

    def requirements(self):
        # self.requires("name/version@user/channel")
        pass

    def package(self):
        copy(self, "include/*", self.source_folder, self.package_folder)
        copy(self, "lib/*", self.source_folder, self.package_folder)

    def package_info(self):
        self.cpp_info.libs = collect_libs(self)
