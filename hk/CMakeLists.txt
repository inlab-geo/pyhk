file ( GLOB rf_c_functions *.c* *.h* )
find_package(Python REQUIRED COMPONENTS Interpreter Development.Module)
Python_add_library(rf_lib MODULE WITH_SOABI ${rf_c_functions})
install(TARGETS rf_lib DESTINATION ./pyhk)
