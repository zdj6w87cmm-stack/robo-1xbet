import time
import requests

BOT_TOKEN = "8623932861:AAF5nAb4JcEio1schFpDUkl8OpRvhya9ZL8"
CHAT_ID = "7709240530"

def enviar_sinal():
    mensagem = (
        "🚨 **SINAL CONFIRMADO - 1xBet**\n"
        "🎮 **Jogo:** Aviator\n"
        "🎯 **Entrada:** Buscar 7.00x\n"
        "🔴 **Saída/Cashout:** Retirar em 7.00x\n"
        "📊 **Padrão:** 4 Velas Baixas\n"
        "🏠 **Casa:** 1xBet\n"
        "⏰ **Entrada:** Próxima Vela"
    )
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": mensagem,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, json=payload)
        print("Sinal enviado com sucesso para o Telegram!")
    except Exception as e:
        print(f"Erro ao enviar: {e}")

def iniciar():
    print("Robô iniciado com sucesso (versão leve)...")
    while True:
        # Simulação de verificação e envio periódico de teste
        enviar_sinal()
        time.sleep(300) # Espera 5 minutos antes de enviar outro sinal de teste

if __name__ == "__main__":
    iniciar()
