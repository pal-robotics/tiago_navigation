#include <pal_core/util/init.h>
#include <pal_core/qa/logger.h>
#include <pal_core/sys/SigHandler.h>

#include "ant_nav_cont_test/NavActClientReporter.h"

int
main(int argc, char *argv[])
{
  pal::util::init(argc, argv);

  PAL_INFO("\n\n\t--> Starting navigationReporterTest\n.");

  pal::slam::NavActClientReporter nac_reporter;

  while(!pal::sys::SigHandler::singleton().isInterrupted())
  {
    nac_reporter.callAvailable();

    sleep (5);
  }
  return 0;
}
