#include "../FlightBooking.h"
#include <iostream>


FlightBooking::FlightBooking(){
    this->id = 0;
    this->capacity = 0;
    this->reserved = 0;
}

FlightBooking::FlightBooking(int id, int capacity, int reserved){
    this->id = id;
    this->capacity = capacity;
    this->reserved = reserved;
}