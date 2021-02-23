import obspython as obs
import urllib.request
import urllib.error
import win32gui
import lib
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
	# sources = obs.obs_enum_sources()
	# print('new update')
	# print(sources)
	# print('ids')
	# if sources is not None:
	# 	for source in sources:
	# 		source_id = obs.obs_source_get_unversioned_id(source)
	# 		if source_id == 'window_cupture':
	# 			print(source)

	# 	obs.source_list_release(sources)
	reorder()

def reorder():
	current_scene = obs.obs_frontend_get_current_scene()
	order = list()
	with scene_ar(current_scene) as scene:
		with scene_enum(scene) as scene_items:
			for i, s in enumerate(scene_items):
				source = obs.obs_sceneitem_get_source(s)
				name = obs.obs_source_get_name(source)
				source_id = obs.obs_source_get_unversioned_id(source)
				if source_id == 'window_capture':
					settings = obs.obs_source_get_settings(source)
					window_name = obs.obs_data_get_string(settings, "window")
					decoded_name = lib.decode_string(window_name.split(':')[0])
					print(decoded_name)
					print(win32gui.FindWindow(None, decoded_name))
					order.append({"index": i, "name": name, "scene_item": s})
				# change second index with pre last
				# order[1]["index"], order[-2]["index"] = (
				# 		order[-2]["index"],
				# 		order[1]["index"],
				# )
				# for s in sorted(order, key=lambda i: i["index"]):
				# 		obs.obs_sceneitem_set_order_position(s["scene_item"], s["index"])
	print(order)

interval = 5
obs.timer_add(update_windows, interval * 1000)
# ------------------------------------------------------------

def script_description():
	return "Updates windows' order."

# def script_update(settings):
	

def script_defaults(settings):
	obs.obs_data_set_default_int(settings, "interval", interval)

def script_properties():
	props = obs.obs_properties_create()

	# obs.obs_properties_add_text(props, "url", "URL", obs.OBS_TEXT_DEFAULT)
	# obs.obs_properties_add_int(props, "interval", "Update Interval (seconds)", 5, 3600, 1)

	# p = obs.obs_properties_add_list(props, "source", "Text Source", obs.OBS_COMBO_TYPE_EDITABLE, obs.OBS_COMBO_FORMAT_STRING)
	# sources = obs.obs_enum_sources()
	# if sources is not None:
	# 	for source in sources:
	# 		source_id = obs.obs_source_get_unversioned_id(source)
	# 		if source_id == "text_gdiplus" or source_id == "text_ft2_source":
	# 			name = obs.obs_source_get_name(source)
	# 			obs.obs_property_list_add_string(p, name, name)

	# 	obs.source_list_release(sources)
	# sources = obs.obs_enum_sources()
	# print(sources)
	# if sources is not None:
	# 	for source in sources:
	# 		source_id = obs.obs_source_get_unversioned_id(source)
	# 		print(source_id)

	# 	obs.source_list_release(sources)

	# obs.obs_properties_add_button(props, "button", "Refresh", refresh_pressed)
	return props
