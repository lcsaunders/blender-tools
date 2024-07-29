#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# CONFIDENTIAL INFORMATION: This software is the confidential and proprietary
# information of Paramount Pictures Corporation (PPC).  This software may not
# be used, disclosed, reproduced or distributed for any purpose without prior
# written authorization and license from PPC. Reproduction of any section of
# this software must include this legend and all copyright notices.
#
# Copyright 2023 (c) Paramount Pictures Corporation. All rights reserved.
# ---------------------------------------------------------------------------
"""Lens kit for blender cameras."""

bl_info = {
    "name": "AVST Lens Kit",
    "description": "Create/change the lens for a camera",
    "author": "Lisa Curtis Saunders",
    "blender": (3, 1, 0),
    "version": (1, 1, 3),
    "category": "Camera"
}

import logging

import bpy

logger = logging.getLogger(__name__)


class LensBase(bpy.types.Operator):
    _lens = 18
    bl_description = 'Create/change the camera to the specified lens'
    bl_category = "AVST Lens Kit"

    def execute(self, context):
        logger.debug('setting lens to %s', self._lens)
        if context.scene.cam_bool:
            camName = 'new.shotcam'
            cam = bpy.data.cameras.new(camName)
            camObj = bpy.data.objects.new(camName, cam)
            context.scene.collection.objects.link(camObj)
            camObj.matrix_world = context.active_object.matrix_world
            # TODO: set new cam as active
            # for area in context.screen.areas:
            #     if area.type == "VIEW_3D":
            #         area.spaces[0].region_3d.view_perspective = 'CAMERA'
        else:
            cam = context.active_object.data

        cam.lens = self._lens
        return {'FINISHED'}


class ADD_OT_lens_18(LensBase):
    _lens = 18
    bl_idname = 'wm.lens_{}'.format(_lens)
    bl_label = "{} mm".format(_lens)


class ADD_OT_lens_22(LensBase):
    _lens = 22
    bl_idname = 'wm.lens_{}'.format(_lens)
    bl_label = "{} mm".format(_lens)


class ADD_OT_lens_35(LensBase):
    _lens = 35
    bl_idname = 'wm.lens_{}'.format(_lens)
    bl_label = "{} mm".format(_lens)


class ADD_OT_lens_55(LensBase):
    _lens = 55
    bl_idname = 'wm.lens_{}'.format(_lens)
    bl_label = "{} mm".format(_lens)


class ADD_OT_lens_72(LensBase):
    _lens = 72
    bl_idname = 'wm.lens_{}'.format(_lens)
    bl_label = "{} mm".format(_lens)


class ADD_OT_lens_85(LensBase):
    _lens = 85
    bl_idname = 'wm.lens_{}'.format(_lens)
    bl_label = "{} mm".format(_lens)


class ADD_OT_lens_100(LensBase):
    _lens = 100
    bl_idname = 'wm.lens_{}'.format(_lens)
    bl_label = "{} mm".format(_lens)


class ADD_OT_lens_135(LensBase):
    _lens = 135
    bl_idname = 'wm.lens_{}'.format(_lens)
    bl_label = "{} mm".format(_lens)


class ADD_MT_LENS_menu(bpy.types.Menu):
    bl_label = "Lenses"
    bl_idname = "ADD_MT_LENS_menu"

    def draw(self, context):
        layout = self.layout

        # Build drop down menu here
        layout.operator(ADD_OT_lens_18.bl_idname)
        layout.operator(ADD_OT_lens_22.bl_idname)
        layout.operator(ADD_OT_lens_35.bl_idname)
        layout.operator(ADD_OT_lens_55.bl_idname)
        layout.operator(ADD_OT_lens_72.bl_idname)
        layout.operator(ADD_OT_lens_85.bl_idname)
        layout.operator(ADD_OT_lens_100.bl_idname)
        layout.operator(ADD_OT_lens_135.bl_idname)


class ADD_PT_panel(bpy.types.Panel):
    bl_idname = "ADD_PT_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "AVST Lens Kit"
    bl_category = "AVST"

    @classmethod
    def poll(cls, context):
        return context.object and context.object.type == 'CAMERA'

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Choose a lens")
        row = layout.row()
        row.menu("ADD_MT_LENS_menu")
        row = layout.row()
        row.prop(context.scene, "cam_bool")


classes = (
    ADD_OT_lens_18,
    ADD_OT_lens_22,
    ADD_OT_lens_35,
    ADD_OT_lens_55,
    ADD_OT_lens_72,
    ADD_OT_lens_85,
    ADD_OT_lens_100,
    ADD_OT_lens_135,
    ADD_MT_LENS_menu,
    ADD_PT_panel
)


def register():
    bpy.types.Scene.cam_bool = bpy.props.BoolProperty(
        name="Create new camera",
        description="Make a new camera or update active camera",
        default=True
    )

    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister():
    from bpy.utils import unregister_class
    for cls in classes:
        unregister_class(cls)
    del bpy.types.Scene.cam_bool


if __name__ == "__main__":
    register()
