#ifndef NavActClientReporter_H
#define NavActClientReporter_H

namespace pal
{
  namespace qa
  { class SupervisorDiagnosticStatus; }

  namespace slam
  {
    class NavActClientReporter
    {
      public:
        NavActClientReporter ();
        ~NavActClientReporter ();

        /**
        * Function to be called by the supervisor to obtain the current status of the service
        */
        void obtainStatus(qa::SupervisorDiagnosticStatus& status) ;

        void callAvailable();

      private:
        bool _statusOK;
    };
  }
}

#endif // NavActClientReporter_H
