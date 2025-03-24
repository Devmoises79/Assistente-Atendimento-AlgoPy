import time
import pywhatkit as kit

def coletar_informacoes():
    """Interage com o usuário e coleta dados."""
    print("🎶 Bem-vindo ao Assistente de Recomendação de Instrumentos! 🎶\n")
    nome = input("Qual é o seu nome? ")
    estilo = input("Qual seu estilo musical favorito? ")
    experiencia = input("Você já toca algum instrumento? (Sim/Não) ")
    
    # Determinar perfil do usuário
    perfil = "Músico Iniciante" if experiencia.lower() == "não" else "Músico Experiente"
    
    return nome, estilo, perfil

def recomendar_instrumentos(perfil):
    """Recomenda instrumentos com base no perfil do usuário."""
    recomendacoes = {
        "Músico Iniciante": [
            ("Violão", "Yamaha C40"),
            ("Teclado", "Casio CT-X700"),
            ("Cajón", "Meinl Headliner"),
        ],
        "Músico Experiente": [
            ("Guitarra", "Fender Stratocaster"),
            ("Baixo", "Fender JazzBass"),
            ("Teclado", "Nord Stage 3"),
            ("Violino", "Stentor 1500"),
        ]
    }
    
    return recomendacoes.get(perfil, [])

def coletar_feedback():
    """Coleta a opinião e a nota do usuário."""
    opiniao = input("\nO que achou das recomendações? ")
    nota = input("De 0 a 10, qual sua nota para o atendimento? ")
    return opiniao, nota

def formatar_mensagem(nome, perfil, instrumentos, opiniao, nota):
    """Formata a mensagem de saída e do WhatsApp."""
    
    mensagem = (
        f"🎶 *Relatório Comercial* 🎶\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        f"👤 *Cliente:* {nome}\n"
        f"🎸 *Perfil Musical:* **{perfil}**\n"
        "🎼 *Instrumentos Recomendados:*\n"
    )

    for instrumento, modelo in instrumentos:
        emoji = "🎸" if instrumento in ["Guitarra", "Baixo"] else "🎻" if instrumento in ["Violino", "Violoncelo"] else "🎹"
        mensagem += f"   {emoji} **{instrumento}:** {modelo}\n"

    mensagem += (
        f"\n💬 *Opinião do Usuário:* **{opiniao}**\n"
        f"⭐ *Nota do Usuário:* **{nota}/10**\n"
        "━━━━━━━━━━━━━━━━━━━━━\n"
        "🙏 Obrigado por utilizar nosso serviço!\n"
        "Que tal explorar outros instrumentos? Entre em contato! 😉"
    )

    return mensagem

def enviar_mensagem_whatsapp(mensagem, numero):
    """Envia a mensagem formatada pelo WhatsApp Web."""
    print("\n📲 Enviando relatório via WhatsApp...\n")
    time.sleep(3)  # Simulação de espera antes do envio
    kit.sendwhatmsg_instantly(numero, mensagem, 15, True, 3)

# 🏁 Execução do fluxo
if __name__ == "__main__":
    nome, estilo, perfil = coletar_informacoes()
    instrumentos = recomendar_instrumentos(perfil)

    # Exibir recomendações no terminal
    print("\n🎼 Instrumentos Recomendados:")
    for instrumento, modelo in instrumentos:
        print(f"   - {instrumento}: {modelo}")

    opiniao, nota = coletar_feedback()

    # Formatar mensagem final
    mensagem_final = formatar_mensagem(nome, perfil, instrumentos, opiniao, nota)

    # Exibir a mensagem no terminal antes do envio
    print("\n📩 Mensagem que será enviada:")
    print(mensagem_final)

    numero_usuario = "+55XXXXXXXXX"  # 🔴 Substituir pelo número correto
    enviar_mensagem_whatsapp(mensagem_final, numero_usuario)

    print("\n✅ Atendimento finalizado! Obrigado por utilizar nosso serviço! 🎵")
