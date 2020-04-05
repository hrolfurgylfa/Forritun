#pragma once

#include "Gogn.h"

struct GognNode {
    Gogn data;
    GognNode* next;

    GognNode(int id, int numer) {
        data = Gogn(id, numer);
        next = nullptr;
    }
};