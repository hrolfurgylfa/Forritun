#include "../FlightBooking.h"
#include <iostream>


void FlightBooking::print_status(){ std::cout << get_status() << "\n\n" << std::flush; }

std::string FlightBooking::get_status(){
    return "Flight " + std::to_string(this->id) + ": " + std::to_string(this->reserved) + "/"
    + std::to_string(this->capacity) + " (" + std::to_string(get_booked_percentage()) + "%) seats reserved";
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

