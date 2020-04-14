#include "RadadurListi.h"
#include "VerkefnaNode.h"

RadadurListi::RadadurListi() { this->start = nullptr; }
RadadurListi::~RadadurListi() {
    if (this->start == nullptr) return;

    VerkefnaNode* current_node = this->start;
    while (current_node != nullptr)
    {
        VerkefnaNode* old_node = current_node;
        current_node = current_node->next;
        delete old_node;
    }
}

void RadadurListi::append(Verkefni verkefni) {
    if(this->contains(verkefni.get_lysing())) return;

    if(this->start == nullptr) {
        this->start = new VerkefnaNode(verkefni);
    } else {
        VerkefnaNode* nyttStak = new VerkefnaNode(verkefni);
        if(this->start->data.get_uniqe_mikilvaegi() < verkefni.get_uniqe_mikilvaegi()) {
            nyttStak->next = this->start;
            this->start = nyttStak;
        } else {
            // std::cout << "Going to loop!!!";
            VerkefnaNode* current = this->start;
            VerkefnaNode* prev = this->start;
            while(current && current->data.get_uniqe_mikilvaegi() > verkefni.get_uniqe_mikilvaegi()) {
                prev = current;
                current = current->next;
            }
            prev->next = nyttStak;
            nyttStak->next = current;
        }
    }
}
void RadadurListi::remove(std::string lysing) {
    if(this->start->data.get_lysing() == lysing) {
        VerkefnaNode* new_start = this->start->next;
        VerkefnaNode* old_start = this->start;
        this->start = new_start;
        delete old_start;
    } else {
        VerkefnaNode* fyrra_stak = this->find_parent(lysing);
        if(!fyrra_stak) return;// Passa að það hafi verið fundið stak
        
        // if(fyrra_stak->next->next){
        //     //Eyða venjulega
        // } else {
        //     // Það er ekkert lokastak til þess að bæta við
        // }
        
        VerkefnaNode* new_child = fyrra_stak->next->next;
        VerkefnaNode* old_child = fyrra_stak->next;
        fyrra_stak->next = new_child;
        delete old_child;
    }
}
VerkefnaNode* RadadurListi::find_parent(std::string lysing) {
    if (this->start == nullptr) return nullptr;

    VerkefnaNode* current_node = this->start;
    VerkefnaNode* old_node = nullptr;

    while (current_node) {
        if (current_node->data.get_lysing() == lysing) return old_node;

        old_node = current_node;
        current_node = current_node->next;
    }

    return nullptr;
}
bool RadadurListi::contains(std::string lysing) {
    VerkefnaNode* fundid_node = this->find_parent(lysing);
    if (fundid_node) return true;
    else return false;
}
Verkefni RadadurListi::fetch_next() {
    if (!this->start) return Verkefni();

    Verkefni return_verkefni = Verkefni(this->start->data);
    this->remove(return_verkefni.get_lysing());
    return return_verkefni;
}

void RadadurListi::print() {
    if (this->start == nullptr) {
        std::cout << "Þú hefur klárað öll verkin þín, eigðu góðan dag.\n" << std::flush;
        return;
    }

    VerkefnaNode* current_node = this->start;
    while (current_node != nullptr)
    {
        current_node->data.prenta_verkefni();
        current_node = current_node->next;
    }
}
void RadadurListi::print_school(bool only_school) {
    if (this->start == nullptr) {
        std::cout << "Þú hefur klárað öll verkin þín, eigðu góðan dag.\n" << std::flush;
        return;
    }

    VerkefnaNode* current_node = this->start;
    while (current_node != nullptr)
    {
        if (current_node->data.get_er_skola() == only_school)
            current_node->data.prenta_verkefni();
        current_node = current_node->next;
    }
}