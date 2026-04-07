---
name: scrape-cooked-wiki-recipe
description: Scrape a recipe from cooked.wiki and create a JSON file in the recipe_template.json format in the recipes folder
---
## What I do
1. Fetch the cooked.wiki page using WebFetch with format "html"
2. Parse the HTML to extract:
   - The source URL from the `<a class="recipe-link">` href attribute
   - Recipe title from `<div class="title">` text content
   - All ingredients from `<li class="ingredient">` elements, extracting text from `<p>` tags inside
3. Create a slugified filename from the recipe title (e.g., "Guy's Spicy Spanish Rice" -> "guys-spicy-spanish-rice.json")
4. Create the recipes folder if it doesn't exist
5. Write a JSON file matching the recipe_template.json format:
   ```json
   {
     "cooked_url": "extracted-cooked.wiki-url",
     "source_url": "extracted-source-url",
     "title": "Extracted Title",
     "ingredients": ["ingredient 1", "ingredient 2", ...],
     "won_round_one": 0,
     "won_round_two": 0,
     "won_round_three": 0,
     "won_round_four": 0,
     "won_round_five": 0
   }
   ```

## When to use me
Use this when the user asks to scrape, import, or create a recipe JSON file from a cooked.wiki URL like:
- https://cooked.wiki/new/recent/1eb83f35-2d9d-4624-bff4-7dd4d2c4f321

## Example workflow
User: "Scrape recipe from https://cooked.wiki/new/recent/uuid"
1. Call WebFetch to get the HTML
2. Parse ingredients and URL
3. Create recipes/ folder if needed
4. Write JSON file to recipes/{snake_title}.json
5. Confirm the file location to the user
