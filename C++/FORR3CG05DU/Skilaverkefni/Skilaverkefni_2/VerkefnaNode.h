#pragma once

#include "Verkefni.h"

struct VerkefnaNode {
    Verkefni data;
    VerkefnaNode* next;

    VerkefnaNode(Verkefni verkefni) {
        this->data = verkefni;
        this->next = nullptr;
    }
};