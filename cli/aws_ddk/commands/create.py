# Copyright 2022 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
from typing import Dict, Optional, Tuple

from aws_ddk.services import codecommit
from aws_ddk.sh import run
from click import echo, secho

_logger: logging.Logger = logging.getLogger(__name__)


def tuples_to_dict(tuples: Tuple[Tuple[str, str]]) -> Dict[str, str]:
    dict: Dict[str, str] = {}
    for k, v in tuples:
        dict.setdefault(k, v)
    return dict


def create_code_repository(
    name: str,
    description: Optional[str] = None,
    tags: Optional[Tuple[Tuple[str, str]]] = None,
) -> None:
    _logger.debug(f"name: {name}")

    echo("Creating AWS CodeCommit repository...")
    dict_tags = tuples_to_dict(tags) if tags else None
    url = codecommit.create_repository(
        name=name,
        description=description,
        tags=dict_tags,
    )

    # Add repository url to local remote
    cmd = f"git remote add origin {url}"
    echo("Adding repository url to local remote...")
    try:
        run(cmd)
    except Exception:
        secho(f"WARNING - Failed to run `{cmd}`", blink=True, bold=True)
    echo("Done.")
