import requests
from discord.ext import commands

def ServerInfoCommand(bot: commands.Bot):
    @bot.command(name='serverinfo')
    async def serverinfo(ctx: commands.Context, invite_url: str = ""):
        if invite_url == "":
            await ctx.send(
                "You have to put a discord invite url --> https://discord.gg/server_invite (use **!h** for more information)")

        else:
            try:
                # Extraire le code de l'invitation
                invite_code = invite_url.split("/")[-1]

                # Envoyer une requête à l'API Discord pour obtenir les informations sur l'invitation
                response = requests.get(f"https://discord.com/api/v9/invites/{invite_code}")

                if response.status_code == 200:
                    data = response.json()
                    # Récupérer les informations nécessaires de l'invitation
                    type_value = data.get('type', 'None')
                    code_value = data.get('code', 'None')
                    inviter_id = data.get('inviter', {}).get('id', 'None')
                    inviter_username = data.get('inviter', {}).get('username', 'None')
                    inviter_avatar = data.get('inviter', {}).get('avatar', 'None')
                    inviter_discriminator = data.get('inviter', {}).get('discriminator', 'None')
                    expires_at = data.get('expires_at', 'None')
                    flags = data.get('flags', 'None')
                    server_id = data.get('guild', {}).get('id', 'None')
                    server_name = data.get('guild', {}).get('name', 'None')
                    server_icon = data.get('guild', {}).get('icon', 'None')
                    server_features = data.get('guild', {}).get('features', 'None')
                    server_verification_level = data.get('guild', {}).get('verification_level', 'None')
                    server_nsfw_level = data.get('guild', {}).get('nsfw_level', 'None')
                    server_premium_subscription_count = data.get('guild', {}).get('premium_subscription_count', 'None')
                    channel_id = data.get('channel', {}).get('id', 'None')
                    channel_name = data.get('channel', {}).get('name', 'None')

                    # Afficher les informations
                    await ctx.send(f"""
## Invitation Information:
**Invitation         :** {invite_url}
**Type               :** {type_value}
**Code               :** {code_value}
**Expired            :** {expires_at}
**Server ID          :** {server_id}
**Server Name        :** {server_name}
**Channel ID         :** {channel_id}
**Channel Name       :** {channel_name}
**Server Icon        :** {server_icon}
**Server Features    :** {server_features}
**Server NSFW Level  :** {server_nsfw_level}
**Flags              :** {flags}
**Server Verification Level          :** {server_verification_level}
**Server Premium Subscription Count  :** {server_premium_subscription_count}

## Inviter Information:
**ID             :** {inviter_id}
**Username       :** {inviter_username}
**Avatar         :** {inviter_avatar}
**Discriminator  :** {inviter_discriminator}""")

                else:
                    await ctx.send("Erreur lors de la récupération des informations de l'invitation.")
            except Exception as e:
                await ctx.send(f"Une erreur est survenue : {str(e)}")

    @bot.command(name='si')
    async def si(ctx: commands.Context, invite_url: str = ""):
        await serverinfo(ctx, invite_url)