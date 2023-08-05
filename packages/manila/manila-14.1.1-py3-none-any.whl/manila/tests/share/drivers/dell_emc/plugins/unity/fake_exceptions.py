# Copyright (c) 2016 EMC Corporation.
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


class UnityFakeException(Exception):
    pass


class UnityException(UnityFakeException):
    pass


class UnitySmbShareNameExistedError(UnityException):
    pass


class UnityFileSystemNameAlreadyExisted(UnityException):
    pass


class UnityNasServerNameUsedError(UnityException):
    pass


class UnityNfsShareNameExistedError(UnityException):
    pass


class UnitySnapNameInUseError(UnityException):
    pass


class UnityIpAddressUsedError(UnityException):
    pass


class UnityResourceNotFoundError(UnityException):
    pass


class UnityOneDnsPerNasServerError(UnityException):
    pass


class UnitySmbNameInUseError(UnityException):
    pass


class UnityNfsAlreadyEnabledError(UnityException):
    pass


class UnityHostNotFoundException(UnityException):
    pass


class UnityNothingToModifyError(UnityException):
    pass


class UnityShareShrinkSizeTooSmallError(UnityException):
    pass


class UnityTenantNameInUseError(UnityException):
    pass


class UnityVLANUsedByOtherTenantError(UnityException):
    pass


class SystemAPINotSupported(UnityException):
    pass


class UnityVLANAlreadyHasInterfaceError(UnityException):
    pass


class UnityAclUserNotFoundError(UnityException):
    pass
