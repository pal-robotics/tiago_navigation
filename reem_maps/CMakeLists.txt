cmake_minimum_required(VERSION 2.8.3)
project(reem_maps)

find_package(catkin REQUIRED)

catkin_package()

install(PROGRAMS
    scripts/map_setup.py
    scripts/poi_manager.py
    scripts/update_map_symlink.sh
    DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})

foreach(dir launch configurations)
    install(DIRECTORY ${dir}/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)

install(DIRECTORY config
    DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})

