#ifndef FLIGHT_BOOKING_H
#define FLIGHT_BOOKING_H

#include <iostream>

class FlightBooking {
public:
    //Constructors
    FlightBooking();
    FlightBooking(int id, int capacity, int reserved);


    // Getters and setters
    int get_flight_id();

    int get_capacity();
    int set_capacity(int capacity);
    int get_booked_seats();


    // Functions
    void print_status();
    std::string get_status();
    int get_booked_percentage();

    int book_seats(int number_of_seats);
    int unbook_seats(int number_of_seats);

    void setup(int id, int capacity);


    // Overloads
    bool operator>(FlightBooking& other);
    bool operator<(FlightBooking& other);
    bool operator>=(FlightBooking& other);
    bool operator<=(FlightBooking& other);

    bool operator==(FlightBooking& other);
    bool operator!=(FlightBooking& other);

private:
    int id;
    int capacity;
    int reserved;
};

std::ostream& operator<<(std::ostream& ostr, FlightBooking& flight);

#endif