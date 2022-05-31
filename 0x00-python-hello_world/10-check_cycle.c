#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * Used the `Floyd's Cycle-Finding Algorithm`
 * @list: head of a linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle, -1 on error
 */
int check_cycle(listint_t *list)
{
	listint_t *one_step, *two_steps;

	if (list == NULL)
		return (0);
	one_step = list;
	two_steps = list->next;

	while (two_steps != NULL)
	{
		if (one_step == two_steps)
			return (1);
		one_step = one_step->next;
		if (two_steps->next == NULL)
			break;
		two_steps = (two_steps->next)->next;
	}
	return (0);
}
