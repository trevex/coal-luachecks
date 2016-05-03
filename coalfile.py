from coal import CoalFile
from util import cp, git_clone, glob
from os import path

class LuachecksFile(CoalFile):
    url = "https://github.com/fab13n/checks.git"
    exports = ["include", "src"]

    def prepare(self):
        git_clone(self.url, 'master', 'repo')
    def package(self):
        cp('repo/*.h', 'include/')
        cp('repo/*.c', 'src/')
    def info(self, generator):
        generator.add_include_dir('include/')
        generator.add_source_files(*glob('src/*'))
