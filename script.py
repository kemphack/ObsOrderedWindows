import obspython as obs
import lib
import myconverter
import typing
from contextlib import contextmanager

@contextmanager
def scene_enum(items):
	items = obs.obs_scene_enum_items(items)
	try:
		yield items
	finally:
		obs.sceneitem_list_release(items)

@contextmanager
def scene_ar(scene):
    scene = obs.obs_scene_from_source(scene)
    try:
        yield scene
    finally:
        obs.obs_scene_release(scene)

def update_windows():
	reorder()

def reorder():
	current_scene = obs.obs_frontend_get_current_scene()
	order = list()
	windows_in_order = lib.windows_ordered()
	with scene_ar(current_scene) as scene:
		with scene_enum(scene) as scene_items:
			for i, s in enumerate(scene_items):
				source = obs.obs_sceneitem_get_source(s)
				source_id = obs.obs_source_get_unversioned_id(source)
				if source_id == 'window_capture':
					properties = obs.obs_source_properties(source)
					handle = myconverter.void_to_window(obs.obs_properties_get_param(properties))
					order.append({"index": i, "scene_item": s, "z": windows_in_order.get(handle)})
	#sorting
	order = list(filter(lambda i: i["z"] != None, order))
	indexes = list(map(lambda i: i["index"], order))
	ordered = sorted(order, key=lambda i: -i["z"])

	for i, s in enumerate(ordered):
			obs.obs_sceneitem_set_order_position(s["scene_item"], indexes[i])

update_interval = 1000
obs.timer_add(update_windows, update_interval)
# ------------------------------------------------------------

def script_description():
	return "Updates windows' order."

# def script_update(settings):

# def script_defaults(settings):
	# obs.obs_data_set_default_int(settings, "interval", interval)

def script_properties():
	props = obs.obs_properties_create()

	return props
