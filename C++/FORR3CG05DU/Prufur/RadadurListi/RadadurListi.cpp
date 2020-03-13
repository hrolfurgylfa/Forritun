#include "RadadurListi.h"

RadadurListi::RadadurListi() { this->head = nullptr; }

// setja stak í listann
void RadadurListi::setjaILista(int id, int numer) {
    if(this->erILista(id)) return;
    if(this->head == nullptr) {
        cout << "Sett í this->head í fyrsta sinn." << endl;
        this->head = new GognNode(id, numer);
    } else {
        GognNode* nyttStak = new GognNode(id, numer);
        if(this->head->data.getID() > id) {
            nyttStak->next = this->head;
            this->head = nyttStak;
        } else {
            GognNode* current = this->head;
            GognNode* prev = this->head;
            while(current && current->data.getID() < id) {
                prev = current;
                current = current->next;
            }
            prev->next = nyttStak;
            nyttStak->next = current;
        }
    }
}

// fallið eyðir staki með id úr listanum
void RadadurListi::eydaUrLista(int id) {
    if(!this->erILista(id)) return;
    if(this->head->data.getID() == id) {
        // TODO
    } else {
        // TODO 
    }
}

// fallið skilar pointer að stakinu sem er með IDið sem er sent inn eða nullptr
GognNode* RadadurListi::finnaFyrraILista(int id) {
    cout << "this->head: " << this->head << endl;
    if (this->head == nullptr) return nullptr;

    GognNode* current_node = this->head;
    GognNode* old_node = this->head;

    while (current_node) {
        cout << "Checking ID " << current_node->data.getID() << endl;
        if (current_node->data.getID() == id) return old_node;

        old_node = current_node;
        current_node = current_node->next;
    }

    return nullptr;
}

// fallið skilar true ef stak með id er í listanum annars false
bool RadadurListi::erILista(int id) {
    GognNode* fundid_node = this->finnaFyrraILista(id);
    if (fundid_node) return true;
    else return false;
}

// fallið skrifa listann út á skjá
void RadadurListi::prentaLista() {
    if (this->head == nullptr) {
        std::cout << "Staflinn er tómur.\n" << std::flush;
        return;
    }

    GognNode* current_node = this->head;
    while (current_node != nullptr)
        current_node->data.prentaGogn();
    
    std::cout << endl;
}

// destructorinn eyðir öllum Node-unum úr listanum
RadadurListi::~RadadurListi() {
    // TODO
}