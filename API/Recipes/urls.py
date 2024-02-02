from django.urls import path

from Recipes.views import AccessRecipeView, AddDietView, AllDiets, AutoComplete, \
    CreateDietView, \
    CreateIngredientView, \
    CreateRecipeView, \
    CreateStepView, DeleteIngredient, DeleteRecipe, DeleteStep, \
    IngredientsView, \
    RecipesView, \
    StepsView, UpdateDietView, UpdateIngredientView, \
    UpdateRecipeView, UpdateStepView, GetDiets, GetDietId, AddIngredientView

urlpatterns = [
    #Recipe
    path('all/', RecipesView.as_view()),
    path('create/', CreateRecipeView.as_view()),
    path('<int:recipe_id>/', AccessRecipeView.as_view()),
    path('<int:recipe_id>/update/', UpdateRecipeView),
    path('<int:recipe_id>/delete/', DeleteRecipe),

    #Ingredients
    path('<int:recipe_id>/ingredients/', IngredientsView.as_view()),
    path('<int:recipe_id>/add-ingredient/', CreateIngredientView.as_view()),
    path('<str:name>/add-to-ingredient/', AddIngredientView),
    path('<int:id>/update-ingredient/', UpdateIngredientView),
    path('<int:id>/delete-ingredient/', DeleteIngredient),

    #Diets
    path('<int:recipe_id>/diets/', AllDiets.as_view()),
    path('create-diet/', CreateDietView.as_view()),
    path('<int:id>/update-diet/', UpdateDietView),
    path('<str:name>/add-diet/', AddDietView),
    path('get-diets/', GetDiets.as_view()),
    path('<str:diet>/get-diet/', GetDietId.as_view()),


    #Steps
    path('<int:recipe_id>/steps/', StepsView.as_view()),
    path('<int:recipe_id>/create-step/', CreateStepView.as_view()),
    path('<int:id>/update-step/', UpdateStepView),
    path('<int:id>/delete-step/', DeleteStep),

    #autocomplete
    path('auto-complete/', AutoComplete)
]
