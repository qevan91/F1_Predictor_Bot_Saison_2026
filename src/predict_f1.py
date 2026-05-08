import os
from typing import Literal

# Third-party library modules
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

# Local modules
import api_f1
import data_manager

# Configuration
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

# Discord Bot Token
TOKEN = os.getenv('TOKEN')

# Discord IDs of administrator roles
ADMIN_ROLE1 = os.getenv('ADMIN_ROLE1')
ADMIN_ROLE2 = os.getenv('ADMIN_ROLE2')
ADMIN_ROLE3 = os.getenv('ADMIN_ROLE3')

ADMIN_ROLES = [ADMIN_ROLE1, ADMIN_ROLE2, ADMIN_ROLE3]

PiloteF1 = Literal[
    "Verstappen", "Lawson", "Hamilton", "Leclerc", "Norris", "Piastri",
    "Russell", "Antonelli", "Alonso", "Stroll", "Sainz", "Albon",
    "Gasly", "Doohan", "Ocon", "Bearman", "Hülkenberg", "Bortoleto",
    "Tsunoda", "Hadjar"
]

EcurieF1 = Literal[
    "Red Bull", "Ferrari", "McLaren", "Mercedes", "Aston Martin",
    "Williams", "Alpine", "Haas", "Audi", "RB"
]


class F1Bot(commands.Bot):
    # Main Discord bot class

    def __init__(self):
        # Initializes the bot with required intents
        super().__init__(command_prefix='!', intents=discord.Intents.all())

    async def setup_hook(self):
        # Synchronizes slash commands on bot startup
        await self.tree.sync()
        print("Commandes Slash (/) synchronisées.")


bot = F1Bot()


@bot.event
async def on_ready():
    # Terminal debug when the bot is connected and ready
    print(f'Bot F1 Predictor lancé : {bot.user.name}')


# Player commands (Accessible only with "/")

@bot.tree.command(
    name="prochain_gp",
    description="Récupère les infos du prochain Grand Prix."
)
async def prochain_gp(interaction: discord.Interaction):
    """Displays information about the next Grand Prix via the API."""
    await interaction.response.defer()
    message = api_f1.fetch_next_gp()

    if message is not None:
        await interaction.followup.send(message)
    else:
        await interaction.followup.send("❌ Impossible de joindre l'API.")


@bot.tree.command(
    name="prono",
    description="Fais tes prédictions pour le prochain Grand Prix !"
)
@app_commands.describe(
    q1="1er en Qualifications", q2="2ème", q3="3ème",
    r1="Gagnant Course", r2="2ème", r3="3ème", r4="4ème", r5="5ème",
    r6="6ème", r7="7ème", r8="8ème", r9="9ème", r10="10ème",
    meilleure_equipe="Équipe marquant le plus de points",
    voiture_de_securite="Voiture de sécurité (Safety Car) ?",
    nombre_abandons="Combien de voitures vont abandonner ?",
    noms_abandons="Pilotes qui abandonnent (séparés par une virgule)",
    pilote_du_jour="Élu pilote du jour",
    plus_de_depassements="Pilote avec le plus de dépassements"
)
async def prono(
                interaction: discord.Interaction,
                q1: PiloteF1, q2: PiloteF1, q3: PiloteF1,
                r1: PiloteF1, r2: PiloteF1, r3: PiloteF1, r4: PiloteF1, r5: PiloteF1,
                r6: PiloteF1, r7: PiloteF1, r8: PiloteF1, r9: PiloteF1, r10: PiloteF1,
                meilleure_equipe: EcurieF1, voiture_de_securite: bool,
                nombre_abandons: int, noms_abandons: str,
                pilote_du_jour: PiloteF1, plus_de_depassements: PiloteF1
                ):
    # Saves a user's predictions
    user_id = str(interaction.user.id)
    predictions = data_manager.load_data(data_manager.DATA_FILE)

    noms_abandons_formates = [
        nom.strip().capitalize() for nom in noms_abandons.split(',')
    ] if noms_abandons else []

    predictions[user_id] = {
        "username": interaction.user.name,
        "q_top3": [q1, q2, q3],
        "r_top10": [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10],
        "ecurie": meilleure_equipe,
        "sc": voiture_de_securite,
        "dnf_count": nombre_abandons,
        "dnf_names": noms_abandons_formates,
        "dotd": pilote_du_jour,
        "overtakes": plus_de_depassements
    }

    data_manager.save_data(predictions, data_manager.DATA_FILE)
    message_confirmation = (
        f"✅ Tes pronostics ont été enregistrés, **{interaction.user.name}** !"
    )
    await interaction.response.send_message(
        message_confirmation,
        ephemeral=True
    )


@bot.tree.command(
    name="classement",
    description="Voir le classement général de la saison."
)
async def classement(interaction: discord.Interaction):
    # Displays the overall standings sorted by points
    scores = data_manager.load_data(data_manager.SCORES_FILE)
    if not scores:
        return await interaction.response.send_message("📊 Classement vide.")

    # Sorts scores by points, in descending order
    scores_tries = sorted(
        scores.items(),
        key=lambda element: element[1]['points'],
        reverse=True
    )

    message = "**🏆 CLASSEMENT GÉNÉRAL 🏆**\n"
    for index, (uid, data) in enumerate(scores_tries, 1):
        if index == 1:
            medaille = "🥇"
        elif index == 2:
            medaille = "🥈"
        elif index == 3:
            medaille = "🥉"
        else:
            medaille = f"{index}."

        message += f"{medaille} <@{uid}> : **{data['points']} points**\n"

    await interaction.response.send_message(message)


# Admin commands (Accessible only with "/")

@bot.tree.command(
    name="auto_resultats",
    description="[ADMIN] Calcule les points automatiquement via l'API."
)
@app_commands.describe(
    ecurie_reelle="Équipe qui a marqué le plus de points",
    sc_reelle="Y a-t-il eu une voiture de sécurité ?",
    dotd_reel="Pilote du jour officiel",
    overtakes_reel="Pilote avec le plus de dépassements"
)
@app_commands.checks.has_any_role(*ADMIN_ROLES)
async def auto_resultats(
        interaction: discord.Interaction,
        ecurie_reelle: EcurieF1,
        sc_reelle: bool,
        dotd_reel: PiloteF1,
        overtakes_reel: PiloteF1
):
    # Calculates scores by fetching factual data from the API
    await interaction.response.defer()

    resultats_q3 = api_f1.fetch_last_quali_data()
    resultats_r10, nombre_abandons_reel, abandons = api_f1.fetch_last_race_data()

    if resultats_q3 is None or resultats_r10 is None:
        return await interaction.followup.send(
            "❌ Erreur API. Utilise la commande manuelle."
        )

    predictions = data_manager.load_data(data_manager.DATA_FILE)
    scores = data_manager.load_data(data_manager.SCORES_FILE)

    rapport, _ = calculate_points(
        predictions, scores, resultats_q3, resultats_r10, ecurie_reelle,
        sc_reelle, nombre_abandons_reel, abandons, dotd_reel, overtakes_reel
    )

    data_manager.save_data(scores, data_manager.SCORES_FILE)
    await interaction.followup.send(rapport)


@bot.tree.command(
    name="resultats_manuels",
    description="[ADMIN] Valide les résultats à la main."
)
@app_commands.describe(
    q1="1er Qualif", q2="2ème Qualif", q3="3ème Qualif",
    r1="P1 Course", r2="P2", r3="P3", r4="P4", r5="P5",
    r6="P6", r7="P7", r8="8ème", r9="9ème", r10="10ème",
    ecurie_reelle="Équipe avec le plus de points",
    sc_reelle="Voiture de sécurité ? (Vrai/Faux)",
    nombre_abandons="Nombre total d'abandons",
    noms_abandons="Noms des abandons (sépare par une virgule)",
    dotd_reel="Pilote du jour",
    overtakes_reel="Plus de dépassements"
)
@app_commands.checks.has_any_role(*ADMIN_ROLES)
async def resultats_manuels(
        interaction: discord.Interaction,
        q1: PiloteF1, q2: PiloteF1, q3: PiloteF1,
        r1: PiloteF1, r2: PiloteF1, r3: PiloteF1, r4: PiloteF1, r5: PiloteF1,
        r6: PiloteF1, r7: PiloteF1, r8: PiloteF1, r9: PiloteF1, r10: PiloteF1,
        ecurie_reelle: EcurieF1, sc_reelle: bool,
        nombre_abandons: int, noms_abandons: str,
        dotd_reel: PiloteF1, overtakes_reel: PiloteF1
):
    # Calculates scores using manually entered data
    await interaction.response.defer()

    predictions = data_manager.load_data(data_manager.DATA_FILE)
    scores = data_manager.load_data(data_manager.SCORES_FILE)

    if not predictions:
        return await interaction.followup.send(
            "⚠️ Impossible de calculer : aucun pronostic en cours."
        )

    resultats_q3 = [q1, q2, q3]
    resultats_r10 = [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10]
    noms_abandons_formates = [
        nom.strip().capitalize() for nom in noms_abandons.split(',')
    ] if noms_abandons else []

    rapport, _ = calculate_points(
        predictions, scores, resultats_q3, resultats_r10, ecurie_reelle,
        sc_reelle, nombre_abandons, noms_abandons_formates, dotd_reel,
        overtakes_reel
    )

    data_manager.save_data(scores, data_manager.SCORES_FILE)

    message_final = "🚨 **RÉSULTATS SAISIS MANUELLEMENT** 🚨\n\n" + rapport
    await interaction.followup.send(message_final)


@bot.tree.command(
    name="modifier_score",
    description="[ADMIN] Modifie manuellement les points d'un joueur."
)
@app_commands.checks.has_any_role(*ADMIN_ROLES)
async def modifier_score(
        interaction: discord.Interaction,
        joueur: discord.User,
        points: int
):
    # Adds or removes points for a specific user
    scores = data_manager.load_data(data_manager.SCORES_FILE)
    user_id = str(joueur.id)

    if user_id not in scores:
        scores[user_id] = {"username": joueur.name, "points": 0}

    scores[user_id]['points'] += points
    data_manager.save_data(scores, data_manager.SCORES_FILE)

    message = (
        f"✅ Nouveau score pour {joueur.name} : "
        f"{scores[user_id]['points']} points."
    )
    await interaction.response.send_message(message)


@bot.tree.command(
    name="reset_pronos",
    description="[ADMIN] Efface les pronostics du dernier Grand Prix."
)
@app_commands.checks.has_any_role(*ADMIN_ROLES)
async def reset_pronos(interaction: discord.Interaction):
    # Clears the prediction file for the following weekend
    data_manager.save_data({}, data_manager.DATA_FILE)
    await interaction.response.send_message("🧹 Pronostics réinitialisés.")


# Calculation logic

def calculate_points(
        predictions, scores, resultats_q3, resultats_r10, resultat_ecurie,
        resultat_sc, nombre_abandons, noms_abandons, resultat_dotd, resultat_overtakes
):
    """Compares predictions to results and awards points.

    Args:
        predictions (dict): User predictions.
        scores (dict): Current season scores.
        resultats_q3 (list): Official Top 3 of the qualifications.
        resultats_r10 (list): Official Top 10 of the race.
        resultat_ecurie (str): Team that scored the most points.
        resultat_sc (bool): True if a Safety Car was deployed.
        nombre_abandons (int): Official number of DNFs.
        noms_abandons (list): Official names of drivers who DNF'd.
        resultat_dotd (str): Official Driver of the Day.
        resultat_overtakes (str): Driver who made the most overtakes.

    Returns:
        tuple: (rapport_texte, points_de_la_session)
    """
    rapport = "**🏁 RÉSULTATS DU GRAND PRIX :**\n"
    points_session = {}

    for user_id, prediction in predictions.items():
        points_gagnes = 0

        # Qualification points
        for index, pilote in enumerate(prediction['q_top3']):
            if index < len(resultats_q3) and pilote == resultats_q3[index]:
                points_gagnes += (5 + (3 - index))
            elif pilote in resultats_q3:
                points_gagnes += 2

        # Race points
        for index, pilote in enumerate(prediction['r_top10']):
            if index < len(resultats_r10) and pilote == resultats_r10[index]:
                points_gagnes += (5 + (10 - index))
            elif pilote in resultats_r10:
                points_gagnes += 2

        # Team, SC, and Number of DNFs points
        if prediction.get('ecurie') == resultat_ecurie:
            points_gagnes += 5
        if prediction['sc'] == resultat_sc:
            points_gagnes += 2
        if prediction['dnf_count'] == nombre_abandons:
            points_gagnes += 3

        # DNF Names points
        for pilote_abandon in prediction['dnf_names']:
            if pilote_abandon in noms_abandons:
                points_gagnes += 2

        # Special bonus points
        if prediction['dotd'] == resultat_dotd:
            points_gagnes += 5
        if prediction['overtakes'] == resultat_overtakes:
            points_gagnes += 5

        # Save points
        points_session[user_id] = points_gagnes

        if user_id not in scores:
            scores[user_id] = {"username": prediction['username'], "points": 0}

        scores[user_id]['points'] += points_gagnes
        rapport += (
            f"- <@{user_id}> : +{points_gagnes} points "
            f"(Total: {scores[user_id]['points']})\n"
        )

    # Add the weekend's winner
    if points_session:
        score_maximum = max(points_session.values())
        gagnants = [
            f"<@{uid}>"
            for uid, score in points_session.items() if score == score_maximum
        ]
        rapport += (
            f"\n🏆 Félicitations à {', '.join(gagnants)} "
            f"avec **{score_maximum} points** sur ce week-end !"
        )

    return rapport, points_session


@bot.tree.error
async def on_app_command_error(
        interaction: discord.Interaction,
        error: app_commands.AppCommandError
):
    # Handles errors related to slash commands
    if isinstance(error, app_commands.MissingAnyRole):
        message_erreur = (
            "❌ Accès refusé. Tu dois posséder un rôle administrateur "
            "pour utiliser cette commande."
        )
        await interaction.response.send_message(
            message_erreur,
            ephemeral=True
        )
    else:
        print(f"Erreur inattendue : {error}")


if __name__ == "__main__":
    bot.run(TOKEN)