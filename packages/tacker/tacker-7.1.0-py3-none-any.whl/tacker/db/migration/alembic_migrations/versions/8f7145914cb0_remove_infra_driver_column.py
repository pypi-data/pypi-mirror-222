# Copyright 2016 OpenStack Foundation
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

"""remove infra_driver column

Revision ID: 8f7145914cb0
Revises: 0ae5b1ce3024
Create Date: 2016-12-08 17:28:26.609343

"""

# flake8: noqa: E402

# revision identifiers, used by Alembic.
revision = '8f7145914cb0'
down_revision = '0ae5b1ce3024'

from alembic import op


def upgrade(active_plugins=None, options=None):
    op.drop_column('vnfd', 'infra_driver')
