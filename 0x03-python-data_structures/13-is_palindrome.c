#include "lists.h"

/**
 * count_list - find total number of node in list
 * @head: pointer to the start of tue list
 * Return: total number or 0
 */
int count_list(listint_t *head)
{
	int c = 0;

	while (head)
	{
		head = head->next;
		c++;
	}

	return (c);
}

/**
 * get_node_index - find node at given index
 * @head: pointer to the start of the list
 * @idx: index
 * Return: value of memeber 'n' of the node
 */
int get_node_index(listint_t *head, int idx)
{
	int i = 0;

	while (head)
	{
		if (idx == i)
			return (head->n);
		i++;
		head = head->next;
	}

	return (head->n);
}

/**
 * is_palindrome - checks if a list is a palidrome
 * @head: pointer to a pointer to the first node
 * Return: 1 if palindrome else -1
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int list_len = 0;

	if (!(*head))
		return (1);
	temp = *head;
	list_len = count_list(temp) - 1;


	while (temp)
	{
		if (temp->n != get_node_index(*head, list_len))
			return (0);
		temp = temp->next;
		list_len--;
	}

	return (1);
}

