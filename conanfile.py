import os
from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake, cmake_layout
from conan.tools.build import cross_building
from conan.tools.files import load, save, update_conandata, copy


class FooConan(ConanFile):
    name = "conandemo"
    version = "0.0.1"

    # Optional metadata
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Mypackage here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    default_channel = "testing"
    default_user = "demo"
    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    generators = "CMakeDeps"

    # Sources are located in the same place as this recipe, copy them to the recipe
    # exports_sources = "CMakeLists.txt", "src/*", "test/*"
    no_copy_source = True

    # 将源码路径保存在/tmp/name + version文件夹下面
    sources_file_path = os.path.join("/tmp", name + version)

    def set_name(self):
        pass

    def set_version(self):
        pass

    def export(self):
        # update_conandata(self, {"sources": {"path": self.recipe_folder}})
        save(self, self.sources_file_path, self.recipe_folder)

    def config_options(self):  # 到这一步的时候setting有值，option还是默认值
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        if self.options.shared:
            del self.options.fPIC
        self.options["jsoncpp"].shared = self.options.shared

    def layout(self):
        cmake_layout(self)

    def requirements(self):
        self.requires("jsoncpp/1.9.5")

    def build_requirements(self):
        self.test_requires("gtest/1.11.0")

    def source(self):
        # copy(self, '*', self.conan_data["sources"]["path"], ".")
        sources_path = load(self, self.sources_file_path)
        copy(self, '*', sources_path, ".")

    def generate(self):
        tc = CMakeToolchain(self)
        tc.user_presets_path = False
        tc.variables["CONAN_BUILD"] = 1
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        if not cross_building(self) and not self.conf.get("tools.build:skip_test", default=False):
            self.run_unit_test()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = [self.name]

    def run_unit_test(self):  # 自定义方法，运行单元测试
        cmd = os.path.join("test", "test")
        self.run(cmd, env="conanrun")
