# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
  "name" : "Json Hierarchy (json)",
  "author" : "AnhHC - haconganh@gmail.com",
  "description" : "Exports hierarchy data of blender project to json format",
  "blender" : (3, 3, 10),
  "version" : (1, 0, 0),
  "location" : "Exporter",
  "warning" : "",
  "category" : "Exporter"
}


import bpy
import json
import random

context = bpy.context
#coll = context.collection
#ob = context.object

def listMeshesFromCollection(colName, json_meshes_object, mesh_detail_objects, level, parentId, levelChar):
    
    json_mesh_detail_object = {}
    k = 0
    for obj in bpy.data.collections[colName].all_objects:
        if (obj.type == 'MESH'):
            print(levelChar + obj.name + " - " + obj.type)
            
            id = random.randint(10000, 99999) + parentId + 1 + k
            k += 1
            
            json_mesh_struct_object = {}
            json_mesh_struct_object["id"] = id
            json_mesh_struct_object["parentId"] = parentId
            json_mesh_struct_object["name"] = obj.name
            json_mesh_struct_object["displayName"] = obj.name.split("_")[-1]
            json_mesh_struct_object["parent"] = colName
            json_mesh_struct_object["level"] = level + 1
            json_mesh_struct_object["defaultOnOff"] = "off"
            
            json_mesh_detail_object = {}
            json_mesh_detail_object["id"] = id
            json_mesh_detail_object["parentId"] = parentId
            json_mesh_detail_object["name"] = obj.name
            json_mesh_detail_object["displayName"] = obj.name.split("_")[-1]
            json_mesh_detail_object["parent"] = colName
            json_mesh_detail_object["level"] = level + 1
            json_mesh_detail_object["defaultOnOff"] = "off"
            
            json_mesh_detail_object["eCommerceProductImage"] = ""
            json_mesh_detail_object["defaultColor"] = ""
            json_mesh_detail_object["selectedColor"] = ""
            
            if (obj.name.startswith("TL") or obj.name.startswith("TR") 
                or obj.name.startswith("BL") or obj.name.startswith("BR")):
                json_mesh_struct_object["target"] = obj.name.split("_")[0]
                json_mesh_detail_object["target"] = obj.name.split("_")[0]
                
            else:
                json_mesh_struct_object["target"] = "base"
                json_mesh_detail_object["target"] = "base"
            
            if ("_Classic" in colName):
                colorOption = [
                    {
                        "id": random.randint(10000000, 99999999) + parentId + 1 + k,
                        "grandParentId": parentId,
                        "parentId": id,
                        "name": "14K White",
                        "target": obj.name.split("_")[0],
                        "level": level + 2,
                        "colorCode": "0xefefef",
                        "eCommerceVariantOptionId": "",
                        "price": 5.0
                    },
                    {
                        "id": random.randint(10000000, 99999999) + parentId + 1 + k,
                        "grandParentId": parentId,
                        "parentId": id,
                        "name": "14K Rose",
                        "target": obj.name.split("_")[0],
                        "level": level + 2,
                        "colorCode": "0xffb8a3",
                        "eCommerceVariantOptionId": "",
                        "price": 5.0
                    },
                    {
                        "id": random.randint(10000000, 99999999) + parentId + 1 + k,
                        "grandParentId": parentId,
                        "parentId": id,
                        "name": "14K Yellow",
                        "target": obj.name.split("_")[0],
                        "level": level + 2,
                        "colorCode": "0xffe374",
                        "eCommerceVariantOptionId": "",
                        "price": 5.0
                    },
                    {
                        "id": random.randint(10000000, 99999999) + parentId + 1 + k,
                        "grandParentId": parentId,
                        "parentId": id,
                        "name": "18K Yellow",
                        "target": obj.name.split("_")[0],
                        "level": level + 2,
                        "colorCode": "0xfece28",
                        "eCommerceVariantOptionId": "",
                        "price": 5.0
                    },
                    {
                        "id": random.randint(10000000, 99999999) + parentId + 1 + k,
                        "grandParentId": parentId,
                        "parentId": id,
                        "name": "18K White",
                        "target": obj.name.split("_")[0],
                        "level": level + 2,
                        "colorCode": "0xcccccc",
                        "eCommerceVariantOptionId": "",
                        "price": 5.0
                    },
                    {
                        "id": random.randint(10000000, 99999999) + parentId + 1 + k,
                        "grandParentId": parentId,
                        "parentId": id,
                        "name": "18K Rose",
                        "target": obj.name.split("_")[0],
                        "level": level + 2,
                        "colorCode": "0xffa286",
                        "eCommerceVariantOptionId": "",
                        "price": 5.0
                    },
                ]
                
                json_mesh_detail_object["colorOption"] = colorOption
                json_mesh_struct_object["colorOption"] = colorOption
                json_mesh_detail_object["componentType"] = "Classic"
                json_mesh_struct_object["componentType"] = "Classic"
            elif ("_Pave" in colName):
                colorOption = [
                    {
                        "id": random.randint(10000000, 99999999) + parentId + 1 + k,
                        "grandParentId": parentId,
                        "parentId": id,
                        "name": "Diamond",
                        "type": "Diamond",
                        "target": obj.name.split("_")[0],
                        "level": level + 2,
                        "colorCode": "0xe7fcff",
                        "eCommerceVariantOptionId": "",
                        "price": 5.0
                    },
                    {
                        "id": random.randint(10000000, 99999999) + parentId + 1 + k,
                        "grandParentId": parentId,
                        "parentId": id,
                        "name": "Ruby",
                        "type": "Diamond",
                        "target": obj.name.split("_")[0],
                        "level": level + 2,
                        "colorCode": "0xb20011",
                        "eCommerceVariantOptionId": "",
                        "price": 5.0
                    },
                    {
                        "id": random.randint(10000000, 99999999) + parentId + 1 + k,
                        "grandParentId": parentId,
                        "parentId": id,
                        "name": "Sapphire",
                        "type": "Diamond",
                        "target": obj.name.split("_")[0],
                        "level": level + 2,
                        "colorCode": "0x223de0",
                        "eCommerceVariantOptionId": "",
                        "price": 5.0
                    },
                    {
                        "id": random.randint(10000000, 99999999) + parentId + 1 + k,
                        "grandParentId": parentId,
                        "parentId": id,
                        "name": "Emerald",
                        "type": "Diamond",
                        "target": obj.name.split("_")[0],
                        "level": level + 2,
                        "colorCode": "0x17dc59",
                        "eCommerceVariantOptionId": "",
                        "price": 5.0
                    },
                    {
                        "id": random.randint(10000000, 99999999) + parentId + 1 + k,
                        "grandParentId": parentId,
                        "parentId": id,
                        "name": "Black",
                        "type": "Diamond",
                        "target": obj.name.split("_")[0],
                        "level": level + 2,
                        "colorCode": "0x000000",
                        "eCommerceVariantOptionId": "",
                        "price": 5.0
                    },
                    {
                        "id": random.randint(10000000, 99999999) + parentId + 1 + k,
                        "grandParentId": parentId,
                        "parentId": id,
                        "name": "Purple",
                        "type": "Diamond",
                        "target": obj.name.split("_")[0],
                        "level": level + 2,
                        "colorCode": "0x800080",
                        "eCommerceVariantOptionId": "",
                        "price": 5.0
                    },
                    {
                        "id": random.randint(10000000, 99999999) + parentId + 1 + k,
                        "grandParentId": parentId,
                        "parentId": id,
                        "name": "Pink",
                        "type": "Diamond",
                        "target": obj.name.split("_")[0],
                        "level": level + 2,
                        "colorCode": "0xFFC0CB",
                        "eCommerceVariantOptionId": "",
                        "price": 5.0
                    },
                    {
                        "id": random.randint(10000000, 99999999) + parentId + 1 + k,
                        "grandParentId": parentId,
                        "parentId": id,
                        "name": "Yellow",
                        "type": "Diamond",
                        "target": obj.name.split("_")[0],
                        "level": level + 2,
                        "colorCode": "0xFFFF00",
                        "eCommerceVariantOptionId": "",
                        "price": 5.0
                    },
                ]
                
                json_mesh_detail_object["colorOption"] = colorOption
                json_mesh_struct_object["colorOption"] = colorOption
                json_mesh_detail_object["componentType"] = "Diamond"
                json_mesh_struct_object["componentType"] = "Diamond"
            else:
                json_mesh_detail_object["colorOption"] = []
                json_mesh_struct_object["colorOption"] = []
                json_mesh_detail_object["componentType"] = ""
                json_mesh_struct_object["componentType"] = ""
            mesh_detail_objects.append(json_mesh_detail_object)
            json_meshes_object.append(json_mesh_struct_object)
            
#        if (obj.type == 'MESH'):
#            print(bpy.data.meshes)
#            for key, value in obj.items():
#                print(str(key) + " - " + str(value))
                

def parentCol(_colParent, json_object, mesh_detail_objects, level, parentId, levelChar):
    print("", end='')
    k = 0        
    for col in _colParent.children:
#        newObj = bpy.data.objects.new("empty", None)
#        bpy.context.scene.collection.objects.link(newObj)
#        newObj.name = col.name
#        newObj.parent = _objParent
        id = (random.randint(100000000, 999999999) if parentId is None else parentId) + 1 + k
        k += 1
        json_sub_object = {}
        json_sub_object["id"] = id
        json_sub_object["parentId"] = parentId
        json_sub_object["name"] = col.name
        json_sub_object["displayName"] = col.name.split("_")[-1]
        json_sub_object["parent"] = _colParent.name
        json_sub_object["defaultOnOff"] = "on"
        json_sub_object["level"] = level
        
        if (col.name.startswith("TL") or col.name.startswith("TR") 
            or col.name.startswith("BL") or col.name.startswith("BR")):
            json_sub_object["target"] = col.name.split("_")[0]
        else:
            json_sub_object["target"] = "base"
        
        
        json_meshes_object = []
        json_child_object = []
        
        print(levelChar + col.name)
    
        if len(col.objects) > 0:
            objs = col.objects
        
            listMeshesFromCollection(col.name, json_meshes_object, mesh_detail_objects, level, id, levelChar + " [Mesh] ")
            json_sub_object["childs"] = []
            json_sub_object["meshes"] = json_meshes_object
#            for obj in objs:
#                obj.parent = newObj
        else:
            parentCol(col, json_child_object, mesh_detail_objects, level + 1, id, levelChar + " > ")
            json_sub_object["childs"] = json_child_object
            json_sub_object["meshes"] = []
        
        json_object.append(json_sub_object)
            

def write_json_hierarchy_data(context, filepath, use_some_setting):
    print("running write_json_hierarchy_data...")
    # print all objects
    
#    root = bpy.data.objects.new("empty", None)
#    bpy.context.scene.collection.objects.link(root)
#    root.name = sCollection.name
    
    sCollection = bpy.context.collection

    json_object =  []
    mesh_detail_objects = []
    parentId = None

    parentCol(sCollection, json_object, mesh_detail_objects, 1, parentId, " > ")
    
    all_objects = {"hierarchy": json_object, "meshes" : mesh_detail_objects}
    
    
#    print(list(root.name))
    print("End running write_json_hierarchy_data...")
    
    
    f = open(filepath, 'w', encoding='utf-8')
    f.write(json.dumps(all_objects, indent=4))
    f.write("\n")
    f.close()

    return {'FINISHED'}


# ExportHelper is a helper class, defines filename and
# invoke() function which calls the file selector.
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy.types import Operator


class ExportJsonHierarchyData(Operator, ExportHelper):
    """This appears in the tooltip of the operator and in the generated docs"""
    bl_idname = "exporter.json_hierarchy_exporter"  # important since its how bpy.ops.import_test.some_data is constructed
    bl_label = "Json Hierarchy (json)"

    # ExportHelper mixin class uses this
    filename_ext = ".json"

    filter_glob: StringProperty(
        default="*.json",
        options={'HIDDEN'},
        maxlen=255,  # Max internal buffer length, longer would be clamped.
    )

    # List of operator properties, the attributes will be assigned
    # to the class instance from the operator settings before calling.
    use_setting: BoolProperty(
        name="Custom properties",
        description="Export custom properties",
        default=True,
    )

    type: EnumProperty(
        name="Export options",
        description="Choose between items",
        items=(
            ('OPT_MESH', "With meshes", "Export with meshes information"),
            ('OPT_NO_MESH', "Without meshes", "Export without meshes information"),
        ),
        default='OPT_MESH',
    )

    def execute(self, context):
        return write_json_hierarchy_data(context, self.filepath, self.use_setting)


# Only needed if you want to add into a dynamic menu
def menu_func_export(self, context):
    self.layout.operator(ExportJsonHierarchyData.bl_idname, text="Json Hierarchy (json)")


# Register and add to the "file selector" menu (required to use F3 search "Text Export Operator" for quick access).
def register():
    bpy.utils.register_class(ExportJsonHierarchyData)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)


def unregister():
    bpy.utils.unregister_class(ExportJsonHierarchyData)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)


if __name__ == "__main__":
    register()

    # test call
    bpy.ops.exporter.json_hierarchy_exporter('INVOKE_DEFAULT')
