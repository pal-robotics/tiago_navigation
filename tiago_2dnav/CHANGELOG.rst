^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tiago_2dnav
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------
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
* disables saving initial_ params
  NOTE this generates 1 socket every time a param is set
* renames to tiago (TiaGo)
* Contributors: enriquefernandez
