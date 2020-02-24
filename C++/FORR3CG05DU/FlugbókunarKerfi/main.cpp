// Headers
#include "FlightBooking.h"

// Class Functions
#include "Class_Functions/Constructors_FlightBooking.hpp"
#include "Class_Functions/Functions_FlightBooking.hpp"
#include "Class_Functions/Getters_setters_FlightBooking.hpp"
#include "Class_Functions/Overloads_FlightBooking.hpp"

// Other functions
#include "individual_functions_FlightBooking.hpp"

#include <iostream>
#include <string>
#include <sstream>


int main(){
    std::cout << "Program starting\n" << std::flush;
    FlightBooking* booking[10];
    int max_flights = sizeof(booking) / sizeof(booking[0]);

    // Fill the booking array
    for (int i = 0; i < max_flights; i++)
        booking[i] = new FlightBooking();


    std::string input_strengur, skipun;
    do {
        // Read the command from the user
        std::cout << ">>> " << std::flush;
        std::getline(std::cin, input_strengur);

        // Parse the command
        std::stringstream ss;
        ss << input_strengur;
        ss >> skipun;

        if (skipun == "" || skipun == "help") {
            print_program_help_info();
        } else if (skipun == "create") {

            // Initialize variables 
            int id = 0;
            int capacity = 0;
            ss >> id >> capacity;

            // Checks
            // Passa að ID sé ekki 0
            if (id == 0) {
                std::cout << "Það er ekki hægt að hafa flug með ID 0.\n\n" << std::flush;
                continue;
            }
            // Passa að það sé ekki núþegar flug með sama ID
            else if (finna_flug(id, booking, max_flights) != NULL) {
                std::cout << "Þetta ID  núþegar tekið.\n\n" << std::flush;
                continue;
            }
            // passa að capacity sé ekki sett of lágt
            else if (capacity <= 0) {
                std::cout << "Það verður að vera pláss fyrir að minsta kosti einn farþega.\n\n" << std::flush;
                continue;
            }
            
            // Finna tómt flug til þess að skrifa yfir
            FlightBooking** fundid_flug_ptr = finna_flug_ptr(0, booking, max_flights);
            if (!fundid_flug_ptr) {
                std::cout << "Öll flugin eru full.\n\n" << std::flush;
                continue;
            }

            // Bæta fluginu við
            *fundid_flug_ptr = new FlightBooking(id, capacity, 0);


        } else if (skipun == "delete") {

            // Initialize variables 
            int id = 0;
            ss >> id;

            // Checks
            // Passa að ID sé ekki 0
            if (id == 0) {
                std::cout << "Það er ekki hægt að hafa flug með ID 0.\n\n" << std::flush;
                continue;
            }
            
            // Finna flugið
            FlightBooking** fundid_flug_ptr = finna_flug_ptr(id, booking, max_flights);
            if (!fundid_flug_ptr) {
                std::cout << "Flugið sem þú valdir var ekki fundið.\n\n" << std::flush;
                continue;
            }

            // Eyða gamla fluginu
            delete *fundid_flug_ptr;

            // Bæta fluginu við
            *fundid_flug_ptr = new FlightBooking();


        } else if (skipun == "add") {

            // Initialize variables 
            int id = 0;
            int number_to_add = 0;
            ss >> id >> number_to_add;

            // Checks
            // Passa að ID sé ekki 0
            if (id == 0) {
                std::cout << "Það er ekki hægt að hafa flug með ID 0.\n\n" << std::flush;
                continue;
            }
            // passa að það sé bætt við 1 eða fleirum
            else if (number_to_add <= 0) {
                std::cout << "Það verður að bæta við einum eða fleiri farðegum.\n\n" << std::flush;
                continue;
            }
            
            // Finna flugið
            FlightBooking* fundid_flug_ptr = finna_flug(id, booking, max_flights);
            if (!fundid_flug_ptr) {
                std::cout << "Flugið sem þú baðst um var ekki fundið.\n\n" << std::flush;
                continue;
            }

            // Bæta farðegunum við
            int result = (*fundid_flug_ptr).book_seats(number_to_add);
            if (result == 1) std::cout << "Their are not enough seats available.\n\n" << std::flush;


        } else if (skipun == "cancel") {

            // Initialize variables 
            int id = 0;
            int number_to_cancel = 0;
            ss >> id >> number_to_cancel;

            // Checks
            // Passa að ID sé ekki 0
            if (id == 0) {
                std::cout << "Það er ekki hægt að hafa flug með ID 0.\n\n" << std::flush;
                continue;
            }
            // passa að það sé bætt við 1 eða fleirum
            else if (number_to_cancel <= 0) {
                std::cout << "Það verður að fjarlægja einn eða fleri farþega.\n\n" << std::flush;
                continue;
            }
            
            // Finna flugið
            FlightBooking* fundid_flug_ptr = finna_flug(id, booking, max_flights);
            if (!fundid_flug_ptr) {
                std::cout << "Flugið sem þú baðst um var ekki fundið.\n\n" << std::flush;
                continue;
            }

            // Bæta farðegunum við
            int result = (*fundid_flug_ptr).unbook_seats(number_to_cancel);
            if (result == 1) std::cout << "Það eru ekki svona margir skráðir á flugið.\n\n" << std::flush;


        } else if (skipun == "allinfo") {

            for (int i = 0; i < max_flights; i++)
                (*booking[i]).print_status();


        } else if (skipun == "info") {

            // Initialize variables 
            int id = 0;
            ss >> id;

            // Checks
            // Passa að ID sé ekki 0
            if (id == 0) {
                std::cout << "Það er ekki hægt að hafa flug með ID 0.\n\n" << std::flush;
                continue;
            }
            
            // Finna flugið
            FlightBooking* fundid_flug_ptr = finna_flug(id, booking, max_flights);
            if (!fundid_flug_ptr) {
                std::cout << "Flugið sem þú baðst um var ekki fundið.\n\n" << std::flush;
                continue;
            }
            FlightBooking flug = *fundid_flug_ptr;

            // Sýna niðurstöðuna
            flug.print_status();

        
        } else if (skipun == "test") {

            FlightBooking a(1, 80, 30);
            FlightBooking b(1, 50, 20);

            if (b < a) std::cout << "Works!" << "\n" << std::flush;
            std::cout << a << "\n" << b << "\n\n";


        } else if (skipun == "exit") {
            std::cout << "Exiting program..." << "\n" << std::flush;
        } else {
            std::cout << "The command you put in was not recognized, do help to check all available commands.\n" << "\n" << std::flush;
        }

    } while (skipun != "exit");
    
    return 0;
}