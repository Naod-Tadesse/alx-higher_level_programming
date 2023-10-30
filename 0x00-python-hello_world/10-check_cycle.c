#include "lists.h"


/**
 * check_cycle - checker function if a singly linked list has cycle
 * @list: pointer to first node
 * Return: return 1 if it is circular, 0 other way
 */

int check_cycle(listint_t *list)
{
	listint_t *present = list, *next_element = list;

	while (present && next_element && next_element->next)
	{
		present = present->next;
		next_element = next_element->next->next;
		if (present == next_element)
		{
			return (1);
		}
	}
	return (0);
}
