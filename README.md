# Pur Beurre

## Histoire Fictive

La startup Pur Beurre, avec laquelle vous avez déjà travaillé, souhaite développer une plateforme web à destination de ses clients. Ce site permettra à quiconque de trouver un substitut sain à un aliment considéré comme "Trop gras, trop sucré, trop salé" (même si nous savons tous que le gras c’est la vie).

## Trello

https://trello.com/invite/b/5qldxhTs/0cefac054afa47c7893eb89ff4129792/projet-8

## GitHub

https://github.com/GoswaTech/pur_beurre

---

## Plan de Test

### App Mugauth

#### But

Les tests de l'app <mugauth> servent à tester la bonne implémentation du modèle
AbstractUser.

#### Arborescence

- test_models
- - test_auth_user_model
- - test_authenticate
- - test_fields

### App Filler

#### But

Les tests de l'app <filler> consolident l'implémentation d'OpenFoodFacts dans
le site. Ils testent d'un côté la communication avec la base de données Django
et d'un autre la communication avec les serveurs d'OpenFoodFacts.

#### Arborescence

- test_functionnal
- - test_update_database
- - test_update_django
- test_integration
- - test_connexion
- - test_update_database

### App FoodFinder

#### But

Les tests de l'app <foodfinder> testent le fonctionnement global du frontend
ainsi que le fonctionnement de l'algorythme de recherche.

#### Arborescence

- test_algorythm
- - test_search_substitutes_by_category
- test_forms
- - test_search_form
- test_models
- - test_models_relations
- - test_food
- test_selenium
- - test_login
- test_views
- - test_home_template_used
- - test_search_perform_search_valid
- - test_search_perform_search_non_valid
