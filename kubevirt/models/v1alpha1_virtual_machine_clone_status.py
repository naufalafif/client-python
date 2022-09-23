# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1alpha1VirtualMachineCloneStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'conditions': 'list[V1alpha1Condition]',
        'creation_time': 'K8sIoApimachineryPkgApisMetaV1Time',
        'phase': 'str',
        'restore_name': 'str',
        'snapshot_name': 'str',
        'target_name': 'str'
    }

    attribute_map = {
        'conditions': 'conditions',
        'creation_time': 'creationTime',
        'phase': 'phase',
        'restore_name': 'restoreName',
        'snapshot_name': 'snapshotName',
        'target_name': 'targetName'
    }

    def __init__(self, conditions=None, creation_time=None, phase=None, restore_name=None, snapshot_name=None, target_name=None):
        """
        V1alpha1VirtualMachineCloneStatus - a model defined in Swagger
        """

        self._conditions = None
        self._creation_time = None
        self._phase = None
        self._restore_name = None
        self._snapshot_name = None
        self._target_name = None

        if conditions is not None:
          self.conditions = conditions
        if creation_time is not None:
          self.creation_time = creation_time
        if phase is not None:
          self.phase = phase
        if restore_name is not None:
          self.restore_name = restore_name
        if snapshot_name is not None:
          self.snapshot_name = snapshot_name
        if target_name is not None:
          self.target_name = target_name

    @property
    def conditions(self):
        """
        Gets the conditions of this V1alpha1VirtualMachineCloneStatus.

        :return: The conditions of this V1alpha1VirtualMachineCloneStatus.
        :rtype: list[V1alpha1Condition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions of this V1alpha1VirtualMachineCloneStatus.

        :param conditions: The conditions of this V1alpha1VirtualMachineCloneStatus.
        :type: list[V1alpha1Condition]
        """

        self._conditions = conditions

    @property
    def creation_time(self):
        """
        Gets the creation_time of this V1alpha1VirtualMachineCloneStatus.

        :return: The creation_time of this V1alpha1VirtualMachineCloneStatus.
        :rtype: K8sIoApimachineryPkgApisMetaV1Time
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """
        Sets the creation_time of this V1alpha1VirtualMachineCloneStatus.

        :param creation_time: The creation_time of this V1alpha1VirtualMachineCloneStatus.
        :type: K8sIoApimachineryPkgApisMetaV1Time
        """

        self._creation_time = creation_time

    @property
    def phase(self):
        """
        Gets the phase of this V1alpha1VirtualMachineCloneStatus.

        :return: The phase of this V1alpha1VirtualMachineCloneStatus.
        :rtype: str
        """
        return self._phase

    @phase.setter
    def phase(self, phase):
        """
        Sets the phase of this V1alpha1VirtualMachineCloneStatus.

        :param phase: The phase of this V1alpha1VirtualMachineCloneStatus.
        :type: str
        """

        self._phase = phase

    @property
    def restore_name(self):
        """
        Gets the restore_name of this V1alpha1VirtualMachineCloneStatus.

        :return: The restore_name of this V1alpha1VirtualMachineCloneStatus.
        :rtype: str
        """
        return self._restore_name

    @restore_name.setter
    def restore_name(self, restore_name):
        """
        Sets the restore_name of this V1alpha1VirtualMachineCloneStatus.

        :param restore_name: The restore_name of this V1alpha1VirtualMachineCloneStatus.
        :type: str
        """

        self._restore_name = restore_name

    @property
    def snapshot_name(self):
        """
        Gets the snapshot_name of this V1alpha1VirtualMachineCloneStatus.

        :return: The snapshot_name of this V1alpha1VirtualMachineCloneStatus.
        :rtype: str
        """
        return self._snapshot_name

    @snapshot_name.setter
    def snapshot_name(self, snapshot_name):
        """
        Sets the snapshot_name of this V1alpha1VirtualMachineCloneStatus.

        :param snapshot_name: The snapshot_name of this V1alpha1VirtualMachineCloneStatus.
        :type: str
        """

        self._snapshot_name = snapshot_name

    @property
    def target_name(self):
        """
        Gets the target_name of this V1alpha1VirtualMachineCloneStatus.

        :return: The target_name of this V1alpha1VirtualMachineCloneStatus.
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        """
        Sets the target_name of this V1alpha1VirtualMachineCloneStatus.

        :param target_name: The target_name of this V1alpha1VirtualMachineCloneStatus.
        :type: str
        """

        self._target_name = target_name

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1alpha1VirtualMachineCloneStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
