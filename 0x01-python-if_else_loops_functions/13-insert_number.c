#include "lists.h"

/**
 * insert_node - inserts a  number in specific postion in ordered linked list
 * @head: pointer to the linked list
 * @number: the number to insert in the node
 *
 * Return: address of the node created, NULL if it is not created
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *present = *head, *swap = NULL;
	listint_t *new = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (present != NULL && present->n < number)
	{
		swap = present;
		present = present->next;
	}
	new->next = present;
	swap->next = new;

	return (new);
}
