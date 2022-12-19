# Copyright 2018-2022 The glTF-Blender-IO authors.
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

import typing
from io_scene_gltf2.blender.exp.gltf2_blender_gather_cache import cached
from .gltf2_blender_gather_keyframes import Keyframe
from .gltf2_blender_gather_animation_sampling_cache import get_bone_matrix
import numpy as np


@cached
def gather_bone_sampled_keyframes(
        armature_uuid: str,
        bone: str,
        channel: str,
        action_name: str,
        node_channel_is_animated: bool,
        export_settings
        ) -> typing.List[Keyframe]:

    start_frame = export_settings['ranges'][armature_uuid][action_name]['start']
    end_frame  = export_settings['ranges'][armature_uuid][action_name]['end']

    keyframes = []

    frame = start_frame
    step = export_settings['gltf_frame_step'] #TODOANIM to be tested correctly

    while frame <= end_frame:
        key = Keyframe(None, frame, channel) #TODOANIM first parameter not needed ... cf refactor of class Keyframe?

        mat = get_bone_matrix(
            armature_uuid,
            bone,
            channel,
            action_name,
            frame,
            step,
            export_settings
        )
        trans, rot, scale = mat.decompose()

        key.value = {
            "location": trans,
            "rotation_quaternion": rot,
            "scale": scale
            }[channel]

        keyframes.append(key)
        frame += step

    if not export_settings['gltf_optimize_animation']:
        return keyframes

    # For armatures
    # Check if all values are the same
    # In that case, if there is no real keyframe on this channel for this given bone,
    # We can ignore these keyframes
    # if there are some fcurve, we can keep only 2 keyframes, first and last
    cst = fcurve_is_constant(keyframes)

    if node_channel_is_animated is True: # fcurve on this bone for this property
            # Keep animation, but keep only 2 keyframes if data are not changing
            return [keyframes[0], keyframes[-1]] if cst is True and len(keyframes) >= 2 else keyframes
    else: # bone is not animated (no fcurve)
        # Not keeping if not changing property if user decided to not keep
        if export_settings['gltf_optimize_animation_keep_armature'] is False:
            return None if cst is True else keyframes
        else:
            # Keep at least 2 keyframes if data are not changing
            return [keyframes[0], keyframes[-1]] if cst is True and len(keyframes) >= 2 else keyframes

def fcurve_is_constant(keyframes):
    return all([j < 0.0001 for j in np.ptp([[k.value[i] for i in range(len(keyframes[0].value))] for k in keyframes], axis=0)])