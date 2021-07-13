
#include <bits/stdc++.h>
#include <iostream>

class Node {
public:
    int data;
    Node* next;
};


void printList(Node* n)
{
    while (n != NULL) {
        std::cout << n->data << std::endl;
        n = n->next;
    }
}


int main()
{
    Node* head = NULL;
    Node* second = NULL;
    Node* third = NULL;





    // allocate 3 nodes in the heap

    head = new Node();
    second = new Node();
    third = new Node();

    head->data = 1; // assign data in first node
    head->next = second; // Link first node with
    // the second node
    second->data = 2;
    second->next = third;

    third->data = 3;
    third->next = NULL;

    printList(head);

    return 0;

}
