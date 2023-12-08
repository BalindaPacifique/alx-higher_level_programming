#include "lists.h"

/**
 * print_dlistint - Prints all the elements of a dlistint_t list.
 * @h: Pointer to the head of the list.
 * Return: The number of nodes.
 */
size_t print_dlistint(const dlistint_t *h)
{
    int count_nodes = 0;

    if (h == NULL)
    {
	    return (count_nodes);
    }
    while (h -> prev != NULL)
    {
	    h = h -> prev;
    }
    while (h != NULL)
    {
        printf("%d\n", h->n);
        h = h->next;
        count_nodes++;
    }

    return count_nodes;
}
