#include "lists.h"


/**
 * check_cycle - checker function if a singly linked list has cycle
 * @list: pointer to first node
 * Return: return 1 if it is circular, 0 other way
 */

int check_cycle(listint_t *list)
{
	listint_t *present , *next_element;

	if (list == NULL)
	{
		return (0);
	}

	present = list->next;
	next_element = list->next->next;

	while (present && next_element && next_element->next)
	{
		if (present == next_element)
		{
			return (1);
		}

		present = present->next;
		next_element = next_elemtn->next->next;
	}
	return (0);
}
