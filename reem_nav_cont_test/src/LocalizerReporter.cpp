#include "reem_nav_cont_test/LocalizerReporter.h"

#include <pal_core/qa/supervisor/SupervisorUpdater.h>
#include <pal_core/qa/logger.h>
#include <pal_supervisor_msgs/lookupTransform.h>

namespace pal
{
  namespace slam
  {
    LocalizerReporter::LocalizerReporter():
    _localizationOK(false)
    {
      qa::SupervisorUpdater::addTest("localizerContinuousTest", this,
          &LocalizerReporter::obtainStatus );
      _localizerPoseSub = _nh.subscribe("/amcl_pose", 1, &LocalizerReporter::locCb, this);
      //Supervisor client to ask for transformations
      _tfClient = _nh.serviceClient<pal_supervisor_msgs::lookupTransform>("/lookupTransform");
    }

    LocalizerReporter::~LocalizerReporter()
    {
        qa::SupervisorUpdater::removeTest ("localizerContinuousTest");
    }

    void LocalizerReporter::obtainStatus(qa::SupervisorDiagnosticStatus &status)
    {
      qa::FunctionalityStatus cmdStatus (status, qa::functionality::LOCALIZER);
      sync::ThreadGuard guard(_mutex);  ///-------------------------------------

      if (_localizationOK )
        cmdStatus.appendMessage("OK");
      else
        cmdStatus.addError(qa::functionalityError::NAVIGATION_SERVICE_NOT_OK,
            "Localization is not working");

      cmdStatus.addValue("Last localization position",_lastLocPos.pose.pose.position);
      cmdStatus.addValue("Last localization orientation",_lastLocPos.pose.pose.orientation);
    }

    void LocalizerReporter::locCb(geometry_msgs::PoseWithCovarianceStamped const &msg)
    {

      sync::ThreadGuard guard(_mutex);  ///-------------------------------------

      PAL_INFO ("localization pose received");
      _lastLocPos = msg;

    }

    void LocalizerReporter::tfCb()
    {

      sync::ThreadGuard guard(_mutex);  ///-------------------------------------

      pal_supervisor_msgs::lookupTransform::Request tfreq;
      pal_supervisor_msgs::lookupTransform::Response tfres;

      tfreq.source_frame = std::string("/map");
      tfreq.target_frame = std::string("/odom");
      tfreq.transform_time = ros::Time::now();

      if(!_tfClient.call(tfreq,tfres))
      {
          PAL_ERROR("Failed to call service tf listener");
          _localizationOK = false;
      }
      else
        _localizationOK = true;
    }

    void LocalizerReporter::callAvailable()
    {
      ros::spinOnce();
      tfCb();
    }
  }
}
