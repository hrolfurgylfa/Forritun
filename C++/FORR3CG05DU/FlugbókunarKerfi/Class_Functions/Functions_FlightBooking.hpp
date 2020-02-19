#include "../FlightBooking.h"
#include <iostream>


void FlightBooking::print_status(){
    std::cout
    << "Flight " << this->id << ": " << this->reserved << "/" << this->capacity
    << " (" << get_booked_percentage() << "%) seats reserved"
    << "\n\n" << std::flush;
}

int FlightBooking::get_booked_percentage(){
    if (this->capacity != 0) {
        return (this->reserved*100)/this->capacity;
    } else {
        return 0;
    } 
}

int FlightBooking::book_seats(int number_of_seats){
    if (this->reserved + number_of_seats <= this->capacity) {
        this->reserved += number_of_seats;
        return 0;
    } else { return 1; }
}

int FlightBooking::unbook_seats(int number_of_seats){
    if (this->reserved - number_of_seats >= 0) {
        this->reserved -= number_of_seats;
        return 0;
    } else { return 1; }
}

void FlightBooking::setup(int id, int capacity){
    this->id = id;
    this->capacity = capacity;
    this->reserved = 0;
}