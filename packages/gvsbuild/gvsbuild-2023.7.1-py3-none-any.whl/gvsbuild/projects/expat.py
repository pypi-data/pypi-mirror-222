#  Copyright (C) 2016 - Yevgen Muntyan
#  Copyright (C) 2016 - Ignacio Casal Quinteiro
#  Copyright (C) 2016 - Arnavion
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, see <http://www.gnu.org/licenses/>.

from pathlib import Path

from gvsbuild.utils.base_builders import CmakeProject
from gvsbuild.utils.base_expanders import Tarball
from gvsbuild.utils.base_project import Project, project_add


@project_add
class Expat(Tarball, CmakeProject):
    def __init__(self):
        Project.__init__(
            self,
            "expat",
            version="2.5.0",
            repository="libexpat",
            archive_url="https://github.com/libexpat/libexpat/releases/download/R_{major}_{minor}_{micro}/expat-{version}.tar.xz",
            hash="ef2420f0232c087801abf705e89ae65f6257df6b7931d37846a193ef2e8cdcbe",
            dependencies=["cmake", "ninja"],
        )

    def build(self):
        CmakeProject.build(self, use_ninja=True)
        self.install(r".\COPYING share\doc\expat")

    def post_install(self):
        if self.builder.opts.configuration == "debug":
            # Fontconfig is looking for libexpat, not libexpatd
            bin_dir = Path(self.builder.gtk_dir) / "bin"
            self.builder.exec_msys(
                ["mv", "libexpatd.dll", "libexpat.dll"],
                working_dir=bin_dir,
            )
            lib_dir = Path(self.builder.gtk_dir) / "lib"
            self.builder.exec_msys(
                ["mv", "libexpatd.lib", "libexpat.lib"],
                working_dir=lib_dir,
            )
