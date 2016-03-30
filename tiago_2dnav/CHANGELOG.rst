^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package tiago_2dnav
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------
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
