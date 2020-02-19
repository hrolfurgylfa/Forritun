#ifndef FLIGHT_BOOKING_H
#define FLIGHT_BOOKING_H

class FlightBooking {
public:
    //Constructors
    FlightBooking();
    FlightBooking(int id, int capacity, int reserved);

    // Getters and setters
    int get_flight_id();

    // Functions
    void print_status();
    int get_booked_percentage();
    int book_seats(int number_of_seats);
    int unbook_seats(int number_of_seats);
    void setup(int id, int capacity);

private:
    int id;
    int capacity;
    int reserved;
};

#endif