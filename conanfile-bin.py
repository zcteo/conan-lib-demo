import os
from conan import ConanFile
from conan.tools.files import copy


class FooConan(ConanFile):
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
        include_folder = os.path.join(self.source_folder, "include")
        lib_folder = os.path.join(self.build_folder, "lib")
        copy(self, "*", include_folder, os.path.join(self.package_folder, "include"), keep_path=False)
        copy(self, "*", lib_folder, os.path.join(self.package_folder, "lib"), keep_path=False)

# 打包预先编译的二进制库；
# conan export-pkg . name/version@
# conan export-pkg . name/version@user/channel
# 2.0 命令如下
# conan export-pkg . --name name --version version
# conan export-pkg . --name name --version version --user user --channel channel