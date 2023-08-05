# Copyright 2022 DeepMind Technologies Limited. All Rights Reserved.
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
# ==============================================================================
"""Install script."""

import setuptools

setuptools.setup(
    name="lingo-llm",
    version="1.1.0",
    url="https://github.com/WENGSYX/Lingo",
    author="Yixuan Weng",
    author_email="wengsyx@gmail.com",
    description="Lingo: Make the LLM Better for Everyone",
    packages=setuptools.find_packages(),
    install_requires=[
        "transformers>=4.30.2",
        "numpy",
        "datasets",
        "torch",
        "nvidia-ml-py",
        'sentencepiece',
        "openai>=0.27.8"
    ],
)
