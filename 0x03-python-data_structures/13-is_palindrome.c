#include "lists.h"

#define ARR_SIZE 1024

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to the head of the singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int arr[ARR_SIZE];
	int i, j;
	listint_t *h;

	i = j = 0;
	if (head != NULL)
	{
		h = *head;
		while (h != NULL)
		{
			arr[i] = h->n;
			h = h->next;
			i++;
		}
		while (j < (i / 2))
		{
			if (arr[j] != arr[i - j - 1])
				return (0);
			j++;
		}
	}
	return (1);
}
