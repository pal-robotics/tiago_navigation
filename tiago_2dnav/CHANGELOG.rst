^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tiago_2dnav
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
