# Plan de Test

*Ce plan de test est sous forme de markdown afin d'être simplement modifiable.*

## In Scope

### App Mugauth

#### But

Les tests de l'app <mugauth> servent à tester la bonne implémentation du modèle
AbstractUser.

#### Arborescence

- test_models
  - test_auth_user_model
  - test_authenticate
  - test_fields

  ---

### App Filler

#### But

Les tests de l'app <filler> consolident l'implémentation d'OpenFoodFacts dans
le site. Ils testent d'un côté la communication avec la base de données Django
et d'un autre la communication avec les serveurs d'OpenFoodFacts.

#### Arborescence

- test_functionnal
  - test_update_database
  - test_update_django
- test_integration
  - test_connexion
  - test_update_database

  ---

### App FoodFinder

#### But

Les tests de l'app <foodfinder> testent le fonctionnement global du frontend
ainsi que le fonctionnement de l'algorythme de recherche.

#### Arborescence

- test_algorythm
  - test_search_substitutes_by_category
- test_forms
  - test_search_form
- test_models
  - test_models_relations
  - test_food
- test_selenium
  - test_login
- test_views
  - test_home_template_used
  - test_search_perform_search_valid
  - test_search_perform_search_non_valid

---

### App Favor

#### But

Les tests de l'app <favor> testent le lien entre les favoris et la nourriture.
Aussi, ils tests le fonctionnement du lien d'ajout aux favoris.

#### Arborescence

- test_models
  - test_models_relations
- test_views
  - test_add_favor_non_valid_code
  - test_add_favor_valid_code

## Out Scope

- Django Admin
- Old Food Manager Methods
