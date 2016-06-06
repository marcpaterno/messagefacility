#ifndef MessageLogger_ELextendedID_h
#define MessageLogger_ELextendedID_h

#include "messagefacility/MessageLogger/ELseverityLevel.h"

namespace mf {

  struct ELextendedID {
  public:
    std::string     process {};
    std::string     id {};
    ELseverityLevel severity {};
    std::string     module {};
    std::string     subroutine {};
    std::string     hostname {};
    std::string     hostaddr {};
    std::string     application {};
    long            pid {};

    bool operator<(ELextendedID const& xid) const;
    void clear();
  };

}        // end of namespace mf


#endif  // MessageLogger_ELextendedID_h

// Local variables:
// mode: c++
// End:
