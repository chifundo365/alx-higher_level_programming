#include "lists.h"


/**
 * reverse_list - reverses a linked list
 * @head: pointer to a pointer to the 1st node
 * Return: pointer to the first node of reversed list
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *next, *current = head, *prev = NULL;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * is_palindrome - checks if a list is a palidrome
 * @head: pointer to a pointer to the first node
 * Return: 1 if palindrome else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *head2, *temp = *head, *fast = *head;

	if (!fast || !fast->next)
		return (1);

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (!fast)
		{
			head2 = reverse_list(slow);
			print_listint(head2);
			while (temp != slow)
			{
				if (temp->n != head2->n)
				{
					return (0);
				}

				temp = temp->next;
				head2 = head2->next;
			}
		}
	}

	return (1);
}

