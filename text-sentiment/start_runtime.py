import sys
import multiprocessing

if sys.platform == "win32":
    orig_get_context = multiprocessing.get_context
    def get_context(method=None):
        if method in ("fork", "forkserver"):
            method = "spawn"
        return orig_get_context(method)
    multiprocessing.get_context = get_context

# Copyright The Caikit Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Standard
import os

# First Party
import alog


# Local
from caikit.runtime import grpc_server
import text_sentiment


alog.configure(default_level="debug")

# Start the gRPC Caikit runtime server
if __name__ == "__main__":
    grpc_server.main()