import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

def MemberInfoCommand(bot: commands.Bot):
    def MemberInfoCommand(bot: commands.Bot):
        @bot.command(name='memberinfo')
        async def memberinfo(ctx: commands.Context, member: discord.Member = None):
            member = ctx.author if member is None else member

            username = member.name
            global_user_name = member.global_name
            user_id = member.id
            user_avatar = member.avatar

            def safe_mention(role: discord.Role):
                return f"<@&{role.id}>"

            staff_roles = [
                "STAFF", "Administrateur ||💎", "Modérateur", "Helper", "Responsable Staff || 🧠", "Modérateur sécurité",
                "Modérateur aide au besoin", "Modérateur communications", "Co-créateur||🐳",
                "Créateur ||🦈", "Bot Rp-Fr Battlefront II"
            ]

            excluded_roles = [
                "-----------type de soldat-----------", "------------grade clone-------------",
                "--------------Régiment--------------", "--------------Spécialité------------",
                "-----------Gardiens de la paix-----------",
                "-----------types de vaisseaux-----------", "---------------grade-------------- ",
                "République", "---------------grade--------------"
            ]

            platform_roles = ["PS4", "PS5"]
            session_launcher_roles = ["Lanceur de session"]

            user_roles = [role for role in member.roles if role.name != "@everyone" and role.name not in excluded_roles]

            user_staff_roles = []
            user_senat_roles = []
            type_de_soldat = []
            specialite = []
            regiment = []
            grade_clone = []
            formateur = []
            instructeur = []
            notifications = []
            jedi = []
            platform = []
            session_launcher = []
            other_roles = []
            not_member_roles = []

            for role in user_roles:
                if role.name in staff_roles:
                    user_staff_roles.append(safe_mention(role))
                elif role.name in ["Responsable Sénat", "Sénateur"]:
                    user_senat_roles.append(safe_mention(role))
                elif role.name in ["commando", "Soldat lourd", "officier", "spécialiste"]:
                    type_de_soldat.append(safe_mention(role))
                elif role.name in ["soldat cra", "Spécialité double", "commandant clone", "jet trooper", "wookies",
                                   "Recrue SOLDAT CRA", "Recrue COMMANDO CLONE", "Recrue JET-TROOPER",
                                   "Recrue wookiee"]:
                    specialite.append(safe_mention(role))
                elif role.name in ["chef de régiment", "second de régiment", "501éme Légion", "Garde de Coruscant",
                                   "104éme wolfpack", "327e-corps-stellaire", "212ème bataillon d'attaque",
                                   "41éme corps d'élite", "Pilote de char"]:
                    regiment.append(safe_mention(role))
                elif role.name in ["Colonel", "Lieutenant Colonel", "Commandant", "Capitaine", "Capitaine en second",
                                   "Lieutenant", "Lieutenant en second", "Major", "Major aspirant", "Adjudant chef",
                                   "Adjudant", "Sergent major", "Sergent", "Caporal-chef", "Caporal", "Clone trooper",
                                   "Cadet clone trooper", "général"]:
                    grade_clone.append(safe_mention(role))
                elif "notifications" in role.name.lower():
                    notifications.append(safe_mention(role))
                elif role.name in ["Maître jedi", "Chevalier jedi", "Padawan", "Initié"]:
                    jedi.append(safe_mention(role))
                elif role.name in ["Instructeur"]:
                    instructeur.append(safe_mention(role))
                elif role.name in ["Formateur Commando", "Formateur Jet-Trooper", "Apprenti formateur"]:
                    formateur.append(safe_mention(role))
                elif role.name in platform_roles:
                    platform.append(safe_mention(role))
                elif role.name in session_launcher_roles:
                    session_launcher.append(safe_mention(role))
                elif role.name in ["Candidature à faire", "Oral à faire"]:
                    not_member_roles.append(safe_mention(role))
                else:
                    other_roles.append(safe_mention(role))

            formatted_staff = " **|** ".join(user_staff_roles) if user_staff_roles else "Aucun"
            formatted_senat = " **|** ".join(user_senat_roles) if user_senat_roles else "Non"
            formatted_formateur = " **|** ".join(formateur) if formateur else "Non"
            formatted_instructeur = "Oui" if instructeur else "Non"
            formatted_type_de_soldat = " **|** ".join(type_de_soldat) if type_de_soldat else "Aucun"
            formatted_specialite = " **|** ".join(specialite) if specialite else "Aucune"
            formatted_regiment = " **|** ".join(regiment) if regiment else "Aucun"
            formatted_grade_clone = " **|** ".join(grade_clone) if grade_clone else "Aucun"
            formatted_notifications = " **|** ".join(notifications) if notifications else "Aucune"
            formatted_jedi = " **|** ".join(jedi) if jedi else "Non"
            formatted_platform = " **|** ".join(platform) if platform else "Aucune"
            formatted_session_launcher = "oui" if session_launcher else "Non"
            formatted_other_roles = " **|** ".join(other_roles) if other_roles else "Aucun"
            formatted_not_member = "Non" if not_member_roles else "Oui"

            if any(role.name == "général" for role in member.roles):
                await ctx.send(f"""
## 🌍  Informations général
``Membre name:`` **{username}**
``Membre global name:`` **{global_user_name}**
``Membre ID:`` **{user_id}**
``Membre avatar:`` **[cdn.discordapp.com]({user_avatar})**

## 👑  Grade à responsabilité
``Member est staff:`` **{formatted_staff}**
``Membre est sénateur:`` **{formatted_senat}**

## 🏹  Grade RP
``Membre est formateur:`` **{formatted_formateur}**
``Membre est instructeur:`` **{formatted_instructeur}**
``Type de soldat:`` **{formatted_type_de_soldat}**
``Spécialité:`` **{formatted_specialite}**
``Régiment:`` **{formatted_regiment}**
``Grade:`` **{formatted_grade_clone}**
``Lanceur de session:`` **{formatted_session_launcher}**
``Jedi:`` **{formatted_jedi}**

## 🎭  Grade HRP
``Platforme:`` **{formatted_platform}**
``Notifications:`` **{formatted_notifications}**
``Membre vérifié:`` **{formatted_not_member}**
``Autres rôles:`` **{formatted_other_roles}**


© wivex""")

            else:
                await ctx.send(f"""
## 🌍  Informations général
``Membre name:`` **{username}**
``Membre global name:`` **{global_user_name}**
``Membre ID:`` **{user_id}**
``Membre avatar:`` **[cdn.discordapp.com]({user_avatar})**

## 👑  Grade à responsabilité
``Member est staff:`` **{formatted_staff}**
``Membre est sénateur:`` **{formatted_senat}**

## 🏹  Grade RP
``Membre est formateur:`` **{formatted_formateur}**
``Membre est instructeur:`` **{formatted_instructeur}**
``Type de soldat:`` **{formatted_type_de_soldat}**
``Spécialité:`` **{formatted_specialite}**
``Régiment:`` **{formatted_regiment}**
``Grade clone:`` **{formatted_grade_clone}**
``Lanceur de session:`` **{formatted_session_launcher}**
``Jedi:`` **{formatted_jedi}**

## 🎭  Grade HRP
``Platforme:`` **{formatted_platform}**
``Notifications:`` **{formatted_notifications}**
``Membre vérifié:`` **{formatted_not_member}**
``Autres rôles:`` **{formatted_other_roles}**


© wivex""")

    @bot.command(name='mi')
    async def mi(ctx: commands.Context, member: discord.Member = None):
        member = ctx.author if member is None else member

        username = member.name
        global_user_name = member.global_name
        user_id = member.id
        user_avatar = member.avatar

        def safe_mention(role: discord.Role):
            return f"<@&{role.id}>"

        staff_roles = [
            "STAFF", "Administrateur ||💎", "Modérateur", "Helper", "Responsable Staff || 🧠", "Modérateur sécurité",
            "Modérateur aide au besoin", "Modérateur communications", "Co-créateur||🐳",
            "Créateur ||🦈", "Bot Rp-Fr Battlefront II"
        ]

        excluded_roles = [
            "-----------type de soldat-----------", "------------grade clone-------------",
            "--------------Régiment--------------", "--------------Spécialité------------",
            "-----------Gardiens de la paix-----------",
            "-----------types de vaisseaux-----------", "---------------grade-------------- ",
            "République", "---------------grade--------------"
        ]

        platform_roles = ["PS4", "PS5"]
        session_launcher_roles = ["Lanceur de session"]

        user_roles = [role for role in member.roles if role.name != "@everyone" and role.name not in excluded_roles]

        user_staff_roles = []
        user_senat_roles = []
        type_de_soldat = []
        specialite = []
        regiment = []
        grade_clone = []
        formateur = []
        instructeur = []
        notifications = []
        jedi = []
        platform = []
        session_launcher = []
        other_roles = []
        not_member_roles = []

        for role in user_roles:
            if role.name in staff_roles:
                user_staff_roles.append(safe_mention(role))
            elif role.name in ["Responsable Sénat", "Sénateur"]:
                user_senat_roles.append(safe_mention(role))
            elif role.name in ["commando", "Soldat lourd", "officier", "spécialiste"]:
                type_de_soldat.append(safe_mention(role))
            elif role.name in ["soldat cra", "Spécialité double", "commando clone", "jet trooper", "wookies",
                               "Recrue SOLDAT CRA", "Recrue COMMANDO CLONE", "Recrue JET-TROOPER",
                               "Recrue wookiee"]:
                specialite.append(safe_mention(role))
            elif role.name in ["chef de régiment", "second de régiment", "501éme Légion", "Garde de Coruscant",
                               "104éme wolfpack", "327e-corps-stellaire", "212ème bataillon d'attaque",
                               "41éme corps d'élite", "Pilote de char"]:
                regiment.append(safe_mention(role))
            elif role.name in ["Colonel", "Lieutenant Colonel", "Commandant", "Capitaine", "Capitaine en second",
                               "Lieutenant", "Lieutenant en second", "Major", "Major aspirant", "Adjudant chef",
                               "Adjudant", "Sergent major", "Sergent", "Caporal-chef", "Caporal", "Clone trooper",
                               "Cadet clone trooper", "général"]:
                grade_clone.append(safe_mention(role))
            elif "notifications" in role.name.lower():
                notifications.append(safe_mention(role))
            elif role.name in ["Maître jedi", "Chevalier jedi", "Padawan", "Initié"]:
                jedi.append(safe_mention(role))
            elif role.name in ["Instructeur"]:
                instructeur.append(safe_mention(role))
            elif role.name in ["Formateur Commando", "Formateur Jet-Trooper", "Apprenti formateur"]:
                formateur.append(safe_mention(role))
            elif role.name in platform_roles:
                platform.append(safe_mention(role))
            elif role.name in session_launcher_roles:
                session_launcher.append(safe_mention(role))
            elif role.name in ["Candidature à faire", "Oral à faire"]:
                not_member_roles.append(safe_mention(role))
            else:
                other_roles.append(safe_mention(role))

        formatted_staff = " **|** ".join(user_staff_roles) if user_staff_roles else "Aucun"
        formatted_senat = " **|** ".join(user_senat_roles) if user_senat_roles else "Non"
        formatted_formateur = " **|** ".join(formateur) if formateur else "Non"
        formatted_instructeur = "Oui" if instructeur else "Non"
        formatted_type_de_soldat = " **|** ".join(type_de_soldat) if type_de_soldat else "Aucun"
        formatted_specialite = " **|** ".join(specialite) if specialite else "Aucune"
        formatted_regiment = " **|** ".join(regiment) if regiment else "Aucun"
        formatted_grade_clone = " **|** ".join(grade_clone) if grade_clone else "Aucun"
        formatted_notifications = " **|** ".join(notifications) if notifications else "Aucune"
        formatted_jedi = " **|** ".join(jedi) if jedi else "Non"
        formatted_platform = " **|** ".join(platform) if platform else "Aucune"
        formatted_session_launcher = "oui" if session_launcher else "Non"
        formatted_other_roles = " **|** ".join(other_roles) if other_roles else "Aucun"
        formatted_not_member = "Non" if not_member_roles else "Oui"

        if any(role.name == "général" for role in member.roles):
            await ctx.send(f"""
## 🌍  Informations général
``Membre name:`` **{username}**
``Membre global name:`` **{global_user_name}**
``Membre ID:`` **{user_id}**
``Membre avatar:`` **[cdn.discordapp.com]({user_avatar})**

## 👑  Grade à responsabilité
``Member est staff:`` **{formatted_staff}**
``Membre est sénateur:`` **{formatted_senat}**

## 🏹  Grade RP
``Membre est formateur:`` **{formatted_formateur}**
``Membre est instructeur:`` **{formatted_instructeur}**
``Type de soldat:`` **{formatted_type_de_soldat}**
``Spécialité:`` **{formatted_specialite}**
``Régiment:`` **{formatted_regiment}**
``Grade:`` **{formatted_grade_clone}**
``Lanceur de session:`` **{formatted_session_launcher}**
``Jedi:`` **{formatted_jedi}**

## 🎭  Grade HRP
``Platforme:`` **{formatted_platform}**
``Notifications:`` **{formatted_notifications}**
``Membre vérifié:`` **{formatted_not_member}**
``Autres rôles:`` **{formatted_other_roles}**


© wivex""")

        else:
            await ctx.send(f"""
## 🌍  Informations général
``Membre name:`` **{username}**
``Membre global name:`` **{global_user_name}**
``Membre ID:`` **{user_id}**
``Membre avatar:`` **[cdn.discordapp.com]({user_avatar})**

## 👑  Grade à responsabilité
``Member est staff:`` **{formatted_staff}**
``Membre est sénateur:`` **{formatted_senat}**

## 🏹  Grade RP
``Membre est formateur:`` **{formatted_formateur}**
``Membre est instructeur:`` **{formatted_instructeur}**
``Type de soldat:`` **{formatted_type_de_soldat}**
``Spécialité:`` **{formatted_specialite}**
``Régiment:`` **{formatted_regiment}**
``Grade clone:`` **{formatted_grade_clone}**
``Lanceur de session:`` **{formatted_session_launcher}**
``Jedi:`` **{formatted_jedi}**

## 🎭  Grade HRP
``Platforme:`` **{formatted_platform}**
``Notifications:`` **{formatted_notifications}**
``Membre vérifié:`` **{formatted_not_member}**
``Autres rôles:`` **{formatted_other_roles}**


© wivex""")