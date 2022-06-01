#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: head of the signly linked list
 * @number: number to be inserted
 *
 * Return: address of the new node, NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new, *h;

	if (*head == NULL)
	{
		*head = malloc(sizeof(listint_t));
		if (head == NULL)
			return (NULL);
		(*head)->n = number;
		(*head)->next = NULL;
		return (*head);
	}
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if ((*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (*head);
	}
	h = *head;
	while (h != NULL && (h->next) != NULL)
	{
		if (h->n <= number && (h->next)->n >= number)
		{
			temp = h->next;
			h->next = new;
			new->next = temp;
			return (*head);
		}
		h = h->next;
	}
	h->next = new;
	return (*head);
}
