//#define NDEBUG

#include <iostream>

#include "MessageLogger/interface/MessageLogger.h"
#include "boost/thread.hpp"

void anotherLogger()
{
  // Set module name
  mf::SetModuleName("anotherLogger");

  LogWarning("warn1 | warn2") << "Followed by a WARNING message.";
  LogDebug("debug")           << "The debug message in the other thread";

  return;
}

int main()
{
  // Start MessageFacility Service
  mf::StartMessageFacility(
      mf::MessageFacilityService::MultiThread, 
      mf::MessageFacilityService::logCFS());

  // Set module name for the main thread
  mf::SetApplicationName("MessageFacility");
  mf::SetModuleName("MFTest");
  mf::SetContext("pre-event");

  // Start up another logger in a seperate thread
  boost::thread loggerThread(anotherLogger);

  // Issue messages with different severity levels
  LogError("err1|err2") << "This is an ERROR message.";
  LogWarning("warning") << "Followed by a WARNING message.";

  // Switch context
  mf::SetContext("pro-event");

  // Log Debugs
  LogDebug("debug")     << "DEBUG information.";
  LogDebug("debug")     << "DEBUG information.";
  LogDebug("debug")     << "DEBUG information.";

  // Thread join
  loggerThread.join();

  mf::LogStatistics();

  return 0;
}
