#include "../FlightBooking.h"
#include <iostream>


bool FlightBooking::operator>(FlightBooking& other){ return this->capacity > other.capacity; }
bool FlightBooking::operator<(FlightBooking& other){ return other > *this; }
bool FlightBooking::operator>=(FlightBooking& other){ return !(*this < other); }
bool FlightBooking::operator<=(FlightBooking& other){ return !(*this > other); }

bool FlightBooking::operator==(FlightBooking& other){ return this->id == other.id; }
bool FlightBooking::operator!=(FlightBooking& other){ return !(*this == other); }

std::ostream& operator<<(std::ostream& ostr, FlightBooking& flight){ return ostr << flight.get_status(); }