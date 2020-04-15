#include "FlightBooking.h"
#include <iostream>


void print_program_help_info(){
    std::cout
    << "help - Get this help information" << "\n"
    << "\n"
    << "create [id] [capacity] - Create a flight with the specified id and capacity." << "\n"
    << "delete [id] - Delete a flight with the specified id." << "\n"
    << "\n"
    << "add [id] [n] - Add n passengers to the specified flight." << "\n"
    << "cancel [id] [n] - Cancel n passengers from the specified flight." << "\n"
    << "\n"
    << "info [id] - Get information about the specified flight." << "\n"
    << "allinfo - Get information about all the registerd flights, no matter if they are in use." << "\n"
    << "\n"
    << "exit - Exit the program" << "\n"
    << "\n" << std::flush;
}

FlightBooking* finna_flug(int id, FlightBooking** all_flights, int max_flights){

    // Finna flugið sem var beðið um
    for (int i = 0; i < max_flights; i++)
    {
        FlightBooking current_flight = **(all_flights+i);
        if (current_flight.get_flight_id() == id) {
            return *(all_flights+i);
        }
    }
    return NULL;
}

FlightBooking** finna_flug_ptr(int id, FlightBooking** all_flights, int max_flights){

    // Finna flugið sem var beðið um
    for (int i = 0; i < max_flights; i++)
    {
        FlightBooking current_flight = **(all_flights+i);
        if (current_flight.get_flight_id() == id) {
            return all_flights+i;
        }
    }
    return NULL;
}
