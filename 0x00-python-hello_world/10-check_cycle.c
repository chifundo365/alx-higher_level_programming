#include "lists.h"

/**
 * check_cycle - checks if linked list has a cycle
 * @list:pointer to the head of the list
 * Return: 1 if lonked list has a cycle or -1
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	if (!list)
		return (0);

	while (fast)
	{
		if (fast == slow)
			return (1);
		fast = fast->next;
		if (!fast)
		{
			return (0);
		}
		else
		{
			fast = fast->next;
		}

		slow = slow->next;
	}

	return (0);
}
