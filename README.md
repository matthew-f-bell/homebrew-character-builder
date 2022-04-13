# About Homebrew Character Builder App
The Homebrew Character Builder App is built with Django and styled with SASS.

This app displays user made characters for Dungeons and Dragons or Pathfinder. Characters can have a photo if using an image url. Each character is in further detail on a Detail page and shows all the specific stats of a character. Each Detail page allows the Characters Creator to update and delete their character.

The live version of this app can be viewed [here](https://homebrew-character-builder.herokuapp.com/).

## **Built With**
- HTML
- [SASS](https://sass-lang.com/documentation)
- [Python](https://docs.python.org/3/)
- [Django](https://docs.djangoproject.com/en/4.0/)

## ERD
![ERD](Prep/fixed-erd.jpg)

## User Story
![User Story](Prep/fixed-user-story.jpg)

## Wireframe
![Wireframe](Prep/fixed-wireframes.jpg)

## Known Bugs
When creating a new character does not save Character Class and Spells but, will update when using Update in Character Details.

## Future Enhancements
- Flesh out details to look like a D&D Character sheet
- Add a D&D api
- Allow users to upload their own photos
- Limits Spells to Classes so characters can't use all spells only ones for their selected classes
- Limit number of classes to characters to 2 classes
- Add a Feats and Race Model as a many to many
- Restrict Feats to different Races
- Restrict Stats total to not exceed standard character build as mentioned in the official D&D Player Handbook
- Add "dice" to create random stats