#include <bits/stdc++.h>
#include <iostream>



struct Node {
    int data;
    Node* next;
};




int main()
{
    Node* head = NULL;
    Node* second = NULL;
    Node* tail = NULL;





    // allocate 3 nodes in the heap

    head = new Node;
    second = new Node;
    tail = new Node;

    head->data = 1; // assign data in first node
    head->next = second; // Link first node with
    // the second node
    second->data = 2;
    second->next = tail;

    tail->data = 3;
    tail->next = NULL;

    //Add node with value 10 to start of list

    Node** oldhead = &head;

    Node* newhead = new Node;

    newhead->data = 10;

    newhead->next = (*oldhead);

    (*oldhead) = newhead;



    //Add node with value 20 to end of List

    Node* newtail = new Node;

    Node *last = *oldhead;



    newtail->data = 20;

    newtail->next = NULL;

    while (last->next != NULL)
    last = last->next;

/* 6. Change the next of last node */
    last->next = newtail;


    Node* n = head;
    while (n != NULL) {
        std::cout << n->data << std::endl;
        n = n->next;
    }

    return 0;

}
