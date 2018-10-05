# Copyright (c) 2017 The Khronos Group Inc.
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

from enum import Enum, IntEnum


class ComponentType(IntEnum):
    Byte = 5120
    UnsignedByte = 5121
    Short = 5122
    UnsignedShort = 5123
    UnsignedInt = 5125
    Float = 5126

    @classmethod
    def to_type_code(cls, component_type):
        return {
            ComponentType.Byte: 'b',
            ComponentType.UnsignedByte: 'B',
            ComponentType.Short: 'h',
            ComponentType.UnsignedShort: 'H',
            ComponentType.UnsignedInt: 'I',
            ComponentType.Float: 'f'
        }[component_type]

    @classmethod
    def from_legacy_define(cls, type_define):
        return {
            GLTF_COMPONENT_TYPE_BYTE: ComponentType.Byte,
            GLTF_COMPONENT_TYPE_UNSIGNED_BYTE: ComponentType.UnsignedByte,
            GLTF_COMPONENT_TYPE_SHORT: ComponentType.Short,
            GLTF_COMPONENT_TYPE_UNSIGNED_SHORT: ComponentType.UnsignedShort,
            GLTF_COMPONENT_TYPE_UNSIGNED_INT: ComponentType.UnsignedInt,
            GLTF_COMPONENT_TYPE_FLOAT: ComponentType.Float
        }[type_define]

    @classmethod
    def get_size(cls, component_type):
        return {
            ComponentType.Byte: 1,
            ComponentType.UnsignedByte: 1,
            ComponentType.Short: 2,
            ComponentType.UnsignedShort: 2,
            ComponentType.UnsignedInt: 4,
            ComponentType.Float: 4
        }[component_type]


class DataType:
    Scalar = "SCALAR"
    Vec2 = "VEC2"
    Vec3 = "VEC3"
    Vec4 = "VEC4"
    Mat2 = "MAT2"
    Mat3 = "MAT3"
    Mat4 = "MAT4"

    @classmethod
    def num_elements(cls, data_type):
        return {
            DataType.Scalar: 1,
            DataType.Vec2: 2,
            DataType.Vec3: 3,
            DataType.Vec4: 4,
            DataType.Mat2: 4,
            DataType.Mat3: 9,
            DataType.Mat4: 16
        }[data_type]


#################
# LEGACY DEFINES

GLTF_VERSION = "2.0"

#
# Component Types
#
GLTF_COMPONENT_TYPE_BYTE = "BYTE"
GLTF_COMPONENT_TYPE_UNSIGNED_BYTE = "UNSIGNED_BYTE"
GLTF_COMPONENT_TYPE_SHORT = "SHORT"
GLTF_COMPONENT_TYPE_UNSIGNED_SHORT = "UNSIGNED_SHORT"
GLTF_COMPONENT_TYPE_UNSIGNED_INT = "UNSIGNED_INT"
GLTF_COMPONENT_TYPE_FLOAT = "FLOAT"


#
# Data types
#
GLTF_DATA_TYPE_SCALAR = "SCALAR"
GLTF_DATA_TYPE_VEC2 = "VEC2"
GLTF_DATA_TYPE_VEC3 = "VEC3"
GLTF_DATA_TYPE_VEC4 = "VEC4"
GLTF_DATA_TYPE_MAT2 = "MAT2"
GLTF_DATA_TYPE_MAT3 = "MAT3"
GLTF_DATA_TYPE_MAT4 = "MAT4"


