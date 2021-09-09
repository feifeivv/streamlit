# Copyright 2018-2021 Streamlit Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os


def open_python_file(filename):
    """Open a read-only Python file taking proper care of its encoding.

    In Python 3, we would like all files to be opened with utf-8 encoding.
    However, some author like to specify PEP263 headers in their source files
    with their own encodings. In that case, we should respect the author's
    encoding.
    """
    import tokenize

    if hasattr(tokenize, "open"):  # Added in Python 3.2
        # Open file respecting PEP263 encoding. If no encoding header is
        # found, opens as utf-8.
        return tokenize.open(filename)
    else:
        return open(filename, "r", encoding="utf-8")


STREAMLIT_APP_SUFFIX = "_app.py"


def find_files_with_suffix(starting_dir, suffix):
    # NOTE: We'll want to do some sort of verification on starting_dir (does it
    # actually exist / is it actually a directory) in the hardened version of
    # this feature, but the best place to do so may not be within this
    # function.

    matching_files = []

    for root, _, filenames in os.walk(starting_dir):
        for name in filenames:
            if name.endswith(suffix):
                matching_files.append(os.path.join(root, name))

    return matching_files
