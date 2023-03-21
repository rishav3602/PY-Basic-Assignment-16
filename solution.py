## Questions..

"""
1. Create a list called years_list, starting with the year of your birth, and each year thereafter until
the year of your fifth birthday. For example, if you were born in 1980. the list would be years_list =
[1980, 1981, 1982, 1983, 1984, 1985].
2. In which year in years_list was your third birthday? Remember, you were 0 years of age for your
first year.
3.In the years list, which year were you the oldest?
4. Make a list called things with these three strings as elements: &quot;mozzarella&quot;, &quot;cinderella&quot;,
&quot;salmonella&quot;.
5. Capitalize the element in things that refers to a person and then print the list. Did it change the
element in the list?
6. Make a surprise list with the elements &quot;Groucho,&quot; &quot;Chico,&quot; and &quot;Harpo.&quot;
7. Lowercase the last element of the surprise list, reverse it, and then capitalize it.
8. Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is
chien, cat is chat, and walrus is morse.
9. Write the French word for walrus in your three-word dictionary e2f.
10. Make a French-to-English dictionary called f2e from e2f. Use the items method.
11. Print the English version of the French word chien using f2e.
12. Make and print a set of English words from the keys in e2f.
13. Make a multilevel dictionary called life. Use these strings for the topmost keys: &#39;animals&#39;, &#39;plants&#39;,
and &#39;other&#39;. Make the &#39;animals&#39; key refer to another dictionary with the keys &#39;cats&#39;, &#39;octopi&#39;, and
&#39;emus&#39;. Make the &#39;cats&#39; key refer to a list of strings with the values &#39;Henri&#39;, &#39;Grumpy&#39;, and &#39;Lucy&#39;.
Make all the other keys refer to empty dictionaries.
14. Print the top-level keys of life.
15. Print the keys for life[&#39;animals&#39;].
16. Print the values for life[&#39;animals&#39;][&#39;cats&#39;]
"""

## Answers...

"""
1. years_list = [ 2002, 2003, 2004, 2005, 2006, 2007]

---------------------------------------------------------------------------------------------

2. If the birth year is 2002, then the year of the third birthday would be 2005 (since the person was 0 in 2002 and turns 3 in 2005).

---------------------------------------------------------------------------------------------

3.The year in years_list in which the person is the oldest would be the last year in the list, which is 2007.

---------------------------------------------------------------------------------------------

4. things = ["mozzarella", "cinderella", "salmonella"]

---------------------------------------------------------------------------------------------

5. things[1] = things[1].capitalize(), Yes, it changes the element in the list.

---------------------------------------------------------------------------------------------

6. surprise_list = ["Groucho", "Chico", "Harpo"]

---------------------------------------------------------------------------------------------

7. surprise_list[-1] = surprise_list[-1].lower()[::-1].capitalize()

---------------------------------------------------------------------------------------------

8. e2f = {"dog": "chien", "cat": "chat", "walrus": "morse"}

---------------------------------------------------------------------------------------------

9.The French word for walrus in the e2f dictionary is "morse".

---------------------------------------------------------------------------------------------

10.f2e = {value: key for key, value in e2f.items()}

---------------------------------------------------------------------------------------------

11. The English version of the French word "chien" is "dog".

---------------------------------------------------------------------------------------------

12. An English words set can be created with the following code: set(e2f.keys()).

---------------------------------------------------------------------------------------------

13. life = {"animals": {"cats": ["Henri", "Grumpy", "Lucy"], "octopi": {}, "emus": {}}, "plants": {}, "other": {}}

---------------------------------------------------------------------------------------------

14. The top-level keys of life can be printed with the following code: print(life.keys())

---------------------------------------------------------------------------------------------

15. The keys for life["animals"] can be printed with the following code: print(life["animals"].keys())

---------------------------------------------------------------------------------------------

16. The values for life["animals"]["cats"] can be printed with the following code: print(life["animals"]["cats"])

---------------------------------------------------------------------------------------------

"""