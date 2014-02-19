#include "ant_nav_cont_test/NavActClientReporter.h"

#include <pal_core/qa/logger.h>
#include <pal_core/qa/supervisor/SupervisorUpdater.h>

#include <navigation_client/NavigationActionClient.h>

namespace pal
{
  namespace slam
  {
    NavActClientReporter::NavActClientReporter():
        _statusOK(false)
    {
      qa::SupervisorUpdater::addTest("navActClientContinuousTest", this,
          &NavActClientReporter::obtainStatus);
    }

    NavActClientReporter::~NavActClientReporter()
    {
      qa::SupervisorUpdater::removeTest ("navActClientContinuousTest");
    }

    void NavActClientReporter::obtainStatus(qa::SupervisorDiagnosticStatus &status)
    {
      qa::FunctionalityStatus cmdStatus (status, qa::functionality::NAVACTCLIENT);

      if (_statusOK )
        cmdStatus.appendMessage("OK");
      else
        cmdStatus.addError(qa::functionalityError::NAVIGATION_SERVICE_NOT_OK, "Not possible to connect to navigation through NavigationActionClient");
    }

    void NavActClientReporter::callAvailable()
    {
      while (!_statusOK)
      {
        try
        {
          abl::NavigationActionClient client;
          while (client.isConnected())
          {
            _statusOK = true;
            sleep(3);
          }
          _statusOK = false;
        }
        catch (util::CommonException const& e)
        {
          _statusOK = false;
        }
        sleep(3);
      }
    }
  }
}
