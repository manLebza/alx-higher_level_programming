#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse -> reverses the second half of list
 * @h_r: head of the other quater of the list
 * Return: 0
 */

void reverse(listint_t **h_r)
{
	listint_t *prv;
	listint_t *crr;
	listint_t *nxt;

	prv = NULL;
	crr = *h_r;

	while (crr != NULL)
	{
		nxt = crr->next;
		crr->next = prv;
		prv = crr;
		crr = nxt;
	}
	*h_r = prv;
}

/**
 * compare -> compares ints in list
 * @h1: head in first half of the list
 * @h2: head in second half of the list
 * Return: 1 if equals, 0 if not
 */

int compare(listint_t *h1, listint_t *h2)
{
	listint_t *tmp1;
	listint_t *tmp2;

	tmp1 = h1;
	tmp2 = h2;

	while (tmp1 != NULL && tmp2 != NULL)
	{
		if (tmp1->n == tmp2->n)
		{
			tmp1 = tmp->next;
			tmp2 = tmp2->next;
		}
		else
		{
			return (0);
		}
	}
	if (tmp1 == NULL && tmp2 == NULL)
	{
		return (1);
	}
	return (0);
}

/**
 * is_palindrome -> checks if singly list is palindrome
 * @head: pointer to haed of the list
 * Return: 0 if not palindrome, 1 if its is
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *prev_slow;
	listint_t *scn_half, *middle;
	int isp;

	slow = fast = prev_slow = *head;
	middle = NULL;
	isp = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fast != NULL && fast->next != NULL)
		{
			fast = fast->next->next;
			prev_slow = slow;
			slow = slow->next;
		}
		if (fast != NULL)
		{
			middle = slow;
			slow = slow->next;
		}
		scn_half = slow;
		prev_slow->next = NULL;
		reverse(&scn_half);
		isp = compare(*head, scn_half);

		if (middle != NULL)
		{
			prev_slow->next = middle;
			middlew->next = scn_half;
		}
		else
		{
			prev_slow->next = scn_half;
		}
	}
	return (isp);
}
