# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.


def try_import(module_name):
    try:
        __import__(module_name)
    except ImportError:
        pass


# Try to import experiments, ignore if not available
try_import("torchtitan.experiments.llama4")
try_import("torchtitan.experiments.qwen3")
try_import("torchtitan.experiments.simple_fsdp")
try_import("torchtitan.experiments.blendcorpus")

# import torchtitan.experiments.llama4  # noqa: F401
# import torchtitan.experiments.qwen3
# import torchtitan.experiments.simple_fsdp  # noqa: F401
# import torchtitan.experiments.blendcorpus
