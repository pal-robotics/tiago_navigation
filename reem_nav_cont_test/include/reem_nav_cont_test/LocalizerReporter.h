/*
 *  LocalizerReporter.h
 *  Copyright (c) 2011 PAL Robotics sl. All Rights Reserved.
 *  Created on: 06-February-2012
 *  Author: Ricardo Tellez
 */


#ifndef LocalizerReporter_H
#define LocalizerReporter_H

#include <ros/node_handle.h>
#include <geometry_msgs/PoseWithCovarianceStamped.h>
#include <pal_core/sync/Mutex.h>

namespace pal
{
  namespace qa
  { struct SupervisorDiagnosticStatus; }

  namespace slam
  {
    class LocalizerReporter
    {

      public:
        LocalizerReporter ();
        ~LocalizerReporter ();

        /**
        * Function to be called by the supervisor to obtain the current status of the service
        */
        void obtainStatus(qa::SupervisorDiagnosticStatus &status) ;

        void callAvailable();

      private:
        void locCb(geometry_msgs::PoseWithCovarianceStamped const &msg) ;
        void tfCb();

        ros::NodeHandle _nh;
        ros::Subscriber _localizerPoseSub;
        ros::Subscriber _tfSub;
        ros::ServiceClient _tfClient ;
        bool _localizationOK;
        geometry_msgs::PoseWithCovarianceStamped _lastLocPos;

        sync::ThreadMutex _mutex;
    };
  }
}

#endif // LocalizerReporter_H
