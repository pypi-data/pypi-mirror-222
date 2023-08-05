# Copyright (c) 2016 Mirantis, Inc.
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

import abc


class EventHandler(object, metaclass=abc.ABCMeta):
    """Base class for event handlers."""

    @abc.abstractmethod
    def __call__(self, event, *args, **kwargs):
        """Handle the event."""
        raise NotImplementedError()

    def __str__(self):
        return self.__class__.__name__
