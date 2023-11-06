#include "lists.h"
#include <stdlib.h>
/**
 * is_palindrome - checker function if linked list is palindrome
 * @head: pointer to first node of the list
 * Return: 1 if true, 0 other wise
 */

int is_palindrome(listint_t **head)
{
	int list_size = 0, *lists = NULL, forward, backward;
	listint_t *current = *head;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	while (current)
	{
		lists = realloc(lists, (list_size + 1) * sizeof(int));
		if (lists == NULL)
		{
			return (0);
		}
		lists[list_size++] = current->n;
		current = current->next;
	}
	forward = 0;
	backward = list_size - 1;

	while (forward <= backward)
	{
		if (lists[forward] != lists[backward])
		{
			free(lists);
			return (0);
		}
		forward++;
		backward--;
	}
	free(lists);
	return (1);
}
