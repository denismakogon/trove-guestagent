# Copyright 2013 Hewlett-Packard Development Company, L.P.
# All Rights Reserved.
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

from trove_guestagent.guestagent.strategy import Strategy
from trove_guestagent.openstack.common import log as logging

LOG = logging.getLogger(__name__)


def get_backup_strategy(backup_driver, ns=__name__):
    LOG.debug("Getting backup strategy: %s" % backup_driver)
    return Strategy.get_strategy(backup_driver, ns)
