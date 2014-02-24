#    Copyright 2010-2011 OpenStack Foundation
#    Copyright 2013-2014 Rackspace Hosting
#    All Rights Reserved.
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

"""Model classes that form the core of instances functionality."""
from trove_guestagent.common import instance as tr_instance


class InstanceStatus(object):
    ACTIVE = "ACTIVE"
    BLOCKED = "BLOCKED"
    BUILD = "BUILD"
    FAILED = "FAILED"
    REBOOT = "REBOOT"
    RESIZE = "RESIZE"
    BACKUP = "BACKUP"
    SHUTDOWN = "SHUTDOWN"
    ERROR = "ERROR"
    RESTART_REQUIRED = "RESTART_REQUIRED"


class InstanceServiceStatus(object):
    _data_fields = ['instance_id', 'status_id', 'status_description',
                    'updated_at']

    def __init__(self, status, **kwargs):
        self.status = status
        kwargs["status_id"] = status.code
        kwargs["status_description"] = status.description
        self.set_status(status)

    def _validate(self, errors):
        if self.status is None:
            errors['status'] = "Cannot be none."
        if tr_instance.ServiceStatus.from_code(self.status_id) is None:
            errors['status_id'] = "Not valid."

    def get_status(self):
        return tr_instance.ServiceStatus.from_code(self.status_id)

    def set_status(self, value):
        self.status_id = value.code
        self.status_description = value.description
