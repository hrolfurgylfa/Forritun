#pragma once

#include "Gogn.h"

struct GognNode {
    Gogn data;
    GognNode* next;

    GognNode(int id, int numer) {
        this->data = Gogn(id, numer);
        this->next = nullptr;
    }
};