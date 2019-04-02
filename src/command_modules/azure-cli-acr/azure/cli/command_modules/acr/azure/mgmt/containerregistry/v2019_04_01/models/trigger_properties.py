# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TriggerProperties(Model):
    """The properties of a trigger.

    :param source_triggers: The collection of triggers based on source code
     repository.
    :type source_triggers:
     list[~azure.mgmt.containerregistry.v2019_04_01.models.SourceTrigger]
    :param base_image_trigger: The trigger based on base image dependencies.
    :type base_image_trigger:
     ~azure.mgmt.containerregistry.v2019_04_01.models.BaseImageTrigger
    """

    _attribute_map = {
        'source_triggers': {'key': 'sourceTriggers', 'type': '[SourceTrigger]'},
        'base_image_trigger': {'key': 'baseImageTrigger', 'type': 'BaseImageTrigger'},
    }

    def __init__(self, source_triggers=None, base_image_trigger=None):
        super(TriggerProperties, self).__init__()
        self.source_triggers = source_triggers
        self.base_image_trigger = base_image_trigger
