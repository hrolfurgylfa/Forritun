#include <iostream>
#include <string>
#include <sstream>


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

    private:
        int id;
        int capacity;
        int reserved;
};


  //////////////////
 // Constructors //
//////////////////

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


  ///////////////
 // Functions //
///////////////

void FlightBooking::print_status(){
    std::cout
    << "Flight " << this->id << ": " << this->reserved << "/" << this->capacity
    << " (" << get_booked_percentage() << "%) seats reserved"
    << "\n\n" << std::flush;
}

int FlightBooking::get_booked_percentage(){
    return (this->reserved*100)/this->capacity;
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


  /////////////////////////
 // Getters and setters //
/////////////////////////

int FlightBooking::get_flight_id(){ return this->id; }


  ///////////////
 // Stök föll //
///////////////

void print_program_help_info(){
    std::cout
    << "help - Get this help information" << "\n"
    << "add [id] [n] - Add n passengers to the specified flight." << "\n"
    << "exit - Exit the program" << "\n"
    << "\n" << std::flush;
}


  //////////
 // Main //
//////////

int main(){
    std::cout << "Program starting\n";
    FlightBooking booking[10];
    int max_flights = sizeof(booking) / sizeof(booking[0]);

    int id = 3;
    int number_to_add = 2;

    // Finna flugið sem var beðið um
    for (int i = 0; i < max_flights; i++)
    {
        FlightBooking current_flight = booking[i];
        current_flight.print_status();
    }
    std::cout << "Buid" << "\n" << std::flush;

    return 0;
}