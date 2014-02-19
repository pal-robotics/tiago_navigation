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
)

include_directories(include ${catkin_INCLUDE_DIRS})

add_executable(navActClientReportingTest
  src/NavActClientReporter.cpp
  src/NavActClientReporterTest.cpp
)
target_link_libraries(navActClientReportingTest ${catkin_LIBRARIES})
