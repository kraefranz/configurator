import streamlit as st
import urllib.parse
from urllib.parse import quote

st.set_page_config(page_title="Karl AI Konfigurator")

st.caption("Prototyp – Preise unverbindlich")

st.markdown(
    '<a href="https://www.dokumet.de" '
    'style="font-size:0.85rem; color:#666; text-decoration:none;">'
    '← Zur Hauptseite</a>',
    unsafe_allow_html=True
)

price_spacer, price_col = st.columns([3, 1])

with price_col:
    price_placeholder = st.empty()

with st.container(border=True):

    st.markdown(
        "<div style='color:#2b13c2; font-size:1.5rem; font-weight:600;'>"
        "Konfigurieren Sie Ihr Karl AI</div>",
        unsafe_allow_html=True
    )

    st.markdown("<div style='height:1rem;'></div>", unsafe_allow_html=True)

    st.markdown(
    "<div style='font-size:1.1rem; font-weight:600;'>"
    "Anzahl der Lizenzen"
    "</div>",
    unsafe_allow_html=True
    )

    option1 = st.selectbox(
        "",
        list(range(1, 26)) + ["> 25"],
        index=2, # 3 Lizenzen vorbelegt
        label_visibility="collapsed"
    )

    st.markdown(
    "<div style='font-size:1.1rem; font-weight:600;'>"
    "Lizenzdauer in Monaten"
    "</div>",
    unsafe_allow_html=True
    )

    option2 = st.selectbox(
        "",
        list(range(1, 37)) + ["> 36"],
        index=9,  # 10 Monate vorbelegt
        label_visibility="collapsed"
    )
    
    st.markdown(
    "<div style='font-size:1.1rem; font-weight:600;'>"
    "Begleitworkshop"
    "</div>",
    unsafe_allow_html=True
    )

    option3 = st.selectbox("Wünschen Sie einen einführenden Workshop?",
        ["Halber Tag online",
        "Ganzer Tag online",
        "Halber Tag Präsenz",
        "Ganzer Tag Präsenz",
        "Beratung gewünscht",
        "Nein"],
        index=4,
        label_visibility="collapsed")

    st.markdown(
    "<div style='font-size:1.1rem; font-weight:600;'>"
    "Login über organisationseigenes SSO"
    "</div>",
    unsafe_allow_html=True
    )

    option4 = st.selectbox("",
                           ["Ja",
                           "Nein",
                           "Beratung gewünscht"],
                           index=2,
                           label_visibility="collapsed")


# --- Live-Preis ---

abopreis = 39
sso = 3000
online_ws_halb = 450
online_ws_ganz = 900
praesenz_ws_halb = 700
praesenz_ws_ganz = 1200

preis = option1 * abopreis * option2 + (sso if option4 == "Ja" else 0) + (
    online_ws_halb if option3 == "Halber Tag online" else
    online_ws_ganz if option3 == "Ganzer Tag online" else
    praesenz_ws_halb if option3 == "Halber Tag Präsenz" else
    praesenz_ws_ganz if option3 == "Ganzer Tag Präsenz" else
    0
)

price_placeholder.markdown(
    f"""
    <div style="text-align:right; margin-bottom:1.5rem;">
        <div style="font-size:1.2rem; font-weight:600;">
            Preis ab {preis:,.0f} €
        </div>
        <div style="font-size:0.85rem;">
            (inkl. 19 % MwSt.)
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# --- CTA: Gespräch anfragen ---
subject = "Gesprächsanfrage Karl AI"

body = f"""Hallo,

ich habe den Karl AI Produktkonfigurator genutzt und bitte um ein Gespräch.

Konfiguration:
- Lizenzen: {option1}
- Lizenzdauer: {option2}
- SSO: {option3}
- Workshop: {option4}
- Preis ab: {preis} €

Bitte kontaktieren Sie mich unter: [Ihre Kontaktdaten]

Viele Grüße
"""

query = urllib.parse.urlencode({
    "subject": subject,
    "body": body
}).replace("+", "%20")

mailto_link = f"mailto:info@dokumet.de?{query}"

st.markdown("<div style='height:1rem;'></div>", unsafe_allow_html=True)

st.markdown(
    f'<div style="text-align:right;">'
    f'<a href="{mailto_link}"><button>Beratungsgespräch anfragen</button></a>'
    f'</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .karl-footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background: #2b13c2;
        color: white;
        padding: 1.2rem 2rem;
        z-index: 1000;
        font-size: 0.9rem;

        display: flex;
        align-items: center;
        gap: 1.5rem;
    }

    .karl-footer a {
        color: white;
        text-decoration: none;
        margin: 0;
    }
    </style>

    <div class="karl-footer">
        <span>© 2026 DokuMet QDA GmbH</span>
        <a href="#">AGB</a>
        <a href="#">Kontakt</a>
        <a href="#">Datenschutz</a>
        <a href="#">Impressum</a>
    </div>
    """,
    unsafe_allow_html=True
)

