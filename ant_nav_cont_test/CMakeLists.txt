cmake_minimum_required(VERSION 2.8.3)
project(ant_nav_cont_test)

set(PAL_MODULE_NAME 'NAVIGATION')
set(PAL_LIBRARY_NAME '${PROJECT_NAME}')

find_package(catkin REQUIRED COMPONENTS
  pal_core
  pal_navigation_client
)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++0x")

catkin_package(
  INCLUDE_DIRS include
  LIBRARIES ${PROJECT_NAME}
  CATKIN_DEPENDS pal_core 
)

include_directories(include ${catkin_INCLUDE_DIRS})

add_executable(antNavActClientReportingTest
  src/NavActClientReporter.cpp
  src/NavActClientReporterTest.cpp
)
target_link_libraries(antNavActClientReportingTest ${catkin_LIBRARIES})

install(DIRECTORY include/
   DESTINATION ${CATKIN_GLOBAL_INCLUDE_DESTINATION}
   FILES_MATCHING PATTERN "*.h"
)
