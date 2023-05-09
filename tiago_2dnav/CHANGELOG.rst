^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tiago_2dnav
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.1.18 (2023-05-09)
-------------------

2.1.17 (2023-04-19)
-------------------

2.1.16 (2023-03-23)
-------------------

2.1.15 (2023-03-23)
-------------------

2.1.14 (2023-03-15)
-------------------

2.1.13 (2023-03-15)
-------------------
* Merge branch 'fix_rosparam' into 'erbium-devel'
  Change the advance nav head to be global parameter
  See merge request robots/tiago_navigation!73
* Change the advance nav head to be global parameter
* Contributors: antoniobrandi, thomaspeyrucain

2.1.12 (2023-03-15)
-------------------

2.1.11 (2023-03-13)
-------------------

2.1.10 (2023-03-09)
-------------------

2.1.8 (2023-03-06)
------------------

2.1.7 (2023-02-09)
------------------
* Merge branch 'add_head_parameter' into 'erbium-devel'
  Add dynamic parameter to change head angle
  See merge request robots/tiago_navigation!69
* Putting back default head angle
* Add dynamic parameter to change head angle
* Contributors: antoniobrandi, thomaspeyrucain

2.1.6 (2023-01-30)
------------------
* Merge branch 'feat/map-manager' into 'erbium-devel'
  move to map manager
  See merge request robots/tiago_navigation!66
* move to map manager
* Contributors: antoniobrandi

2.1.5 (2022-09-15)
------------------

2.1.4 (2022-08-16)
------------------

2.1.3 (2022-08-16)
------------------

2.1.2 (2022-08-11)
------------------

2.1.1 (2022-07-26)
------------------

2.1.0 (2021-11-03)
------------------
* Merge branch 'omni_base_robot' into 'erbium-devel'
  Omni base robot
  See merge request robots/tiago_navigation!57
* cosmetic
* tiago navigation with omni base
* Contributors: antoniobrandi, saikishor

2.0.6 (2020-07-30)
------------------
* Merge branch 'rename_tf_prefix' into 'erbium-devel'
  Rename tf_prefix to robot_namespace
  See merge request robots/tiago_navigation!53
* Rename tf_prefix to robot_namespace
* Contributors: davidfernandez, victor

2.0.5 (2020-05-14)
------------------
* updated basic nav cfg
* updated rviz config
* Contributors: Procópio Stein, procopiostein

2.0.4 (2020-05-14)
------------------

2.0.3 (2019-09-23)
------------------
* mapping uses scan_raw
* Contributors: Procópio Stein

2.0.2 (2019-09-18)
------------------

2.0.1 (2019-09-12)
------------------
* Merge branch 'velodyne' into 'erbium-devel'
  added launch file for velodyne laser
  See merge request robots/tiago_navigation!50
* remove pmb2_2dnav dependency with new navigation_cfg usage
* Contributors: Sai Kishor Kothakota, Victor Lopez

2.0.0 (2019-06-17)
------------------
* added robot related dependencies
* added pal_navigation_cfg_tiago dependency
* moved config and launch to pal_navigation_cfg_tiago
* Contributors: Procópio Stein, Sai Kishor Kothakota

1.0.7 (2019-03-22)
------------------
* Merge branch 'fix-nav-test' into 'erbium-devel'
  do not shutdown costmaps
  See merge request robots/tiago_navigation!48
* do not shutdown costmaps
* Contributors: Procópio Stein

1.0.6 (2019-03-15)
------------------
* Merge branch 'teb_planner' into 'erbium-devel'
  Add configuration for TEB planner
  See merge request robots/tiago_navigation!45
* Add configuration for TEB planner
* Contributors: Victor Lopez, davidfernandez

1.0.5 (2019-02-13)
------------------

1.0.4 (2019-02-05)
------------------
* Add missing exec depend
* Contributors: Victor Lopez

1.0.3 (2019-01-24)
------------------
* Decrease yaw tolerance for eband planner for public simulation
* Contributors: Victor Lopez

1.0.2 (2018-12-21)
------------------

1.0.1 (2018-12-20)
------------------
* Fix typo
* Contributors: Victor Lopez

1.0.0 (2018-12-19)
------------------
* Merge branch 'specifics-refactor' into 'erbium-devel'
  Specifics refactor
  See merge request robots/tiago_navigation!42
* Add rgbd cloud
* Add latch_xy_goal_tolerance: true to pal local planner
* mapping_karto will call pmb2's mapping_karto
* Add rgbd_sensors parameter
* Contributors: Victor Lopez

0.12.11 (2018-10-26)
--------------------
* simplified recoveries for simple navigation
* reduced acc x for smoothness
* mirrowed recoveries from pmb2 plus rotate recovery
* added dummy recovery
* added vo clearing in recovery behavior
* vo_layer uses base frame, greatly improves large maps costmap loops
* increase max vel to 0.5 m/s
* Contributors: Procópio Stein

0.12.10 (2018-09-28)
--------------------
* output move base log to screen
* Contributors: Procópio Stein

0.12.9 (2018-09-26)
-------------------
* changed param name from threshold to max_threshold
* removed deprecated param
* 0.12.8
* changelog
* Merge branch 'fix-collision-avoidance' into 'dubnium-devel'
  adjust local planner plan params
  See merge request robots/tiago_navigation!35
* adjust local planner plan params
* Contributors: Procópio Stein

0.12.7 (2018-09-17)
-------------------
* updated rviz config
* updated maintainers and license
* updated karto config to use max range and less updates
* updated plp params format
* avoid narrow passages, use same config of pmb2
* updated costmap config from specifics
* Contributors: Procópio Stein

0.12.6 (2018-07-23)
-------------------
* Merge branch 'update-amcl-params' into 'dubnium-devel'
  updated the amcl config to match the specifics template
  See merge request robots/tiago_navigation!31
* updated the amcl config to match the specifics template
* Contributors: Procópio Stein, Victor Lopez

0.12.5 (2018-04-24)
-------------------
* Revert "avoid oscillating global path and prefer shorter paths"
  This reverts commit 3f808b86f7e19c9dea9d647615b44b1ff53fba9c.
* avoid oscillating global path and prefer shorter paths
* Contributors: Procópio Stein

0.12.4 (2018-03-21)
-------------------
* Add tf_prefix and multiple arguments for consistency
* Contributors: Victor Lopez

0.12.3 (2018-03-08)
-------------------

0.12.2 (2018-02-15)
-------------------
* Merge branch 'respawn-move-base' into 'dubnium-devel'
  added respawn flag to move_base.launch
  See merge request robots/tiago_navigation!27
* added respawn flag to move_base.launch
* Contributors: Jordi Pages, Procópio Stein

0.12.1 (2018-02-02)
-------------------
* Merge branch 'remove-rgbd-layers' into 'dubnium-devel'
  removed rgbd layers from base config
  Closes #1
  See merge request robots/tiago_navigation!26
* restored changes in public sim files
* removed rgbd layers from base config
* Contributors: Procópio Stein

0.12.0 (2018-02-01)
-------------------

0.11.5 (2018-01-11)
-------------------
* allow alternative goals if original is blocked
* Contributors: Procópio Stein

0.11.4 (2017-11-27)
-------------------
* increased rot vel, adjusted footprint
* use only one aggressive costmap clearing and a rotate recovery
* Contributors: Procópio Stein

0.11.3 (2017-11-07)
-------------------
* shutdown costmaps when the robot is not moving
* Contributors: Jordi Pages

0.11.2 (2017-11-07)
-------------------

0.11.1 (2017-11-02)
-------------------
* update rviz config file for advanced navigation
  - Disable by default the navfn potential viewer
  - Add rgbd_scan viewer
* Contributors: Jordi Pages

0.11.0 (2017-10-17)
-------------------
* updated parameter due to refactoring in pal-local-planner
* Contributors: Procópio Stein

0.10.2 (2017-09-19)
-------------------
* updated params to new pal local planner
* Contributors: Procópio Stein

0.10.1 (2017-08-09)
-------------------
* added the first_map_only parameter for the amcl used with topic
* fixed the pose.yaml files for multi tiago
* fix empty tf_prefix in navigation.sh calling
* Contributors: AleDF

0.10.0 (2017-05-30)
-------------------
* removed deprecated launch
* Contributors: Procópio Stein

0.9.15 (2017-05-08)
-------------------
* improved move_base goal status management
* minor verbosity changes
* enable disable head mgr through action client
* moved subscriber init down to avoid callback before completing init
* Contributors: Procópio Stein

0.9.14 (2017-05-05)
-------------------
* elevates torso and talks to head manager when navigating
* Contributors: Procópio Stein

0.9.13 (2017-05-04)
-------------------
* added navigation camera manager script and inst rules
* removed pointcloud_to_laserscan entries and files
  the pointcloud to laserscan files were moved to specific tools
  they will be available only if advanced navigation is active
* reduced planner patience to 0.1
* tweaked global planner params
* added launch and config for rgbd_scan
* reduced max rot vel and adde time offset for all laser configs
* local planner config to new version of planner
* doubled mapping resolution and tweaked some params
* adde dock panel in rviz
* Allow multiple Tiagos on a single Gazebo
* Contributors: Procópio Stein, davidfernandez

0.9.12 (2016-12-21)
-------------------

0.9.11 (2016-10-27)
-------------------
* Update global_planner.yaml, commented neutral_cost
* added param config to activate global planner special behaviors:
  1. reuse last valid path if goal becames blocked
  2. (commented) try alternative goto points inside a radius if original is blocked
* Contributors: Procópio Stein

0.9.10 (2016-10-25)
-------------------
* enable rgbd layer for obstacle avoidance
* Contributors: Jordi Pages

0.9.9 (2016-10-21)
------------------
* fix rviz config file
* add proper obstacle layers in recovery mode yaml
* visualize RGBD laser scan. Refs #14514
* refs #14514: project RGBD pointcloud to laserscan
* fixes #14514
* fixes #14512, #14514
* remove tab
* fix arg not being assigned
* remove typo
* remove commented lines in public sim config files
* public simulation for tiago including navigation
  refs #14239
* Contributors: Jordi Pages

0.9.8 (2016-07-28)
------------------
* Add advanced navigation rviz file
* Contributors: Victor Lopez

0.9.7 (2016-06-22)
------------------
* move_base config file base path param
* Contributors: Jeremie Deray

0.9.6 (2016-06-15)
------------------
* update rviz conf to add sonars
* Contributors: Jeremie Deray

0.9.5 (2016-06-10)
------------------
* update rviz with sonars & POI
* add rviz launch file
* update rviz conf
* Contributors: Jeremie Deray

0.9.4 (2016-03-30)
------------------
* increase karto scan range threshold
* record scan
* new laser launch
* meld pmb2_2dnav tiago_2dnav
* add laser_filter conf
* missing nav debug scripts
* Improved parameters for actually creating map, its not perfect, but it works
* Hokuyo laser max range is 5 meters instead of 10 in the sick
* Copied parameters tested on stockbot for navigation
* Contributors: Jeremie Deray, Jordi Adell, Sammy Pfeiffer

0.9.3 (2015-04-14)
------------------

0.9.2 (2015-01-20)
------------------

0.9.1 (2015-01-20)
------------------
* refs #10237 : removes rgbd sensor from navigation
  This is still experimental in ant... in the future it could be taken
  from there
* disables saving initial params
  NOTE this generates 1 socket every time a param is set
* renames to tiago (TiaGo)
* Contributors: enriquefernandez
