#include "lists.h"

/**
 * create_node - creates a node
 * @number: a number to insert in the node 'n' member
 * Return: pointer to the new node or NULL
 */
listint_t *create_node(int number)
{
	listint_t *new_node = (listint_t *)malloc(sizeof(listint_t));

	if (new_node)
	{
		new_node->n = number;
		new_node->next = NULL;

		return (new_node);
	}

	return (NULL);
}
/**
 * insert_node - insert a number into a sorted  linked-list
 * @head: pointer to a pointer to the first element of list
 * @number: the number to insert in the created node
 * Return: pointer to the newly created noe or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = create_node(number);
	listint_t *fast, *slow = *head;

	if (new_node)
	{
		if (*head == NULL)
		{
			*head = new_node;

			return (new_node);
		}

		fast = (*head)->next;
		while (fast)
		{
			if (slow->n >= new_node->n)
			{
				new_node->next = slow;
				*head = new_node;

				return (new_node);
			}
			else if (fast->n >= new_node->n || !fast)
			{
				slow->next = new_node;
				new_node->next = fast;

				return (new_node);
			}

			fast = fast->next;
			slow = slow->next;
		}
	}

	return (NULL);
}
