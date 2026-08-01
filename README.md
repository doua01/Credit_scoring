# Credit_scoring
Objectif : Construire un modèle de Machine Learning pour prédire si un client aura un défaut de paiement (c'est-à-dire s'il ne pourra pas rembourser son prêt). Nous utiliserons des variables numériques (comme l'âge ou le revenu) ET catégoriques (comme le statut d'emploi ou le niveau d'éducation).
Pourquoi c'est important ? Les banques utilisent ces modèles tous les jours pour décider d'accorder ou non un crédit. Un bon modèle permet de réduire les pertes financières de la banque tout en accordant des crédits aux personnes qui peuvent les rembourser.
Approche (Étape par étape) :
1.Exploration des données : Comprendre nos données avant de les utiliser.
2. Préparation : Nettoyer et transformer les données pour que l'ordinateur les comprenne.
3. Modélisation classique : Utiliser Scikit-Learn (KNN, Arbre de Décision, Random Forest).
4. Suivi avec MLflow : Apprendre à enregistrer et comparer nos modèles comme des pros.
5. Automatisation avec PyCaret : Voir comment simplifier tout ce processus.

Variables explicatives (Ce que le modèle utilise pour apprendre) :
- Numériques (7) : Age, Revenu, Montant_Credit, Duree_Mois, Score_Credit, Nb_Credits_Prec, Ratio_Dette_Revenu
- Catégoriques (5) : Statut_Emploi, Niveau_Education, Type_Propriete, Historique_Credit, Objet_Credit

Variable cible(Ce que le modèle doit deviner) : 
- Defaut_Paiement (0 = Pas de défaut, 1 = Défaut)
