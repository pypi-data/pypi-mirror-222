########################################################################
# ERROR CATCHES AND LOGGING FOR CLARITY WHEN USING CENTERLINE-WIDTH
########################################################################

# Built in Python functions
import logging
from io import StringIO

# Internal centerline_width reference to access functions, global variables, and error handling
import centerline_width

## Logging set up for .CRITICAL
logger = logging.getLogger(__name__)
logger.setLevel(logging.CRITICAL)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

centerline_type_options = ["Voronoi", "Evenly Spaced", "Smoothed", "Equal Distance"]

## Error Handling: preprocessing.py
def errrorHandlingConvertColumnsToCSV(text_file=None,
									flipBankDirection=None):
	# Error handling for convertColumnsToCSV()
	if text_file is None:
		logger.critical("\nCRITICAL ERROR, [text_file]: Requires text file")
		exit()
	else:
		if type(text_file) != str:
			logger.critical("\nCRITICAL ERROR, [text_file]: Must be a str, current type = '{0}'".format(type(text_file)))
			exit()
		else:
			if not text_file.lower().endswith(".txt"):
				logger.critical("\nCRITICAL ERROR, [text_file]: Extension must be a .txt file, current extension = '{0}'".format(text_file.split(".")[1]))
				exit()

	if type(flipBankDirection) != bool:
		logger.critical("\nCRITICAL ERROR, [flipBankDirection]: Must be a bool, current type = '{0}'".format(type(flipBankDirection)))
		exit()

## Error Handling: plotDiagrams.py
def errorHandlingPlotCenterline(river_object=None,
								centerline_type=None,
								marker_type=None,
								centerline_color=None,
								display_all_possible_paths=None,
								plot_title=None,
								save_plot_name=None,
								display_voronoi=None,
								coordinate_type=None):
	# Error handling for plotCenterline()
	if river_object is None:
		logger.critical("\nCRITICAL ERROR, [river_object]: Requires a river object (see: centerline_width.riverCenterline)")
		exit()
	else:
		if not isinstance(river_object, centerline_width.riverCenterline):
			logger.critical("\nCRITICAL ERROR, [river_object]: Must be a river object (see: centerline_width.riverCenterline), current type = '{0}'".format(type(river_object)))
			exit()

	if type(centerline_type) != str:
		logger.critical("\nCRITICAL ERROR, [centerline_type]: Must be a str, current type = '{0}'".format(type(centerline_type)))
		exit()
	else:
		if centerline_type.title() not in centerline_type_options:
			logger.critical("\nCRITICAL ERROR, [centerline_type]: Must be an available option in {0}, current option = '{1}'".format(centerline_type_options, centerline_type))
			exit()

	if type(marker_type) != str:
		logger.critical("\nCRITICAL ERROR, [marker_type]: Must be a str, current type = '{0}'".format(type(marker_type)))
		exit()
	else:
		marker_type_options = ["Line", "Scatter"]
		if marker_type.title() not in marker_type_options:
			logger.critical("\nCRITICAL ERROR, [marker_type]: Must be an available option in {0}, current option = '{1}'".format(marker_type_options, marker_type))
			exit()

	if type(centerline_color) != str:
		logger.critical("\nCRITICAL ERROR, [centerline_color]: Must be a str, current type = '{0}'".format(type(centerline_color)))
		exit()

	if type(display_all_possible_paths) != bool:
		logger.critical("\nCRITICAL ERROR, [display_all_possible_paths]: Must be a bool, current type = '{0}'".format(type(display_all_possible_paths)))
		exit()

	if plot_title is not None and type(plot_title) != str:
		logger.critical("\nCRITICAL ERROR, [plot_title]: Must be a str, current type = '{0}'".format(type(plot_title)))
		exit()

	if save_plot_name is not None and type(save_plot_name) != str:
		logger.critical("\nCRITICAL ERROR, [save_plot_name]: Must be a str, current type = '{0}'".format(type(save_plot_name)))
		exit()

	if type(display_voronoi) != bool:
		logger.critical("\nCRITICAL ERROR, [display_voronoi]: Must be a bool, current type = '{0}'".format(type(display_voronoi)))
		exit()

	if type(coordinate_type) != str:
		logger.critical("\nCRITICAL ERROR, [coordinate_type]: Must be a str, current type = '{0}'".format(type(coordinate_type)))
		exit()
	else:
		coordinate_type_options = ["Decimal Degrees", "Relative Distance"]
		if coordinate_type.title() not in coordinate_type_options:
			logger.critical("\nCRITICAL ERROR, [coordinate_type]: Must be an available option in {0}, current option = '{1}'".format(coordinate_type_options, coordinate_type))
			exit()

def errorHandlingPlotCenterlineWidth(river_object=None,
									plot_title=None,
									save_plot_name=None,
									display_true_centerline=None,
									transect_span_distance=None,
									apply_smoothing=None,
									flag_intersections=None,
									remove_intersections=None,
									coordinate_type=None):
	# Error handling for plotCenterlineWidth()
	if river_object is None:
		logger.critical("\nCRITICAL ERROR, [river_object]: Requires a river object (see: centerline_width.riverCenterline)")
		exit()
	else:
		if not isinstance(river_object, centerline_width.riverCenterline):
			logger.critical("\nCRITICAL ERROR, [river_object]: Must be a river object (see: centerline_width.riverCenterline), current type = '{0}'".format(type(river_object)))
			exit()

	if plot_title is not None and type(plot_title) != str:
		logger.critical("\nCRITICAL ERROR, [plot_title]: Must be a str, current type = '{0}'".format(type(plot_title)))
		exit()

	if save_plot_name is not None and type(save_plot_name) != str:
		logger.critical("\nCRITICAL ERROR, [save_plot_name]: Must be a str, current type = '{0}'".format(type(save_plot_name)))
		exit()

	if type(display_true_centerline) != bool:
		logger.critical("\nCRITICAL ERROR, [display_true_centerline]: Must be a bool, current type = '{0}'".format(type(display_true_centerline)))
		exit()

	if type(transect_span_distance) != int:
		logger.critical("\nCRITICAL ERROR, [transect_span_distance]: Must be a int, current type = '{0}'".format(type(transect_span_distance)))
		exit()
	else:
		if transect_span_distance < 3:
			logger.critical("\nCRITICAL ERROR, [transect_span_distance]: Must be a greater than 2 to find the slope between at least two points, currently = '{0}'".format(transect_span_distance))
			exit()

	if apply_smoothing is not None:
		if type(apply_smoothing) != bool:
			logger.critical("\nCRITICAL ERROR, [apply_smoothing]: Must be a bool, current type = '{0}'".format(type(apply_smoothing)))
			exit()
	
	if type(flag_intersections) != bool:
		logger.critical("\nCRITICAL ERROR, [flag_intersections]: Must be a bool, current type = '{0}'".format(type(flag_intersections)))
		exit()

	if type(remove_intersections) != bool:
		logger.critical("\nCRITICAL ERROR, [remove_intersections]: Must be a bool, current type = '{0}'".format(type(remove_intersections)))
		exit()

	if type(coordinate_type) != str:
		logger.critical("\nCRITICAL ERROR, [coordinate_type]: Must be a str, current type = '{0}'".format(type(coordinate_type)))
		exit()
	else:
		coordinate_type_options = ["Decimal Degrees", "Relative Distance"]
		if coordinate_type.title() not in coordinate_type_options:
			logger.critical("\nCRITICAL ERROR, [coordinate_type]: Must be an available option in {0}, current option = '{1}'".format(coordinate_type_options, coordinate_type))
			exit()

## Error Handling: centerline.py
def errorHandlingRiverWidthFromCenterline(river_object=None,
										transect_span_distance=None,
										apply_smoothing=None,
										remove_intersections=None,
										coordinate_type=None,
										save_to_csv=None):
	# Error Handling for riverWidthFromCenterline()
	if river_object is None:
		logger.critical("\nCRITICAL ERROR, [river_object]: Requires a river object (see: centerline_width.riverCenterline)")
		exit()
	else:
		if not isinstance(river_object, centerline_width.riverCenterline):
			logger.critical("\nCRITICAL ERROR, [river_object]: Must be a river object (see: centerline_width.riverCenterline), current type = '{0}'".format(type(river_object)))
			exit()

	if transect_span_distance is not None:
		if type(transect_span_distance) != int:
			logger.critical("\nCRITICAL ERROR, [transect_span_distance]: Must be a int, current type = '{0}'".format(type(transect_span_distance)))
			exit()
		else:
			if transect_span_distance < 3:
				logger.critical("\nCRITICAL ERROR, [transect_span_distance]: Must be greater than 2, currently = '{0}'".format(transect_span_distance))
				exit()

	if type(apply_smoothing) != bool:
		logger.critical("\nCRITICAL ERROR, [apply_smoothing]: Must be a bool, current type = '{0}'".format(type(apply_smoothing)))
		exit()

	if type(remove_intersections) != bool:
		logger.critical("\nCRITICAL ERROR, [remove_intersections]: Must be a bool, current type = '{0}'".format(type(remove_intersections)))
		exit()

	if type(coordinate_type) != str:
		logger.critical("\nCRITICAL ERROR, [coordinate_type]: Must be a str, current type = '{0}'".format(type(coordinate_type)))
		exit()
	else:
		coordinate_type_options = ["Decimal Degrees", "Relative Distance"]
		if coordinate_type.title() not in coordinate_type_options:
			logger.critical("\nCRITICAL ERROR, [coordinate_type]: Must be an available option in {0}, current option = '{1}'".format(coordinate_type_options, coordinate_type))
			exit()

	if save_to_csv is not None:
		if type(save_to_csv) != str:
			logger.critical("\nCRITICAL ERROR, [save_to_csv]: Must be a str, current type = '{0}'".format(type(save_to_csv)))
			exit()
		if not save_to_csv.lower().endswith(".csv"):
			logger.critical("\nCRITICAL ERROR, [save_to_csv]: Extension must be a .csv file, current extension = '{0}'".format(save_to_csv.split(".")[1]))
			exit()

def errorHandlingSaveCenterlineCSV(river_object=None,
								latitude_header=None,
								longitude_header=None,
								save_to_csv=None,
								centerline_type=None,
								coordinate_type=None):
	# Error Handling for saveCenterlineCSV()
	if river_object is None:
		logger.critical("\nCRITICAL ERROR, [river_object]: Requires a river object (see: centerline_width.riverCenterline)")
		exit()
	else:
		if not isinstance(river_object, centerline_width.riverCenterline):
			logger.critical("\nCRITICAL ERROR, [river_object]: Must be a river object (see: centerline_width.riverCenterline), current type = '{0}'".format(type(river_object)))
			exit()

	if latitude_header is not None and type(latitude_header) != str:
		logger.critical("\nCRITICAL ERROR, [latitude_header]: Must be a str, current type = '{0}'".format(type(latitude_header)))
		exit()

	if longitude_header is not None and type(longitude_header) != str:
		logger.critical("\nCRITICAL ERROR, [longitude_header]: Must be a str, current type = '{0}'".format(type(longitude_header)))
		exit()

	if save_to_csv is None:
		logger.critical("\nCRITICAL ERROR, [save_to_csv]: Requires csv filename")
		exit()
	else:
		if type(save_to_csv) != str:
			logger.critical("\nCRITICAL ERROR, [save_to_csv]: Must be a str, current type = '{0}'".format(type(save_to_csv)))
			exit()
		else:
			if not save_to_csv.lower().endswith(".csv"):
				logger.critical("\nCRITICAL ERROR, [save_to_csv]: Extension must be a .csv file, current extension = '{0}'".format(save_to_csv.split(".")[1]))
				exit()

	if type(centerline_type) != str:
		logger.critical("\nCRITICAL ERROR, [centerline_type]: Must be a str, current type = '{0}'".format(type(centerline_type)))
		exit()
	else:
		if centerline_type.title() not in centerline_type_options:
			logger.critical("\nCRITICAL ERROR, [centerline_type]: Must be an available option in {0}, current option = '{1}'".format(centerline_type_options, centerline_type))
			exit()

	if type(coordinate_type) != str:
		logger.critical("\nCRITICAL ERROR, [coordinate_type]: Must be a str, current type = '{0}'".format(type(coordinate_type)))
		exit()
	else:
		coordinate_type_options = ["Decimal Degrees", "Relative Distance"]
		if coordinate_type.title() not in coordinate_type_options:
			logger.critical("\nCRITICAL ERROR, [coordinate_type]: Must be an available option in {0}, current option = '{1}'".format(coordinate_type_options, coordinate_type))
			exit()

def errorHandlingSaveCenterlineMAT(river_object=None,
								latitude_header=None,
								longitude_header=None,
								save_to_mat=None,
								centerline_type=None,
								coordinate_type=None):
	# Error Handling for saveCenterlineMAT()
	if river_object is None:
		logger.critical("\nCRITICAL ERROR, [river_object]: Requires a river object (see: centerline_width.riverCenterline)")
		exit()
	else:
		if not isinstance(river_object, centerline_width.riverCenterline):
			logger.critical("\nCRITICAL ERROR, [river_object]: Must be a river object (see: centerline_width.riverCenterline), current type = '{0}'".format(type(river_object)))
			exit()

	if latitude_header is not None:
		if type(latitude_header) != str:
			logger.critical("\nCRITICAL ERROR, [latitude_header]: Must be a str, current type = '{0}'".format(type(latitude_header)))
			exit()
		if any(not character.isalnum() for character in latitude_header):
			logger.critical("\nCRITICAL ERROR, [latitude_header]: Column names cannot contain any whitespace or non-alphanumeric characters, currently = '{0}'".format(latitude_header))
			exit()

	if longitude_header is not None:
		if type(longitude_header) != str:
			logger.critical("\nCRITICAL ERROR, [longitude_header]: Must be a str, current type = '{0}'".format(type(longitude_header)))
			exit()
		if any(not character.isalnum() for character in longitude_header):
			logger.critical("\nCRITICAL ERROR, [longitude_header]: Column names cannot contain any whitespace or non-alphanumeric characters, currently = '{0}'".format(longitude_header))
			exit()

	if save_to_mat is None:
		logger.critical("\nCRITICAL ERROR, [save_to_mat]: Requires mat filename")
		exit()
	else:
		if type(save_to_mat) != str:
			logger.critical("\nCRITICAL ERROR, [save_to_mat]: Must be a str, current type = '{0}'".format(type(save_to_mat)))
			exit()
		else:
			if not save_to_mat.lower().endswith(".mat"):
				logger.critical("\nCRITICAL ERROR, [save_to_mat]: Extension must be a .mat file, current extension = '{0}'".format(save_to_mat.split(".")[1]))
				exit()

	if type(centerline_type) != str:
		logger.critical("\nCRITICAL ERROR, [centerline_type]: Must be a str, current type = '{0}'".format(type(centerline_type)))
		exit()
	else:
		if centerline_type.title() not in centerline_type_options:
			logger.critical("\nCRITICAL ERROR, [centerline_type]: Must be an available option in {0}, current option = '{1}'".format(centerline_type_options, centerline_type))
			exit()

	if type(coordinate_type) != str:
		logger.critical("\nCRITICAL ERROR, [coordinate_type]: Must be a str, current type = '{0}'".format(type(coordinate_type)))
		exit()
	else:
		coordinate_type_options = ["Decimal Degrees", "Relative Distance"]
		if coordinate_type.title() not in coordinate_type_options:
			logger.critical("\nCRITICAL ERROR, [coordinate_type]: Must be an available option in {0}, current option = '{1}'".format(coordinate_type_options, coordinate_type))
			exit()

# Error Handling: getCoordinatesKML.py
def errorHandlingExtractPointsToTextFile(left_kml=None, right_kml=None, text_output_name=None):
	# Error Handling for extractPointsToTextFile()
	if left_kml is None:
		logger.critical("\nCRITICAL ERROR, [left_kml]: Requires left_kml file")
		exit()
	else:
		if type(left_kml) != str:
			logger.critical("\nCRITICAL ERROR, [left_kml]: Must be a str, current type = '{0}'".format(type(left_kml)))
			exit()
		if not left_kml.lower().endswith(".kml"):
			logger.critical("\nCRITICAL ERROR, [left_kml]: Extension must be a .kml file, current extension = '{0}'".format(left_kml.split(".")[1]))
			exit()

	if right_kml is None:
		logger.critical("\nCRITICAL ERROR, [right_kml]: Requires right_kml file")
		exit()
	else:
		if type(right_kml) != str:
			logger.critical("\nCRITICAL ERROR, [right_kml]: Must be a str, current type = '{0}'".format(type(right_kml)))
			exit()
		if not right_kml.lower().endswith(".kml"):
			logger.critical("\nCRITICAL ERROR, [right_kml]: Extension must be a .kml file, current extension = '{0}'".format(right_kml.split(".")[1]))
			exit()

	if right_kml == left_kml:
			logger.critical("\nCRITICAL ERROR, right_kml and left_kml are set to the same file (needs a seperate left and right bank): right_kml='{0}' and left_kml='{1}'".format(right_kml, left_kml))
			exit()

	if text_output_name is None:
		logger.critical("\nCRITICAL ERROR, [text_output_name]: Requires output file name")
		exit()
	else:
		if type(text_output_name) != str:
			logger.critical("\nCRITICAL ERROR, [text_output_name]: Must be a str, current type = '{0}'".format(type(text_output_name)))
			exit()

## Error Handling: riverCenterlineClass.py
def errorHandlingRiverCenterlineClass(csv_data=None,
									optional_cutoff=None,
									interpolate_data=None,
									interpolate_n=None,
									interpolate_n_centerpoints=None,
									equal_distance=None,
									ellipsoid=None):
	# Error Handling for riverCenterlineClass()
	if csv_data is None:
		logger.critical("\nCRITICAL ERROR, [csv_data]: Requires csv_data location")
		exit()
	else:
		if type(csv_data) != str and not isinstance(csv_data, StringIO): 
			# StringIO accounts for testing against a StringIO instead of a CSV (used in pytests)
			logger.critical("\nCRITICAL ERROR, [csv_data]: Must be a str, current type = '{0}'".format(type(csv_data)))
			exit()

	if optional_cutoff is not None:
		if type(optional_cutoff) != int:
			logger.critical("\nCRITICAL ERROR, [optional_cutoff]: Must be a int, current type = '{0}'".format(type(optional_cutoff)))
			exit()

	if type(interpolate_data) != bool:
		logger.critical("\nCRITICAL ERROR, [interpolate_data]: Must be a bool, current type = '{0}'".format(type(interpolate_data)))
		exit()

	if type(interpolate_n) != int:
		logger.critical("\nCRITICAL ERROR, [interpolate_n]: Must be a int, current type = '{0}'".format(type(interpolate_n)))
		exit()
		if interpolate_n > 15:
			logger.warn("WARNING, [interpolate_n]: Setting interpolate_n above 15 will cause the code to execute exponentially slower")

	if interpolate_n_centerpoints is not None:
		if type(interpolate_n_centerpoints) != int:
			logger.critical("\nCRITICAL ERROR, [interpolate_n_centerpoints]: Must be a int, current type = '{0}'".format(type(interpolate_n_centerpoints)))
			exit()
		else:
			if interpolate_n_centerpoints < 2:
				logger.critical("\nCRITICAL ERROR, [interpolate_n_centerpoints]: Must be a greater than 1, currently = '{0}'".format(interpolate_n_centerpoints))
				exit()

	if type(equal_distance) != int and type(equal_distance) != float:
		logger.critical("\nCRITICAL ERROR, [equal_distance]: Must be a int or float, current type = '{0}'".format(type(equal_distance)))
		exit()
		if equal_distance <= 0:
			logger.critical("WARNING, [equal_distance]: Must be a postive value, greater than 0, currently = '{0}'".format(equal_distance))
			exit()

	ellipsoid_options = ["GRS80", "airy", "bessel", "clrk66", "intl", "WGS60", "WGS66", "WGS72", "WGS84", "sphere"]
	if type(ellipsoid) != str:
		logger.critical("\nCRITICAL ERROR, [ellipsoid]: Must be a str, current type = '{0}'".format(type(ellipsoid)))
		exit()
	else:
		if ellipsoid not in ellipsoid_options:
			logger.critical("\nCRITICAL ERROR, [ellipsoid]: Must be an available option in {0}, current option = '{1}'".format(ellipsoid_options, ellipsoid))
			exit()
