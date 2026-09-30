import time
import requests
from playwright.sync_api import sync_playwright

BOT_TOKEN = "8623932861:AAF5nAb4JcEio1schFpDUkl8OpRvhya9ZL8"
CHAT_ID = "7709240530"

def enviar_sinal():
    mensagem = (
        "🚨 **SINAL CONFIRMADO - 1xBet** 🚨\n\n"
        "🎮 **Jogo:** Aviator\n"
        "🎯 **Entrada:** Buscar 7.00x (ou 9.00x)\n"
        "🛑 **Saída/Cashout:** Retirar em 7.00x\n"
        "📊 **Padrão:** 4 Velas Baixas Seguidas (< 1.50x)\n"
        "🏠 **Casa:** 1xBet\n"
        "⏰ **Entrada:** Próxima Vela"
    )
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": mensagem, "parse_mode": "Markdown"})

def iniciar():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://1xbet.com")
        time.sleep(10)

        historico_velas = []
        while True:
            try:
                elementos = page.query_selector_all(".payouts__item")
                if elementos:
                    ultimas = [float(el.inner_text().replace('x','').strip()) for el in elementos[:4] if el.inner_text().replace('x','').replace('.','',1).strip().isdigit()]
                    
                    if ultimas and ultimas != historico_velas:
                        historico_velas = ultimas
                        # Regra das 4 velas baixas
                        if len(ultimas) >= 4 and all(v < 1.50 for v in ultimas):
                            enviar_sinal()
                            time.sleep(40)
            except Exception as e:
                pass
            time.sleep(3)

if __name__ == "__main__":
    iniciar()
