#include "../FlightBooking.h"
#include <iostream>


int FlightBooking::get_flight_id(){ return this->id; }

int FlightBooking::get_capacity(){ return this->capacity; }
int FlightBooking::set_capacity(int capacity){
    if (this->reserved <= capacity) {
        this->capacity = capacity;
        return 0;
    } else return 1;
}