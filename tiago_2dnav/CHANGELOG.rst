^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package pmb2_2dnav
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.0.8 (2020-07-30)
------------------
* Merge branch 'rename_tf_prefix' into 'erbium-devel'
  Rename tf_prefix to robot_namespace
  See merge request robots/pmb2_navigation!46
* Rename tf_prefix to robot_namespace
* Contributors: davidfernandez, victor

2.0.7 (2020-07-02)
------------------

4.5.0 (2024-10-25)
------------------
* Merge branch 'abr/feat/mppi' into 'humble-devel'
  Use mppi
  See merge request robots/tiago_navigation!120
* Use mppi
* Contributors: antoniobrandi

4.4.0 (2024-10-23)
------------------
* Merge branch 'feat/aca/omni-navigation-mppi' into 'humble-devel'
  Using MPPI
  See merge request robots/tiago_navigation!119
* Using MPPI
* Contributors: andreacapodacqua

4.3.0 (2024-10-17)
------------------
* Merge branch 'man/feat/nav-rviz-config' into 'humble-devel'
  added unless condition to rviz
  See merge request robots/tiago_navigation!117
* added unless condition to rviz
* Contributors: antoniobrandi, martinaannicelli

4.2.0 (2024-09-03)
------------------
* Merge branch 'man/feat/docking' into 'humble-devel'
  added docking link
  See merge request robots/tiago_navigation!115
* added docking link
* Contributors: josegarcia, martinaannicelli

4.1.7 (2024-07-19)
------------------
* Merge branch 'fix/aca/laser-frames' into 'humble-devel'
  fix laser frames
  See merge request robots/tiago_navigation!113
* fix laser frames
* Contributors: andreacapodacqua

4.1.6 (2024-07-17)
------------------
* Merge branch 'air/unify_pkgs' into 'humble-devel'
  restructure launch file
  See merge request robots/tiago_navigation!109
* add slam condition in slam launch include & fix error file path for slam
* remove condition in public rviz
* fix config files paths
* using base_type and changing pub/private condition
* change base name into base_navigation_type
* add laser dependency
* restructure launch file
* Contributors: Aina, antoniobrandi

4.1.5 (2024-07-15)
------------------
* Merge branch 'feat/aca/pipeline-substitution' into 'humble-devel'
  using variables for pipeline
  See merge request robots/tiago_navigation!105
* reorganized remappings file
* naming convention
* added device number laser
* Contributors: andreacapodacqua

4.1.4 (2024-07-10)
------------------
* Merge branch 'fix/aca/missing-dep' into 'humble-devel'
  added missing dep
  See merge request robots/tiago_navigation!112
* added missing dep
* Contributors: andreacapodacqua

4.1.3 (2024-07-09)
------------------
* Add warning for pal_module_cmake not found
* Contributors: Noel Jimenez

4.1.2 (2024-07-05)
------------------
* Merge branch 'fix/changed-base-type-name' into 'humble-devel'
  changed diff_drive to pmb2
  See merge request robots/tiago_navigation!110
* fix default
* removed base_type check
* changed diff_drive to pmb2
* Contributors: andreacapodacqua

4.1.1 (2024-07-01)
------------------
* Merge branch 'abr/feat/using-filters' into 'humble-devel'
  using costmap with filters
  See merge request robots/tiago_navigation!108
* using costmap with filters
* Contributors: antoniobrandi

4.1.0 (2024-06-26)
------------------
* Merge branch 'feature/support-different-base-types' into 'humble-devel'
  feat: support different base types
  See merge request robots/tiago_navigation!102
* feat: support base_type on real robot
* feat: support base_type in simulation
* Contributors: antoniobrandi, josegarcia

4.0.18 (2024-06-25)
-------------------
* Merge branch 'abr/feat/rviz-nav' into 'humble-devel'
  move rviz in nav launch file
  See merge request robots/tiago_navigation!106
* move rviz in nav launch file
* Contributors: antoniobrandi

4.0.17 (2024-06-18)
-------------------
* Fix pal_maps path
* Contributors: Noel Jimenez

4.0.16 (2024-05-29)
-------------------
* Merge branch 'fix/aca/public-sim' into 'humble-devel'
  fix public sim
  See merge request robots/tiago_navigation!103
* fix public sim
* Contributors: Noel Jimenez, andreacapodacqua

4.0.15 (2024-05-08)
-------------------

4.0.14 (2024-04-29)
-------------------
* Merge branch 'abr/feat/deprecate-maps' into 'humble-devel'
  deprecate tiago_maps
  See merge request robots/tiago_navigation!99
* deprecate tiago_maps
* Contributors: antoniobrandi

4.0.13 (2024-04-23)
-------------------
* Merge branch 'feat/ros2-pipelines' into 'humble-devel'
  Feat/ros2 pipelines
  See merge request robots/tiago_navigation!98
* using variables lifecycle manager
* using new variables names
* using variables
* restored default controller
* update public sim launch and renamed params
* cosmetic
* linters
* modified params laser pipeline
* linters
* navigation pipelines
* navigation pipeline
* added modules and pipelines
* Contributors: andreacapodacqua, antoniobrandi

4.0.12 (2024-02-13)
-------------------
* Merge branch 'abr/fix/world-name' into 'humble-devel'
  set default world_name for standalone navigation
  See merge request robots/tiago_navigation!97
* set default world_name for standalone navigation
* Contributors: antoniobrandi

4.0.11 (2024-02-12)
-------------------
* Merge branch 'fix/pal_nav2_bringup' into 'humble-devel'
  Use pal_nav2_bringup only for private simulation
  See merge request robots/tiago_navigation!96
* Use pal_nav2_bringup only for private simulation
* Contributors: Noel Jimenez, antoniobrandi

4.0.10 (2024-02-02)
-------------------
* Merge branch 'feat/register-components' into 'humble-devel'
  using components and parameters
  See merge request robots/tiago_navigation!95
* using components and parameters
* Contributors: antoniobrandi

4.0.9 (2023-12-12)
------------------

4.0.8 (2023-11-14)
------------------
* Add website tag
* Contributors: Noel Jimenez

4.0.7 (2023-11-07)
------------------

4.0.6 (2023-09-18)
------------------
* Merge branch 'remove_pal_flags_dependency' into 'humble-devel'
  Remove pal flags dependency
  See merge request robots/tiago_navigation!86
* Remove pal flags dependency
* Contributors: Jordan Palacios, Noel Jimenez

4.0.5 (2023-06-16)
------------------
* Merge branch 'feat/laser-filters' into 'humble-devel'
  using laser filters in simulation
  See merge request robots/tiago_navigation!83
* clarifying remappings usage
* using pmb2_sim_nav_bringup and update deps
* using sim bringup
* start laser filters in simulation
* using laser filters in simulation
* Contributors: antoniobrandi

4.0.3 (2023-04-03)
------------------
* Merge branch 'feat/pal-navigation-cfg' into 'humble-devel'
  Using pal_navigation_cfg
  See merge request robots/tiago_navigation!77
* Using pal_navigation_cfg
* Contributors: antoniobrandi

4.0.2 (2022-12-15)
------------------
* Merge pull request #12 from jmguerreroh/humble-devel
  Remap to show laser scan on RViz
* Remap to show laser scan on RViz
* Contributors: Sai Kishor Kothakota, jmguerreroh

4.0.1 (2022-11-29)
------------------
* Merge branch 'mlu/fix/tiago_2dnav_buildtool' into 'humble-devel'
  Fix  buildtool_depend of tiago_2dnav
  See merge request robots/tiago_navigation!68
* Fix  buildtool_depend of tiago_2dnav
  Must be ament_cmake_auto
* Contributors: Noel Jimenez, mathiasluedtke

4.0.0 (2022-11-08)
------------------
* Merge branch 'update_copyright' into 'humble-devel'
  Update copyright
  See merge request robots/tiago_navigation!65
* update package format
* update copyright
* Merge branch 'update_maintainers' into 'humble-devel'
  update maintainers
  See merge request robots/tiago_navigation!64
* update maintainers
* Merge branch 'linters' into 'humble-devel'
  linters
  See merge request robots/tiago_navigation!63
* linters
* First version of foxy-devel tiago_2dnav
* Contributors: Jordan Palacios, Noel Jimenez, Victor Lopez

2.0.6 (2020-04-02)
------------------

2.0.5 (2019-11-22)
------------------
* passing subtype parameter to move_base
* Contributors: federiconardi

2.0.4 (2019-10-01)
------------------

2.0.3 (2019-09-23)
------------------
* use scan_raw for mapping
* Contributors: Procópio Stein

2.0.2 (2019-09-18)
------------------

2.0.1 (2019-07-19)
------------------
* Merge branch 'multi_pmb2' into 'erbium-devel'
  Add multi pmb2 navigation
  See merge request robots/pmb2_navigation!40
* Add multi pmb2 navigation
* Contributors: Adria Roig, Victor Lopez

2.0.0 (2019-06-17)
------------------
* added pal_navigation_cfg_pmb2 dependency
* moved config and launch to pal_navigation_cfg_pmb2
* Contributors: Procópio Stein, Sai Kishor Kothakota

1.0.6 (2019-05-20)
------------------
* Merge branch 'update_adv_nav' into 'erbium-devel'
  Update AdvNav Rviz config
  See merge request robots/pmb2_navigation!38
* Update AdvNav Rviz config
* Contributors: Victor Lopez, davidfernandez

1.0.5 (2019-05-06)
------------------
* updated teb config to match tiago's
* Contributors: Procópio Stein

1.0.4 (2019-03-22)
------------------
* Merge branch 'update-karto-cfg' into 'erbium-devel'
  updated karto params to improve loop closures
  See merge request robots/pmb2_navigation!36
* updated karto params to improve loop closures
* Contributors: Procópio Stein

1.0.3 (2019-01-25)
------------------
* Merge branch 'public_eband_conf' into 'erbium-devel'
  added eband planner config
  See merge request robots/pmb2_navigation!35
* added eband planner config
* Merge branch 'plugin_fix' into 'erbium-devel'
  public simulation plugin fix
  See merge request robots/pmb2_navigation!34
* public simulation plugin fix
* Contributors: Sai Kishor Kothakota, Victor Lopez

1.0.2 (2019-01-17)
------------------
* Merge branch 'public_sim_kinetic' into 'erbium-devel'
  add Kinetic pulbic simulation changes
  See merge request robots/pmb2_navigation!33
* add kinetic public simulation changes
* Contributors: Sai Kishor Kothakota, Victor Lopez

1.0.1 (2019-01-15)
------------------
* Fix typo
* Contributors: Victor Lopez

1.0.0 (2018-12-19)
------------------
* Merge branch 'specifics-refactor' into 'erbium-devel'
  Specifics refactor
  See merge request robots/pmb2_navigation!30
* Cosmetic
* Add parameters for using rgbd
* Specify one karto file per laser model
* Contributors: Victor Lopez

0.13.17 (2018-12-19)
--------------------
* change the param load order to overrite the karto config
* activated latch xy for goals
* Contributors: Procópio Stein

0.13.16 (2018-11-21)
--------------------
* added sonar layer
* added sound feedback for loop closure
* Contributors: Procópio Stein, Sai Kishor Kothakota

0.13.15 (2018-10-20)
--------------------
* Merge branch 'clear-vo-on-recovery' into 'dubnium-devel'
  added vo clearing in recovery behavior
  See merge request robots/pmb2_navigation!25
* added vo clearing in recovery behavior
* Contributors: Procópio Stein

0.13.14 (2018-10-03)
--------------------
* updated costmaps config to correspond to template generation
* Contributors: Procópio Stein

0.13.13 (2018-09-28)
--------------------
* slightly increased max_threshold from 1.5 to 1.8
* Contributors: Procópio Stein

0.13.12 (2018-09-26)
--------------------
* changed param name from threshold to max_threshold
* removed deprecated parameter
* Contributors: Procópio Stein

0.13.11 (2018-09-26)
--------------------
* Merge branch 'adjust-plp-params' into 'dubnium-devel'
  increased max threshold and reduced security
  See merge request robots/pmb2_navigation!23
* increased max threshold and reduced security
* Contributors: Procópio Stein

0.13.10 (2018-09-17)
--------------------
* increased plp threshold
* updated recovery to match cobra, but commented blanking recoveries
* updated rviz config
* enabled search alternative goals
* reduced pub freq of costmaps, cleaned them up
* adjusted default threshold and sec distance
* better visualization
* updated pal_local_planner config
* Contributors: Procópio Stein

0.13.9 (2018-06-22)
-------------------

0.13.8 (2018-05-17)
-------------------
* updated amcl and karto configs for clarity and to match last developments in specifics
* added odom filter config and changed search path to pmb2_2dnav
* Contributors: Procópio Stein

0.13.7 (2018-05-15)
-------------------
* added slippage related launch files
* Contributors: Procópio Stein

0.13.6 (2018-04-24)
-------------------
* Revert "avoid oscillating global path and prefer shorter paths"
  This reverts commit 0d0601e59441e560ffb56ce15d7cb37bce0a9d71.
* Contributors: Procópio Stein

0.13.5 (2018-04-17)
-------------------

0.13.4 (2018-04-12)
-------------------

0.13.3 (2018-04-06)
-------------------
* added TEB config
* disable navigation in unknown
* added dependency on range layer and teb local planner
* avoid oscillating global path and prefer shorter paths
* Contributors: Procópio Stein

0.13.2 (2018-03-08)
-------------------

0.13.1 (2018-02-15)
-------------------
* Merge branch 'respawn-move-base' into 'dubnium-devel'
  added respawn flag to move_base.launch
  See merge request robots/pmb2_navigation!11
* added respawn flag to move_base.launch
* Contributors: Procópio Stein

0.13.0 (2018-02-01)
-------------------

0.12.0 (2017-10-17)
-------------------
* updated parameter due to refactoring in pal-local-planner
* Contributors: Procópio Stein

0.11.10 (2017-09-27)
--------------------
* normalized package.xml for all packages
* Contributors: Procópio Stein

0.11.9 (2017-09-19)
-------------------
* updated parameters to new pal local planner
* Contributors: Procópio Stein

0.11.8 (2017-09-18)
-------------------
* added config base path arg, so it can load params from .pal
* Contributors: Procópio Stein

0.11.7 (2017-08-08)
-------------------
* allow global plan in unkown spaces
* Contributors: Procópio Stein

0.11.6 (2017-07-03)
-------------------

0.11.5 (2017-06-30)
-------------------
* added rotate recovery behavior
* Contributors: Procópio Stein

0.11.4 (2017-06-30)
-------------------

0.11.3 (2017-06-01)
-------------------

0.11.2 (2017-04-25)
-------------------
* updated adv nav rviz config
* Contributors: Procópio Stein

0.11.1 (2017-04-22)
-------------------
* added advanced nav config
* Contributors: Procópio Stein

0.11.0 (2017-02-28)
-------------------
* removed legacy move_base configs
* updated costmap files to match template
* fixed global planner config file
* updated rviz navigation config
* 0.10.4
* changelogs
* updated costmap and recovery params
* fixed robot radius
* Contributors: Procópio Stein

0.10.4 (2017-02-28)
-------------------
* updated costmap and recovery params
* fixed robot radius
* Contributors: Procópio Stein

0.10.3 (2017-02-24)
-------------------
* enhanced navigation config, fixed recovery behaviors
* Contributors: Procópio Stein

0.10.2 (2017-02-23)
-------------------

0.10.1 (2017-02-23)
-------------------
* removed rgbd launches and config, fixed dependencies
* minor changes in mapping and localization config
* better mapping and slam configurations
* updated local_planner config for enhanced version of planner
* updated costmap config based on new tiago files
* add rviz launch file
* Contributors: Jeremie Deray, Procópio Stein

0.10.0 (2016-03-15)
-------------------
* use degree
* Contributors: Jeremie Deray

0.9.15 (2016-03-10)
-------------------
* missing deps maps
* Contributors: Jeremie Deray

0.9.14 (2016-03-02)
-------------------

0.9.13 (2016-02-10)
-------------------

0.9.12 (2016-02-10)
-------------------

0.9.11 (2016-02-09)
-------------------

0.9.10 (2016-02-09)
-------------------
* final review of parameters with jeremie
* restoring plugins in costmaps (but commented)
* correcting errors in pm2_2dnav
  restored amcl laser range to default values, corrected typo in local costmap, removed plugins example
* minor cleaning in pmb2 navigation files
* cleaned generic pmb2_2dnav and improved specific pmb2_5_2dnav
* Contributors: Procopio Stein, procopiostein

0.9.9 (2015-10-26)
------------------
* disable free space mapping for pmb2 & add warning abt it
* Fixing localization amcl jumps
* update rviz conf
* Custom launch file for pmb2-5
* Contributors: Jeremie Deray, Luca Marchionni

0.9.8 (2015-10-01)
------------------
* typo
* add slam graph display to rviz
* amcl laser min/max range
* karto laser max_range
* karto map free space
* reduce global inflation radius
* reduce visualization pub rate
* amcl config add param defaut value + comments
* rviz do not display sonar/rgbd related stuff
* do not launch xtion related stuff
* deactivate rgbd layer for costmaps
* Add laser classification displays
* Sync filter script with ant
* Sync with ant_2dnav
* Add covariance (odometry + pose) displays
  NOTE they are disabled by default because they have some issues yet
  with the 6DOF mode property, which is not disabled properly on startup
* Update layout and add inertia + CoM marker
* Update rviz layout
* Increase the number of sonars from 3 to 5
* Contributors: Enrique Fernandez, Jeremie Deray

0.9.7 (2015-02-02)
------------------
* Replace ant -> pmb2
* Rename files
* Contributors: Enrique Fernandez
