# Pytest for preprocessing.py
# centerline-width/: python3 -m pytest -v
import logging
from io import StringIO

# External Python libraries (installed via pip install)
import pytest

# Internal centerline-width reference to access functions, global variables, and error handling
import centerline_width

invalid_non_bool_options = [(1961, "<class 'int'>"),
						(3.1415, "<class 'float'>"),
						([], "<class 'list'>"),
						("testing_string", "<class 'str'>")]

invalid_non_class_options = [(1961, "<class 'int'>"),
						(3.1415, "<class 'float'>"),
						([], "<class 'list'>"),
						("testing_string", "<class 'str'>"),
						(False, "<class 'bool'>")]

invalid_non_int_options = [("testing_string", "<class 'str'>"),
						(3.1415, "<class 'float'>"),
						([], "<class 'list'>"),
						(False, "<class 'bool'>")]

invalid_non_str_options = [(1961, "<class 'int'>"),
						(3.1415, "<class 'float'>"),
						([], "<class 'list'>"),
						(False, "<class 'bool'>")]

def river_class_object():
	csv_example = StringIO()
	csv_example.write("llat,llon,rlat,rlon\n")
	csv_example.write("30.037581,-92.868569,30.037441,-92.867476\n")
	csv_example.write("30.137581,-92.868569,30.037441,-92.867476\n")
	csv_example.write("30.237581,-92.868569,30.037441,-92.867476\n")
	csv_example.seek(0)
	return centerline_width.riverCenterline(csv_data=csv_example)

river_class_example = river_class_object()

## riverWidthFromCenterlineCoordinates() #####################################################
def test_riverWidthFromCenterline_riverObjectRequired(caplog):
	with pytest.raises(SystemExit):
		centerline_width.riverWidthFromCenterline(river_object=None)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [river_object]: Requires a river object (see: centerline_width.riverCenterline)"

@pytest.mark.parametrize("river_object_invalid, river_object_error_output", invalid_non_class_options)
def test_riverWidthFromCenterline_riverObjectInvalidTypes(caplog, river_object_invalid, river_object_error_output):
	with pytest.raises(SystemExit):
		centerline_width.riverWidthFromCenterline(river_object=river_object_invalid)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [river_object]: Must be a river object (see: centerline_width.riverCenterline), current type = '{0}'".format(river_object_error_output)

@pytest.mark.parametrize("transect_span_distance_invalid, transect_span_distance_error_output", invalid_non_int_options)
def test_riverWidthFromCenterline_transectSpanDistanceInvalidTypes(caplog, transect_span_distance_invalid, transect_span_distance_error_output):
	with pytest.raises(SystemExit):
		centerline_width.riverWidthFromCenterline(river_object=river_class_example,
											transect_span_distance=transect_span_distance_invalid)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [transect_span_distance]: Must be a int, current type = '{0}'".format(transect_span_distance_error_output)

@pytest.mark.parametrize("apply_smoothing_invalid, apply_smoothing_error_output", invalid_non_bool_options)
def test_riverWidthFromCenterline_applySmoothingInvalidTypes(caplog, apply_smoothing_invalid, apply_smoothing_error_output):
	with pytest.raises(SystemExit):
		centerline_width.riverWidthFromCenterline(river_object=river_class_example,
											apply_smoothing=apply_smoothing_invalid)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [apply_smoothing]: Must be a bool, current type = '{0}'".format(apply_smoothing_error_output)

@pytest.mark.parametrize("remove_intersections_invalid, remove_intersections_error_output", invalid_non_bool_options)
def test_riverWidthFromCenterline_removeIntersectionsInvalidTypes(caplog, remove_intersections_invalid, remove_intersections_error_output):
	with pytest.raises(SystemExit):
		centerline_width.riverWidthFromCenterline(river_object=river_class_example,
											remove_intersections=remove_intersections_invalid)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [remove_intersections]: Must be a bool, current type = '{0}'".format(remove_intersections_error_output)

@pytest.mark.parametrize("save_to_csv_invalid, save_to_csv_error_output", invalid_non_str_options)
def test_riverWidthFromCenterline_saveToCSVInvalidTypes(caplog, save_to_csv_invalid, save_to_csv_error_output):
	with pytest.raises(SystemExit):
		centerline_width.riverWidthFromCenterline(river_object=river_class_example,
											save_to_csv=save_to_csv_invalid)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [save_to_csv]: Must be a str, current type = '{0}'".format(save_to_csv_error_output)

def test_riverWidthFromCenterline_csvInvalidExtension(caplog):
	with pytest.raises(SystemExit):
		centerline_width.riverWidthFromCenterline(river_object=river_class_example,
												save_to_csv="filename.txt")
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [save_to_csv]: Extension must be a .csv file, current extension = 'txt'"

def test_riverWidthFromCenterline_coordinateTypeInvalidOption(caplog):
	with pytest.raises(SystemExit):
		centerline_width.riverWidthFromCenterline(river_object=river_class_example,
										coordinate_type="Invalid Option")
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [coordinate_type]: Must be an available option in ['Decimal Degrees', 'Relative Distance'], current option = 'Invalid Option'"

@pytest.mark.parametrize("coordinate_type_name_invalid, coordinate_type_error_output", invalid_non_str_options)
def test_riverWidthFromCenterline_coordinateTypeInvalidTypes(caplog, coordinate_type_name_invalid, coordinate_type_error_output):
	with pytest.raises(SystemExit):
		centerline_width.riverWidthFromCenterline(river_object=river_class_example,
										coordinate_type=coordinate_type_name_invalid)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [coordinate_type]: Must be a str, current type = '{0}'".format(coordinate_type_error_output)


## saveCenterlineCSV() #####################################################
def test_saveCenterlineCSV_riverObjectRequired(caplog):
	with pytest.raises(SystemExit):
		centerline_width.saveCenterlineCSV(river_object=None)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [river_object]: Requires a river object (see: centerline_width.riverCenterline)"

def test_saveCenterlineCSV_csvInvalidExtension(caplog):
	with pytest.raises(SystemExit):
		centerline_width.saveCenterlineCSV(river_object=river_class_example, save_to_csv=None)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [save_to_csv]: Requires csv filename"

def test_saveCenterlineCSV_csvRequired(caplog):
	with pytest.raises(SystemExit):
		centerline_width.saveCenterlineCSV(river_object=river_class_example, save_to_csv="filename.txt")
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [save_to_csv]: Extension must be a .csv file, current extension = 'txt'"

@pytest.mark.parametrize("latitude_header_invalid, latitude_header_error_output", invalid_non_str_options)
def test_saveCenterlineCSV_latitudeHeaderTypeInvalidTypes(caplog, latitude_header_invalid, latitude_header_error_output):
	with pytest.raises(SystemExit):
		centerline_width.saveCenterlineCSV(river_object=river_class_example,
											save_to_csv="testing.csv",
											latitude_header=latitude_header_invalid)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [latitude_header]: Must be a str, current type = '{0}'".format(latitude_header_error_output)

@pytest.mark.parametrize("longitude_header_invalid, longitude_header_error_output", invalid_non_str_options)
def test_saveCenterlineCSV_longitudeHeaderTypeInvalidTypes(caplog, longitude_header_invalid, longitude_header_error_output):
	with pytest.raises(SystemExit):
		centerline_width.saveCenterlineCSV(river_object=river_class_example,
											save_to_csv="testing.csv",
											longitude_header=longitude_header_invalid)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [longitude_header]: Must be a str, current type = '{0}'".format(longitude_header_error_output)

@pytest.mark.parametrize("centerline_type_invalid, centerline_type_error_output", invalid_non_str_options)
def test_saveCenterlineCSV_centerlineTypeInvalidTypes(caplog, centerline_type_invalid, centerline_type_error_output):
	with pytest.raises(SystemExit):
		centerline_width.saveCenterlineCSV(river_object=river_class_example,
											save_to_csv="testing.csv",
											centerline_type=centerline_type_invalid)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [centerline_type]: Must be a str, current type = '{0}'".format(centerline_type_error_output)

def test_saveCenterlineCSV_centerlineTypeInvalidOptions(caplog):
	with pytest.raises(SystemExit):
		centerline_width.saveCenterlineCSV(river_object=river_class_example,
											save_to_csv="testing.csv",
											centerline_type="not valid")
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [centerline_type]: Must be an available option in ['Voronoi', 'Evenly Spaced', 'Smoothed', 'Equal Distance'], current option = 'not valid'"

def test_saveCenterlineCSV_coordinateTypeInvalidOption(caplog):
	with pytest.raises(SystemExit):
		centerline_width.saveCenterlineCSV(river_object=river_class_example,
										save_to_csv="testing.csv",
										coordinate_type="Invalid Option")
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [coordinate_type]: Must be an available option in ['Decimal Degrees', 'Relative Distance'], current option = 'Invalid Option'"

@pytest.mark.parametrize("coordinate_type_name_invalid, coordinate_type_error_output", invalid_non_str_options)
def test_saveCenterlineCSV_coordinateTypeInvalidTypes(caplog, coordinate_type_name_invalid, coordinate_type_error_output):
	with pytest.raises(SystemExit):
		centerline_width.saveCenterlineCSV(river_object=river_class_example,
										save_to_csv="testing.csv",
										coordinate_type=coordinate_type_name_invalid)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [coordinate_type]: Must be a str, current type = '{0}'".format(coordinate_type_error_output)

## saveCenterlineMAT() #####################################################
def test_saveCenterlineMAT_riverObjectRequired(caplog):
	with pytest.raises(SystemExit):
		centerline_width.saveCenterlineMAT(river_object=None)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [river_object]: Requires a river object (see: centerline_width.riverCenterline)"

def test_saveCenterlineMAT_matInvalidExtension(caplog):
	with pytest.raises(SystemExit):
		centerline_width.saveCenterlineMAT(river_object=river_class_example, save_to_mat=None)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [save_to_mat]: Requires mat filename"

def test_saveCenterlineMAT_matRequired(caplog):
	with pytest.raises(SystemExit):
		centerline_width.saveCenterlineMAT(river_object=river_class_example, save_to_mat="filename.txt")
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [save_to_mat]: Extension must be a .mat file, current extension = 'txt'"

@pytest.mark.parametrize("latitude_header_invalid, latitude_header_error_output", invalid_non_str_options)
def test_saveCenterlineMAT_latitudeHeaderTypeInvalidTypes(caplog, latitude_header_invalid, latitude_header_error_output):
	with pytest.raises(SystemExit):
		centerline_width.saveCenterlineMAT(river_object=river_class_example,
											save_to_mat="testing.mat",
											latitude_header=latitude_header_invalid)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [latitude_header]: Must be a str, current type = '{0}'".format(latitude_header_error_output)

def test_saveCenterlineMAT_latitudeHeaderTypeInvalidAlphanumeric(caplog):
	with pytest.raises(SystemExit):
		centerline_width.saveCenterlineMAT(river_object=river_class_example,
											save_to_mat="testing.mat",
											latitude_header="invalid whitespace")
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [latitude_header]: Column names cannot contain any whitespace or non-alphanumeric characters, currently = 'invalid whitespace'"

@pytest.mark.parametrize("longitude_header_invalid, longitude_header_error_output", invalid_non_str_options)
def test_saveCenterlineMAT_longitudeHeaderTypeInvalidTypes(caplog, longitude_header_invalid, longitude_header_error_output):
	with pytest.raises(SystemExit):
		centerline_width.saveCenterlineMAT(river_object=river_class_example,
											save_to_mat="testing.mat",
											longitude_header=longitude_header_invalid)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [longitude_header]: Must be a str, current type = '{0}'".format(longitude_header_error_output)

def test_saveCenterlineMAT_longitudeHeaderTypeInvalidAlphanumeric(caplog):
	with pytest.raises(SystemExit):
		centerline_width.saveCenterlineMAT(river_object=river_class_example,
											save_to_mat="testing.mat",
											longitude_header="invalid whitespace")
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [longitude_header]: Column names cannot contain any whitespace or non-alphanumeric characters, currently = 'invalid whitespace'"

@pytest.mark.parametrize("centerline_type_invalid, centerline_type_error_output", invalid_non_str_options)
def test_saveCenterlineMAT_centerlineTypeInvalidTypes(caplog, centerline_type_invalid, centerline_type_error_output):
	with pytest.raises(SystemExit):
		centerline_width.saveCenterlineMAT(river_object=river_class_example,
											save_to_mat="testing.mat",
											centerline_type=centerline_type_invalid)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [centerline_type]: Must be a str, current type = '{0}'".format(centerline_type_error_output)

def test_saveCenterlineMAT_centerlineTypeInvalidOptions(caplog):
	with pytest.raises(SystemExit):
		centerline_width.saveCenterlineMAT(river_object=river_class_example,
											save_to_mat="testing.mat",
											centerline_type="not valid")
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [centerline_type]: Must be an available option in ['Voronoi', 'Evenly Spaced', 'Smoothed', 'Equal Distance'], current option = 'not valid'"

def test_saveCenterlineMAT_coordinateTypeInvalidOption(caplog):
	with pytest.raises(SystemExit):
		centerline_width.saveCenterlineMAT(river_object=river_class_example,
										save_to_mat="testing.mat",
										coordinate_type="Invalid Option")
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [coordinate_type]: Must be an available option in ['Decimal Degrees', 'Relative Distance'], current option = 'Invalid Option'"

@pytest.mark.parametrize("coordinate_type_name_invalid, coordinate_type_error_output", invalid_non_str_options)
def test_saveCenterlineMAT_coordinateTypeInvalidTypes(caplog, coordinate_type_name_invalid, coordinate_type_error_output):
	with pytest.raises(SystemExit):
		centerline_width.saveCenterlineMAT(river_object=river_class_example,
										save_to_mat="testing.mat",
										coordinate_type=coordinate_type_name_invalid)
	log_record = caplog.records[0]
	assert log_record.levelno == logging.CRITICAL
	assert log_record.message == "\nCRITICAL ERROR, [coordinate_type]: Must be a str, current type = '{0}'".format(coordinate_type_error_output)
