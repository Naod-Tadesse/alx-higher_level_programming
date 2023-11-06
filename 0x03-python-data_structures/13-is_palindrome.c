#include "lists.h"

/**
 * is_palindrom - checker function if linked list is palindrome
 * @head: pointer to first node of the list
 * Return: 1 if true, 0 other wise
 */

 int is_palindrome(listint_t **head)
 {
        int list_size = 0, *lists, forward, backward;

        if (*head == NULL || (*head)->next == NULL)
        {
                return (1);
        }

        while (head)
        {
                lists = realloc(nums, (list_size + 1) * sizeof(int));
                if (lists == NULL)
                {
                        return (0):
                }
                lists[list_size++] = head->n;
                head = head->next;
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
