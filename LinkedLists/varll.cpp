#include <bits/stdc++.h>
#include <iostream>

// Variable size linked list creation

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


// append to link list taking argument of popinter to pointer of head of linked list and the data value to be appended
void append(Node** head_ref, int new_data)
{

    // 1. allocate node
    Node* new_node = new Node();

    Node *last = *head_ref;

    // 2. Put in the data
    new_node->data = new_data;

    // 3. This new node is going to be
    // the last node, so make next of
    // it as NULL
    new_node->next = NULL;

    // 4. If the Linked List is empty,
    // then make the new node as head
    if (*head_ref == NULL)
    {
        *head_ref = new_node;
        return;
    }

    // 5. Else traverse till the last node
    while (last->next != NULL)
        last = last->next;

    // 6. Change the next of last node
    last->next = new_node;
    return;
}

int main()
{
    Node* head = NULL;

    // create linked list from 1 to 10
    for(int i = 1; i <= 10; i++)
    {
      append(&head, i);
    }


    printList(head);

    return 0;

}
