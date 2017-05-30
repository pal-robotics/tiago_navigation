^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tiago_laser_sensors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------

0.9.15 (2017-05-08)
-------------------

0.9.14 (2017-05-05)
-------------------

0.9.13 (2017-05-04)
-------------------
* removed pointcloud_to_laserscan entries and files
  the pointcloud to laserscan files were moved to specific tools
  they will be available only if advanced navigation is active
* added launch and config for rgbd_scan
* reduced max rot vel and adde time offset for all laser configs
* added footprint laser filter
* Allow multiple Tiagos on a single Gazebo
* Contributors: Procópio Stein, davidfernandez

0.9.12 (2016-12-21)
-------------------
* add footprint filter
* Contributors: Jordi Pages

0.9.11 (2016-10-27)
-------------------
* updated dependencies, updated laser filter, normalized config files, updated pc2ls launch and config
* Contributors: Procópio Stein

0.9.10 (2016-10-25)
-------------------

0.9.9 (2016-10-21)
------------------
* fixe RGBD laser-scan frame. Refs #14514
* Contributors: Jordi Pages

0.9.8 (2016-07-28)
------------------

0.9.7 (2016-06-22)
------------------

0.9.6 (2016-06-15)
------------------

0.9.5 (2016-06-10)
------------------
* fix hokuyo port accordingly to new dev rule
* Contributors: Jeremie Deray

0.9.4 (2016-03-30)
------------------
* tiago default laser sick tim 561
* fix lasers launch
* laser launch set laser param
* update maintainer
* new laser launch
* add laser_filter conf
* rm rebujito laser
* add lasers sick 561 571
* Contributors: Jeremie Deray

0.9.3 (2015-04-14)
------------------
* Set hokuyo laser
* Contributors: Enrique Fernandez

0.9.2 (2015-01-20)
------------------

0.9.1 (2015-01-20)
------------------
* renames to tiago (TiaGo)
* Contributors: enriquefernandez
