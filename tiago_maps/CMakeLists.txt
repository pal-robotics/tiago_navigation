cmake_minimum_required(VERSION 2.8.3)
project(tiago_maps)

find_package(catkin REQUIRED)

catkin_package()

foreach(dir configurations buildings)
    install(DIRECTORY ${dir}/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)

install(DIRECTORY config
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

install(FILES building_description.yaml building.yaml
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
