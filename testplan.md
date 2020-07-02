# Plan de Test

*Ce plan de test est sous forme de markdown afin d'être simplement modifiable.*

## Introduction

**Périmètre :**

Nous allons majoritairement réaliser des tests fonctionnels ainsi que des tests
d'intégration.

**Outils :**

- django.test (extends unittest)
- selenium
- unittest.mock > MagicMock
- coverage

**Organisation :**

L'organisation des tests se fait par rapport à l'app en elle-même, c'est à dire
que chaque app possède sa propre arborescence et points importants. Autrement
dit, il n'y a pas d'organisation standard. L'organisation de chaque app est
détaillée plus bas.

**Temporalité :**

Les tests sont écrits en même temps que les méthodes testées. Nous commençons
par coder le squelette de la classe dans le dossier de test puis nous codons
cette dite classe pour enfin compléter le test et y insérer les assertions et
éventuellement ajouter d'autres tests complémentaires testant des points
sensibles de la classe.

## In Scope

*C'est ici que sont détaillées les organisations des tests de chaque app.
Vous y trouverai le but du dossier de tests ainsi que l'arborescence de chaque
dossier.*

---

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
- Test de Performances
- Test de Charge
- Test de Sécurité
