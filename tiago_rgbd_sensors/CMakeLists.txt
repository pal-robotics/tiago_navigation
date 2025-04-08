cmake_minimum_required(VERSION 3.5)
project(tiago_rgbd_sensors)

find_package(ament_cmake_auto REQUIRED)
ament_auto_find_build_dependencies()

if(pal_module_cmake_FOUND)
  pal_register_modules(module/40_rgbd.yaml)
elseif(DEFINED ENV{PAL_DISTRO})
  message(FATAL_ERROR "The pal_module_cmake package was not found. Modules not registered.")
endif()
if(pal_configuration_cmake_FOUND)
  pal_register_configs(
    CONFIGS
      params/40_astra_camera_cfg_tiago.yaml
    RESOURCE_NAME
      astra_camera_cfg
  )
elseif(DEFINED ENV{PAL_DISTRO})
  message(FATAL_ERROR "The pal_configuration_cmake package was not found. Configurations not registered.")
endif()

if(BUILD_TESTING)
  ament_auto_find_test_dependencies()
  ament_lint_auto_find_test_dependencies()
endif()

ament_auto_package()
